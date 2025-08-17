#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pyodbc
import pandas as pd
import os
from sqlalchemy import create_engine
import urllib


# # Begain Of Bronze Layer

# # EDA Of Customer Table And Make Some Transformations

# In[7]:


# Read Customers table
customers_df = pd.read_csv("Data/Customers.csv",encoding="windows-1252")


# In[16]:


customers_df.head()


# In[9]:


print(customers_df.info())


# In[10]:


#(Rows,Columns)
customers_df.shape


# In[11]:


customers_df.describe()


# In[12]:


# Change Data Types for multiple columns from object to string
cols = ["Gender", "Name", "City","State Code","State","Zip Code","Country","Continent"]
customers_df[cols] = customers_df[cols].astype("string")


# In[15]:


print(customers_df.info())


# In[14]:


customers_df['Birthday'] = pd.to_datetime(customers_df['Birthday'])


# # ==========================================================

# # Make Connection To Microsoft SQL SERVER Database To Put Customer Table in Staging Database

# In[3]:


# access destination to write data in database
params = urllib.parse.quote_plus(
r"Driver={ODBC Driver 17 for SQL Server};"
r"server=your_server;"
r"Database=your_desination_database;"
r"Trusted_Connection=yes;"    
)


# In[4]:


engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")


# In[20]:


# write data in database
customers_df.to_sql("customers",engine,index=False)


# # EDA Of Products Table And Make Some Transformations

# In[21]:


# Read Customers table
products_df = pd.read_csv("Data/Products.csv")


# In[29]:


products_df.head()


# In[28]:


print(products_df.info())


# In[24]:


#(Rows,Columns)
products_df.shape


# In[25]:


# Change Data Types for multiple columns from object to string
cols1 = ["Product Name", "Brand", "Color","Subcategory","Category"]
products_df[cols1] = products_df[cols1].astype("string")


# In[27]:


# Remove $ and convert Unit Cost USD ,Unit Price USD  to float
products_df["Unit Cost USD"] = products_df["Unit Cost USD"].replace(r'[\$,]', '', regex=True).astype(float)
products_df["Unit Price USD"] = products_df["Unit Price USD"].replace(r'[\$,]', '', regex=True).astype(float)


# In[31]:


print(products_df.dtypes)


# # Make Connection To Microsoft SQL SERVER Database To Put Product Table in Staging Database

# In[32]:


# access destination to write data in database
params = urllib.parse.quote_plus(
r"Driver={ODBC Driver 17 for SQL Server};"
r"server=your_server;"
r"Database=your_desination_database;"
r"Trusted_Connection=yes;"    
)



# In[33]:


engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")


# In[34]:


# write data in database
products_df.to_sql("products",engine,index=False)


# # ==========================================================

# # EDA Of Stores Table And Make Some Transformations

# In[35]:


# Read Stores table
stores_df = pd.read_csv("Data/Stores.csv")


# In[44]:


stores_df.head()


# In[43]:


print(stores_df.info())


# In[39]:


#(Rows,Columns)
stores_df.shape


# In[40]:


# Change Data Types for multiple columns from object to string
cols2 = ["Country", "State"]
stores_df[cols2] = stores_df[cols2].astype("string")


# In[42]:


stores_df['Open Date'] = pd.to_datetime(stores_df['Open Date'])


# In[45]:


print(stores_df.dtypes)


# # Make Connection To Microsoft SQL SERVER Database To Put Stores Table in Staging Database

# In[46]:


# write data in database
stores_df.to_sql("stores",engine,index=False)


# # ==========================================================

# # EDA Of Data Dictionary Table And Make Some Transformations

# In[48]:


# Read Stores table
Data_Dictionary_df = pd.read_csv("Data/Data_Dictionary.csv")


# In[52]:


# No limit on column width
pd.set_option('display.max_colwidth', None) 


# In[53]:


Data_Dictionary_df.head(100)


# In[55]:


print(Data_Dictionary_df.info())


# In[56]:


# Change Data Types for multiple columns from object to string
cols3 = ["Table", "Field", "Description"]
Data_Dictionary_df[cols3] = Data_Dictionary_df[cols3].astype("string")


# In[57]:


Data_Dictionary_df.to_html("MetaData.html", index=False)


# # ==========================================================

# # EDA Of Exchange Rates Table And Make Some Transformations

# In[58]:


# Read Stores table
Exchange_Rates_df = pd.read_csv("Data/Exchange_Rates.csv")


# In[59]:


Exchange_Rates_df.head()


# In[63]:


print(Exchange_Rates_df.info())


# In[61]:


Exchange_Rates_df.shape


# In[62]:


Exchange_Rates_df['Date'] = pd.to_datetime(Exchange_Rates_df['Date'])
Exchange_Rates_df['Currency'] = Exchange_Rates_df['Currency'].astype("string")


# In[64]:


print(Exchange_Rates_df.dtypes)


# # Make Connection To Microsoft SQL SERVER Database To Put Exchange Rates Table in Staging Database

# In[65]:


# write data in database
Exchange_Rates_df.to_sql("Exchange_Rates",engine,index=False)


# # ==========================================================

# # EDA Of Sales Table And Make Some Transformations

# In[5]:


# Read Stores table
sales_df = pd.read_csv("Data/Sales.csv")


# In[14]:


sales_df.head()


# In[16]:


print(sales_df.info())


# In[8]:


sales_df.shape


# In[12]:


# cols5 = ["Order Date", "Delivery Date"]
# sales_df[cols5] = pd.to_datetime(sales_df[cols5])
cols5 = ["Order Date", "Delivery Date"]

for col in cols5:
    sales_df[col] = pd.to_datetime(sales_df[col], errors="coerce")  # coerce → invalid dates become NaT


# In[15]:


sales_df['Currency Code'] = sales_df['Currency Code'].astype("string")


# # Make Connection To Microsoft SQL SERVER Database To Put Sales Table in Staging Database

# In[17]:


# write data in database
sales_df.to_sql("sales",engine,index=False)


# # ==========================================================

# ## Finish extracting data and load it into staging layer database 
# ### 14/8/2025

# # Ending Of Bronze Layer

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




