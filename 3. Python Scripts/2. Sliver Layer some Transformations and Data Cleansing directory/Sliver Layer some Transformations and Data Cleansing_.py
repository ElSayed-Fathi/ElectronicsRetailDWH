#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyodbc
import pandas as pd
import os
from sqlalchemy import create_engine
import urllib


# # Sliver Layer some Transformations and Data Cleansing 

# # Access the data from staging_db (Bronze Layer)

# In[2]:


pyodbc.drivers()


# In[49]:


# access destination to write data in database
params = urllib.parse.quote_plus(
r"Driver={ODBC Driver 17 for SQL Server};"
r"server=your_server;"
r"Database=your_desination_database;"
r"Trusted_Connection=yes;"    
)


conn = pyodbc.connect(connecting_str)
print("Connection is succesufly")


# In[50]:


query = ''' select * from bronze_customers'''


# In[51]:


silver_customers = pd.read_sql(query,conn)
silver_customers.head()


# In[19]:


silver_customers.info()


# In[ ]:





# In[ ]:





# ## Identify Fact and Dimension Tables

# ## 1 - Customer Dimension  Dim >> Dimension

# In[58]:


# Change Data Types for multiple columns from object to string
cols = ["Gender", "Name", "City","State Code","State","Zip Code","Country","Continent"]
silver_customers[cols] = silver_customers[cols].astype("string")


# In[59]:


silver_customers['Birthday'] = pd.to_datetime(silver_customers['Birthday'])


# In[60]:


silver_customers.shape


# In[61]:


# remove duplicates
silver_customers = silver_customers.drop_duplicates(subset=["CustomerKey"]).copy()


# In[62]:


silver_customers.shape


# In[63]:


# Add surrogate key if needed
silver_customers["CustomerSK"] = range(1, len(silver_customers) + 1)


# In[64]:


silver_customers.head()


# In[65]:


silver_customers = silver_customers[[
    "CustomerSK",          # Surrogate Key
    "CustomerKey",         # Natural Key
    "Name",
    "Gender",
    "Birthday",
    "City",
    "State Code",
    "State",
    "Zip Code",
    "Country",
    "Continent"
]]


# In[66]:


silver_customers.head()


# # Make Connection To Microsoft SQL SERVER Database To Put silver_customers_Dim Table in Staging Database

# In[2]:


