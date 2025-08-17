# 📊 Global Electronics Retailer – Data Engineering & Analytics Project
## Project Description
This project demonstrates the end-to-end design and implementation of a Data Warehouse (DWH) and Business Intelligence (BI) solution for a global electronics retailer. The goal is to integrate raw transactional data into a dimensional model and enable rich business insights through advanced analytics and dashboards.
# 🏗️ Medallion Architecture

We adopted the Medallion Architecture (Bronze → Silver → Gold) to structure our data layers:

#### 🔹 Bronze Layer (Raw/Staging):
Stores raw data ingested from multiple sources (SQL Server, CSV files, APIs). Data is loaded with minimal transformations for traceability.

#### 🔹 Silver Layer (Cleaned & Standardized):
Applied data cleaning, type standardization, and enrichment in Alteryx/Python. This layer provides reliable, deduplicated, and business-ready data tables.

#### 🔹 Gold Layer (Business/Analytics):
Implemented Star Schema dimensional models (FactSales, DimCustomer, DimProduct, DimStore, DimDate, DimCurrency). This layer powers BI dashboards and analytical queries.
# 🚀 Project Workflow

Data Ingestion → Extract raw data into Bronze layer.

ETL Transformations → Apply business logic & cleaning into Silver layer.

Data Warehouse Modeling → Create Gold layer with star schema for analytics.

Optimization → Use indexes in SQL Server.

Visualization → Build Power BI dashboards for business insights.

# 🛠️ Tech Stack

Database: SQL Server (staging & DWH)

ETL Tools: Alteryx, Python (Pandas, SQLAlchemy)

Data Modeling: Dimensional modeling (Kimball methodology – Star Schema)

Architecture: Medallion Architecture (Bronze, Silver, Gold)

BI & Visualization: Power BI

Version Control: GitHub

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


## [Alteryx Workflow ](https://github.com/ElSayed-Fathi/ElectronicsRetailDWH/blob/main/2.%20ETL%20Pipeline/WorkFlow.png)

###  Alteryx Workflow :
![Alteryx Workflow](https://github.com/ElSayed-Fathi/ElectronicsRetailDWH/blob/main/2.%20ETL%20Pipeline/WorkFlow.png)

## [Data Warehouse Model ](https://github.com/ElSayed-Fathi/ElectronicsRetailDWH/blob/main/5.%20Power%20BI%20Charts/Data%20Model.png)

###  Data Warehouse Model :
![Data Warehouse Model](https://github.com/ElSayed-Fathi/ElectronicsRetailDWH/blob/main/5.%20Power%20BI%20Charts/Data%20Model.png)

## [Analysis using SQL](https://github.com/ElSayed-Fathi/ElectronicsRetailDWH/blob/main/4.%20SQL%20Scripts/3.%20Analytical%20Queries/SQL_Analytical_Queries_on_Global_Electronics_Retailer_DWH.sql)
Example of the analysis:

Customer Lifetime Value (CLV)

```sql
SELECT 
    c.CustomerSK,
    c.Name,
    SUM(f.ExtendedPriceUS) AS TotalSpent,
    SUM(f.ProfitUSD) AS TotalProfit
FROM FactSales f
JOIN DimCustomer c ON f.CustomerSK = c.CustomerSK
GROUP BY c.CustomerSK, c.Name
ORDER BY TotalSpent DESC;
```
## [Final Insights](https://github.com/ElSayed-Fathi/ElectronicsRetailDWH/blob/main/5.%20Power%20BI%20Charts/Files/dashboard.png)
### Dashboard:
![Dashboard](https://github.com/ElSayed-Fathi/ElectronicsRetailDWH/blob/main/5.%20Power%20BI%20Charts/Files/dashboard.png)
### Examples Of Useful Insights : 

##### profit_margin_by_category 
![Profit_Margin_By_Category](https://github.com/ElSayed-Fathi/ElectronicsRetailDWH/blob/main/5.%20Power%20BI%20Charts/Charts/profit_margin_by_category.png)

##### total profit by category. 
![Total Profit By On Category](https://github.com/ElSayed-Fathi/ElectronicsRetailDWH/blob/main/5.%20Power%20BI%20Charts/Charts/total%20profit%20by%20category.png)

##### total sales by month  
![Total Sales By Month](https://github.com/ElSayed-Fathi/ElectronicsRetailDWH/blob/main/5.%20Power%20BI%20Charts/Charts/total%20sales%20by%20month.png)

## 📂 Repository Structure
```
data-warehouse-project/
│
├── 1. Sourece Data /                   # Raw datasets used for the project
│
├── 2. EtL Pipline /                    # Alteryx Workflow And Containers
│   ├── Alteryx Worflow /               # data from staging layer to DWH_Autosave.yxmd
│   ├── Containters                     # Containers For each pipline to move data
│   ├── WorkFlow.png                    # The Full WorkFolw For The Project
│
├── 3. Python Scripts /                 # Python files to extract and transform data
│   ├── bronze Layer/                   # Bronze Layer From Extracting Data To Load Data in Staging Database
│   ├── silver Layer/                   # Sliver Layer some Transformations and Data Cleansing directory
│
├── 4. SQL Scripts /                    # Contains All SQL Files
│   ├── DDL /                           # Data Defination Language For Create Dimensional Modelling
│   ├── Indexing Tables /               # Create Indexes on Dimension Modelling in DWH For Optimization
│   ├── Analytical Queries /            # SQL Analytical Queries on Global Electronics Retailer DWH
|
├── 5. Power BI Charts /                # Contains All Charts Files
│   ├── Charts /                        # Contain Charts
│   ├── Files /                         # Contain All Files and Dashboard
|
├── Docs /                              # Contains Files included ETL,Data Layers And Data Architecture
|
├── README.md                           # Project overview and instructions
|
└──LICENSE                              # License information for the repository
```

## Conclusion:

This project showcases how raw business data can be transformed into a scalable Data Warehouse using Medallion Architecture and turned into actionable insights for decision-making.
