--	DDL for Global_Electronics_Retailer_DWH
-- =========================
-- Dimension: Category
-- =========================
CREATE TABLE DimCategory (
    CategoryKey INT PRIMARY KEY,
    Category NVARCHAR(255)
);

--=================================================================================
-- =========================
-- Dimension: Subcategory
-- =========================
CREATE TABLE DimSubcategory (
    SubcategoryKey INT PRIMARY KEY,
    Subcategory NVARCHAR(255),
    CategoryKey INT FOREIGN KEY REFERENCES DimCategory(CategoryKey)
);

--=================================================================================



-- =========================
-- Dimension: Store
-- =========================
CREATE TABLE DimStore (
    StoreKey INT PRIMARY KEY,
    Country NVARCHAR(100),
    State NVARCHAR(100),
    SquareMeters INT,
    OpenDate DATE
);

--=================================================================================

-- =========================
-- Dimension: Product
-- =========================
CREATE TABLE DimProduct (
    ProductKey INT PRIMARY KEY,
    ProductName NVARCHAR(255),
    Brand NVARCHAR(255),
    Color NVARCHAR(50),
    UnitCostUSD DECIMAL(18,2),
    UnitPriceUSD DECIMAL(18,2),
    SubcategoryKey INT FOREIGN KEY REFERENCES DimSubcategory(SubcategoryKey)
);

--=================================================================================


-- =========================
-- Dimension: Date
-- =========================
CREATE TABLE DimDate (
    DateKey INT PRIMARY KEY, -- YYYYMMDD format
    Date DATE NOT NULL,
    Year INT,
    Month INT,
    Day INT,
    Quarter INT,
    Week INT,
    DayOfWeek INT
);

--=================================================================================



-- =========================
-- Dimension: Customer
-- =========================
CREATE TABLE DimCustomer (
    CustomerSK INT PRIMARY KEY,
    CustomerKey INT, -- Natural key from source
    Name NVARCHAR(255),
    Gender NVARCHAR(50),
    Birthday DATE,
    City NVARCHAR(255),
    StateCode NVARCHAR(50),
    State NVARCHAR(255),
    ZipCode NVARCHAR(50),
    Country NVARCHAR(100),
    Continent NVARCHAR(50)
);


--=================================================================================

-- =========================
-- Dimension: Currency
-- =========================
CREATE TABLE DimCurrency (
    CurrencyCode NVARCHAR(10) PRIMARY KEY,
    CurrencyName NVARCHAR(50)
);

--=================================================================================


CREATE TABLE FactSales (
    SalesOrderNumber NVARCHAR(50) NOT NULL,
    SalesLineItem    INT NOT NULL,

    -- FKs
    OrderDateKey     INT NOT NULL FOREIGN KEY REFERENCES DimDate(DateKey),
    DeliveryDateKey  INT NOT NULL FOREIGN KEY REFERENCES DimDate(DateKey),
    CustomerSK       INT NOT NULL FOREIGN KEY REFERENCES DimCustomer(CustomerSK),
    ProductKey       INT NOT NULL FOREIGN KEY REFERENCES DimProduct(ProductKey),
    StoreKey         INT NOT NULL FOREIGN KEY REFERENCES DimStore(StoreKey),
    CurrencyCode     NVARCHAR(10) NOT NULL FOREIGN KEY REFERENCES DimCurrency(CurrencyCode),

    -- Exchange rate at transaction time (to USD)
    ExchangeRateUSD  DECIMAL(18,6) NOT NULL,          -- e.g., 1.000000 for USD

    -- Measures (in USD)
    Quantity         INT NOT NULL,

    -- Derived
    ExtendedPriceUS DECIMAL(18,2) NOT NULL ,
    ProfitUSD       DECIMAL(18,2) NOT NULL  ,

    CONSTRAINT PK_FactSales PRIMARY KEY (SalesOrderNumber, SalesLineItem)
);

--=================================================================================

























--===============================
/**
select
*
from silver_products_Dim
where [Unit Cost USD] is null*/