# access destination to write data in database
params = urllib.parse.quote_plus(
r"Driver={ODBC Driver 17 for SQL Server};"
r"server=your_server;"
r"Database=your_desination_database;"
r"Trusted_Connection=yes;"    
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")


# In[24]:


# write data in database
silver_customers.to_sql("silver_customers_Dim",engine,index=False)


# # =================================================

# # 2 - Store Dimension

# In[83]:


query1 = ''' select * from bronze_stores'''


# In[84]:


silver_stores = pd.read_sql(query1,conn)
silver_stores.head()


# In[85]:


silver_stores.info()


# In[86]:


# Change Data Types for multiple columns from object to string
cols2 = ["Country", "State"]
silver_stores[cols2] = silver_stores[cols2].astype("string")


# In[87]:


silver_stores = silver_stores.drop_duplicates(subset=["StoreKey"]).copy()


# ### not needed suroggate keys because StoreKey is good   SK >> suroggate Key

# # Make Connection To Microsoft SQL SERVER Database To Put silver_customers_Dim Table in Staging Database

# In[33]:


# write data in database
silver_stores.to_sql("silver_stores_Dim",engine,index=False)


# # =================================================

# # 3 - Currency Dimension >> From Exchange Rate Table

# In[89]:


query2 = ''' select * from bronze_exchange_rates'''


# In[90]:


silver_currency = pd.read_sql(query2,conn)
silver_currency.head()


# In[91]:


silver_currency = silver_currency[["Currency"]].drop_duplicates()
# silver_currency["CurrencyCode"] = silver_currency["Currency"]  # Rename if needed


# In[94]:


print(silver_currency.info())


# In[93]:


silver_currency['Currency'] = silver_currency['Currency'].astype("string")


# # Make Connection To Microsoft SQL SERVER Database To Put silver_currency_Dim Table in Staging Database

# In[13]:


# write data in database
silver_currency.to_sql("silver_currency_Dim",engine,index=False)


# # =================================================

# # 4 - Products Dimension 

# In[68]:


query5 = ''' select * from bronze_products'''


# In[69]:


silver_products = pd.read_sql(query5,conn)
silver_products.head()


# In[20]:


print(silver_products.info())


# In[71]:


# Change Data Types for multiple columns from object to string
cols5 = ["Product Name", "Brand", "Color","Subcategory","Category"]
silver_products[cols5] = silver_products[cols5].astype("string")


# In[72]:


silver_category_dim = silver_products[["CategoryKey", "Category"]].drop_duplicates()
silver_subcategory_dim = silver_products[["SubcategoryKey", "Subcategory", "CategoryKey"]].drop_duplicates()

silver_products_dim = silver_products[[
    "ProductKey", "Product Name", "Brand", "Color",
    "Unit Cost USD", "Unit Price USD", "SubcategoryKey"
]].drop_duplicates()


# In[73]:


silver_category_dim.head()


# In[77]:


print(silver_category_dim.info())


# In[103]:


# write data in database
silver_category_dim.to_sql("silver_category_Dim",engine,index=False)


# In[78]:


silver_subcategory_dim.head()


# In[79]:


print(silver_subcategory_dim.info())


# In[29]:


# write data in database
silver_subcategory_dim.to_sql("silver_subcategory_Dim",engine,index=False)


# In[80]:


silver_products_dim.head()


# In[81]:


print(silver_products_dim.info())


# In[30]:


# write data in database
silver_products_dim.to_sql("silver_products_Dim",engine,index=False)


# # =================================================

# # 5 - Date Dimension

# In[31]:


query7 = ''' select * from bronze_sales'''


# In[32]:


sales_dim = pd.read_sql(query7,conn)
sales_dim.head()


# In[39]:


silver_sales_df = sales_dim


# In[33]:


print(sales_dim.info())


# In[35]:


def build_dim_date(date_series):
    dates = pd.to_datetime(date_series.dropna().unique())
    dim_date = pd.DataFrame({"Date": dates})
    dim_date["DateKey"] = dim_date["Date"].dt.strftime("%Y%m%d").astype(int)
    dim_date["Year"] = dim_date["Date"].dt.year
    dim_date["Month"] = dim_date["Date"].dt.month
    dim_date["Day"] = dim_date["Date"].dt.day
    dim_date["Quarter"] = dim_date["Date"].dt.quarter
    dim_date["Week"] = dim_date["Date"].dt.isocalendar().week
    dim_date["DayOfWeek"] = dim_date["Date"].dt.dayofweek
    return dim_date

# Collect all unique dates from sales + exchange rates
all_dates = pd.concat([
    sales_dim["Order Date"],
    sales_dim["Delivery Date"],
    silver_currency["Date"]
])

dim_date = build_dim_date(all_dates)


# In[36]:


dim_date.head()


# In[37]:


print(dim_date.info())


# In[38]:


# write data in database
dim_date.to_sql("silver_date_Dim",engine,index=False)


# # =================================================
# 

# # 6 - Sales Fact

# In[ ]:





# In[40]:


silver_sales_df.head()


# In[43]:


print(silver_sales_df.info())


# In[42]:


silver_sales_df['Currency Code'] = silver_sales_df['Currency Code'].astype("string")


# In[44]:


# Merge Sales with surrogate keys
fact_sales = silver_sales_df.copy()


# In[45]:


# Merge with DimDate for OrderDate
fact_sales = fact_sales.merge(
    dim_date[["Date", "DateKey"]],
    left_on="Order Date",
    right_on="Date",
    how="left"
).rename(columns={"DateKey": "OrderDateKey"}).drop(columns=["Date"])


# In[46]:


# Merge with DimDate for DeliveryDate
fact_sales = fact_sales.merge(
    dim_date[["Date", "DateKey"]],
    left_on="Delivery Date",
    right_on="Date",
    how="left"
).rename(columns={"DateKey": "DeliveryDateKey"}).drop(columns=["Date"])


# In[67]:


# Merge with Customer
fact_sales = fact_sales.merge(
    silver_customers[["CustomerKey", "CustomerSK"]],
    on="CustomerKey",
    how="left"
)


# In[82]:


# Merge with Product
fact_sales = fact_sales.merge(
    silver_products_dim[["ProductKey"]],
    on="ProductKey",
    how="left"
)


# In[88]:


# Merge with Store
fact_sales = fact_sales.merge(
    silver_stores[["StoreKey"]],
    on="StoreKey",
    how="left"
)


# In[96]:


# Merge with Currency
fact_sales = fact_sales.merge(
    silver_currency[["Currency"]],
    left_on="Currency Code",
    right_on="Currency",
    how="left"
)


# In[99]:


# Calculated measures
fact_sales["ExtendedPriceUSD"] = fact_sales["Quantity"] * silver_products_dim["Unit Price USD"]
fact_sales["ProfitUSD"] = (silver_products_dim["Unit Price USD"] - silver_products_dim["Unit Cost USD"]) * fact_sales["Quantity"]


# In[100]:


fact_sales.head()


# In[101]:


print(fact_sales.info())


# In[102]:


# write data in database
fact_sales.to_sql("silver_sales_Fact",engine,index=False)


# # =================================================

# In[ ]:





# In[ ]:





# In[ ]:




