# 📊 Global Electronics Retailer – Data Engineering & Analytics Project
## Project Description
This project demonstrates the end-to-end design and implementation of a Data Warehouse (DWH) and Business Intelligence (BI) solution for a global electronics retailer. The goal is to integrate raw transactional data into a dimensional model and enable rich business insights through advanced analytics and dashboards.
# 🏗️ Medallion Architecture

We adopted the Medallion Architecture (Bronze → Silver → Gold) to structure our data layers:

## 🔹 Bronze Layer (Raw/Staging):
Stores raw data ingested from multiple sources (SQL Server, CSV files, APIs). Data is loaded with minimal transformations for traceability.

## 🔹 Silver Layer (Cleaned & Standardized):
Applied data cleaning, type standardization, and enrichment in Alteryx/Python. This layer provides reliable, deduplicated, and business-ready data tables.

## 🔹 Gold Layer (Business/Analytics):
Implemented Star Schema dimensional models (FactSales, DimCustomer, DimProduct, DimStore, DimDate, DimCurrency). This layer powers BI dashboards and analytical queries.
# 🚀 Project Workflow

### Data Ingestion → Extract raw data into Bronze layer.

### ETL Transformations → Apply business logic & cleaning into Silver layer.

### Data Warehouse Modeling → Create Gold layer with star schema for analytics.

### Optimization → Use indexes in SQL Server.

### Visualization → Build Power BI dashboards for business insights.

# 🛠️ Tech Stack

### Database: SQL Server (staging & DWH)

### ETL Tools: Alteryx, Python (Pandas, SQLAlchemy)

### Data Modeling: Dimensional modeling (Kimball methodology – Star Schema)

### Architecture: Medallion Architecture (Bronze, Silver, Gold)

### BI & Visualization: Power BI

### Version Control: GitHub
# 📈 Key Features

Automated ETL pipelines from staging → DWH.

Centralized FactSales table linked to dimensions.

Analytical queries for sales trends, profit margins, and customer lifetime value.

Partitioned fact table for performance on large volumes of data.

Power BI dashboards with interactive filters for time, region, product, and currency.

