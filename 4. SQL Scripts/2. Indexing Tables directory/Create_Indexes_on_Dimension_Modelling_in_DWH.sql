/* ==========================
   Dimension: Date
   ========================== */
-- Clustered Primary Key on DateKey

/*CREATE CLUSTERED INDEX CIX_DimDate_DateKey
ON DimDate(DateKey);*/

-- Support queries by Year/Month
CREATE NONCLUSTERED INDEX IX_DimDate_YearMonth
ON DimDate(Year, Month);

----------------------------------------------------------------

/* ==========================
   Dimension: Customer
   ========================== */
-- Surrogate key is unique
/*CREATE UNIQUE CLUSTERED INDEX CIX_DimCustomer_CustomerSK
ON DimCustomer(CustomerSK);*/

-- Business key also unique
CREATE UNIQUE NONCLUSTERED INDEX IX_DimCustomer_CustomerKey
ON DimCustomer(CustomerKey);

-- Attributes: allow duplicates
CREATE NONCLUSTERED INDEX IX_DimCustomer_Country
ON DimCustomer(Country);

CREATE NONCLUSTERED INDEX IX_DimCustomer_State
ON DimCustomer(State);

-------------------------------------------------------------

/* ==========================
   Dimension: Product
   ========================== */
-- Surrogate key is unique
/*CREATE UNIQUE CLUSTERED INDEX CIX_DimProduct_ProductKey
ON DimProduct(ProductKey);*/

-- ProductName ideally unique, but depends on business rules
CREATE NONCLUSTERED INDEX IX_DimProduct_ProductName
ON DimProduct(ProductName);

CREATE NONCLUSTERED INDEX IX_DimProduct_Brand
ON DimProduct(Brand);

-- FK to Subcategory for joins
CREATE NONCLUSTERED INDEX IX_DimProduct_SubcategoryKey
ON DimProduct(SubcategoryKey);



/* ==========================
   Dimension: Store
   ========================== */
-- Surrogate key is unique
/*CREATE UNIQUE CLUSTERED INDEX CIX_DimStore_StoreKey
ON DimStore(StoreKey);*/

-- City/Country attributes, duplicates allowed
CREATE NONCLUSTERED INDEX IX_DimStore_Country
ON DimStore(Country);

CREATE NONCLUSTERED INDEX IX_DimStore_City
ON DimStore(State);




/* ==========================
   Dimension: Currency
   ========================== */
-- Each CurrencyCode is unique
/*CREATE UNIQUE CLUSTERED INDEX CIX_DimCurrency_Code
ON DimCurrency(CurrencyCode);*/

-- CurrencyName should be unique too (one-to-one)
CREATE UNIQUE NONCLUSTERED INDEX IX_DimCurrency_Name
ON DimCurrency(CurrencyName);


/* ==========================
   Fact: Sales
   ========================== */


-- Foreign keys → always nonunique (many rows per key)
CREATE NONCLUSTERED INDEX IX_FactSales_OrderDateKey
ON FactSales(OrderDateKey);

CREATE NONCLUSTERED INDEX IX_FactSales_DeliveryDateKey
ON FactSales(DeliveryDateKey);

CREATE NONCLUSTERED INDEX IX_FactSales_CustomerSK
ON FactSales(CustomerSK);

CREATE NONCLUSTERED INDEX IX_FactSales_ProductKey
ON FactSales(ProductKey);

CREATE NONCLUSTERED INDEX IX_FactSales_StoreKey
ON FactSales(StoreKey);

CREATE NONCLUSTERED INDEX IX_FactSales_CurrencyCode
ON FactSales(CurrencyCode);