## Data architecture
![Architecture Diagram](https://github.com/ElSayed-Fathi/ElectronicsRetailDWH/blob/main/Docs/Data%20Warehouse%20Architecture.drawio.png)
## Key Components:

#### Python Transformations:
Witness the power of Python as it refines and transforms data within the SQL Server staging area, ensuring data quality and integrity before proceeding to the modeling phase.

#### Workflow with Alteryx:
Explore the Alteryx workflow that efficiently extracts data from CSV files and loads it into SQL Server with minimal transformations, ensuring a smooth transition from source to the staging area.

#### Data Modeling in SQL Server:
Delve into the intricacies of data modeling, where the structure of the data warehouse, including dimension and fact tables, is meticulously crafted for analytical purposes.

#### SQL Analysis for Strategic Insights:
Experience the synergy of SQL Server and Tableau as We leverage queries to uncover valuable insights, enabling informed decision-making in the dynamic e-commerce landscape.



## [1. Source Data](https://github.com/ElSayed-Fathi/Data-Engineering-project-for-E-Commerce/blob/39ad69d2d37099fa41b76d7e503a428064980460/1%20Data%20Sources/README%20(2).md)


## Data Source:
![Data Source](source_data.png)

## [2. ETL Using Python](https://github.com/ElSayed-Fathi/Data-Engineering-project-for-E-Commerce/tree/0ebbe62252ef0016922c4cb9b87696cd8b87dff1/1%20Data%20Sources)

### ETL Using Python:
![ETL Using Python](code_example.PNG)

## [3. Alteryx Workflow ](https://github.com/ElSayed-Fathi/Data-Engineering-project-for-E-Commerce/tree/b23186f3ff775672d3c36ae8d8ae24422dd205e0/2%20Staging%20Layer)

###  Alteryx Workflow :
![Alteryx Workflow](https://github.com/ElSayed-Fathi/Data-Engineering-project-for-E-Commerce/blob/b23186f3ff775672d3c36ae8d8ae24422dd205e0/2%20Staging%20Layer/Full%20Workflow.PNG)

## [4. Data Warehouse Model ](https://github.com/ElSayed-Fathi/Data-Engineering-project-for-E-Commerce/tree/cc7b833140ddde630aa206cfcacba4e7d713dc18/5%20Data%20Warehouse%20Dimensional%20Model%20and%20Code)

###  Data Warehouse Model :
![Data Warehouse Model](Data_Warehouse_Diagram_11_light.png)

## [4. Analysis using SQL](https://github.com/ElSayed-Fathi/Data-Engineering-project-for-E-Commerce/tree/1e6ea70c5581a9dd6c38f746ea4f135d3c794e44/6%20SQL%20Analytical%20Queries)

Example of the analysis:
Question: 

Which Logistic Route Has Heavy Traffic In Our E-Commerce? (Delay Frequency)

```sql
SELECT TOP 10 CONCAT(Sellers.SellerState, ', ', Sellers.SellerCity,' ==>> ', Users.UserState, ', ', Users.UserCity) 'Logistic Route', AVG(SubQuery.MaxDeliveryDelayDays) / 
           COUNT(DISTINCT(OrderItems.OrderID)) AS 'Average Delivery Days Per Order'
FROM (
    SELECT OrderItems.OrderID, MAX(OrderItems.DeliveryDelayDays*1.0) AS MaxDeliveryDelayDays
    FROM OrderItems
	WHERE OrderItems.DeliveryDelayCheck = 'Delayed'
    GROUP BY OrderItems.OrderID
) AS SubQuery
JOIN OrderItems ON SubQuery.OrderID = OrderItems.OrderID
JOIN Users
ON Users.UserID = OrderItems.UserID
JOIN Sellers
ON Sellers.SellerID = OrderItems.SellerID
WHERE OrderItems.DeliveryDelayCheck = 'Delayed'
GROUP BY Sellers.SellerState, Sellers.SellerCity, Users.UserState, Users.UserCity
ORDER BY 'Average Delivery Days Per Order' DESC;
```
## [5. Final Insights](https://github.com/ElSayed-Fathi/Data-Engineering-project-for-E-Commerce/tree/6b65b53ece3c6922144ba7813b2b991c14dde1ea/7%20Data%20Visualization%20Using%20Tableau)

### Dashboard:
![Dashboard](https://github.com/ElSayed-Fathi/Data-Engineering-project-for-E-Commerce/blob/6b65b53ece3c6922144ba7813b2b991c14dde1ea/7%20Data%20Visualization%20Using%20Tableau/Dashboard_1.png)

### Examples Of Useful Insights : 

##### Best Payment Methods 
![Best Payment Methods](https://github.com/ElSayed-Fathi/Data-Engineering-project-for-E-Commerce/blob/6b65b53ece3c6922144ba7813b2b991c14dde1ea/7%20Data%20Visualization%20Using%20Tableau/Best_Payment_Method.png)

##### Total Orders Based On Product Category 
![Total Orders Based On Product Category](https://github.com/ElSayed-Fathi/Data-Engineering-project-for-E-Commerce/blob/91afb2b76442a9e7325dcbc40609e71e5217fa42/7%20Data%20Visualization%20Using%20Tableau/Best_Selling_Category.PNG)

##### Total Orders Based On Year And Quarters  
![Total Orders Based On Year And Quarters](https://github.com/ElSayed-Fathi/Data-Engineering-project-for-E-Commerce/blob/91afb2b76442a9e7325dcbc40609e71e5217fa42/7%20Data%20Visualization%20Using%20Tableau/Total_Order_By_year_and_Quarters.png)



## Conclusion:

This project showcases the integration of Alteryx for efficient ETL processes, Python for meticulous transformations, and SQL Server along with Tableau for insightful analysis. Join me in exploring the intricacies of data engineering, from CSV extraction to strategic insights in the context of an ever-evolving e-commerce industry.
