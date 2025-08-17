
/* ==========================
  1. Total Sales & Profit by Year
   ========================== */

SELECT 
    d.Year,
    SUM(f.ExtendedPriceUS) AS TotalSalesUSD,
    SUM(f.ProfitUSD) AS TotalProfitUSD
FROM FactSales f
JOIN DimDate d ON f.OrderDateKey = d.DateKey
GROUP BY d.Year
ORDER BY d.Year;
--==============================================================
/* ==========================
  2. Top 10 Products by Revenue
   ========================== */

SELECT TOP 10
    p.ProductKey,
    p.ProductName,
    SUM(f.ExtendedPriceUS) AS RevenueUSD
FROM FactSales f
JOIN DimProduct p ON f.ProductKey = p.ProductKey
GROUP BY p.ProductKey, p.ProductName
ORDER BY RevenueUSD DESC;

--==============================================================

/* ==========================
  3. Sales by Country and Year where Year = 2016 
   ========================== */
SELECT 
    c.Country,
    d.Year,
    SUM(f.ExtendedPriceUS) AS SalesUSD
FROM FactSales f
JOIN DimCustomer c ON f.CustomerSK = c.CustomerSK
JOIN DimDate d ON f.OrderDateKey = d.DateKey
WHERE d.Year = 2016
GROUP BY c.Country, d.Year
ORDER BY c.Country, d.Year;

--==============================================================
/* ==========================
  4. Profit Margin by Store_Country 
   ========================== */

SELECT 
    s.Country AS Store_Country,
    SUM(f.ExtendedPriceUS) AS RevenueUSD,
    SUM(f.ProfitUSD) AS ProfitUSD,
    (SUM(f.ProfitUSD) * 1.0 / NULLIF(SUM(f.ExtendedPriceUS), 0)) AS ProfitMargin
FROM FactSales f
JOIN DimStore s ON f.StoreKey = s.StoreKey
GROUP BY s.Country
ORDER BY ProfitMargin DESC;
--==============================================================

/* ==========================
  5. Monthly Sales Trend
   ========================== */
SELECT 
    d.Year,
    d.Month,
	DATENAME(MONTH, d.Date) AS MonthName,
    SUM(f.ExtendedPriceUS) AS MonthlySalesUSD
FROM FactSales f
JOIN DimDate d ON f.OrderDateKey = d.DateKey
WHERE d.Year = 2016
GROUP BY d.Year, d.Month, DATENAME(MONTH, d.Date)
ORDER BY d.Year, d.Month;

--=====================================================================

/* ==========================
  7. Customer Lifetime Value (CLV)
   ========================== */
   /*CLV measures the total revenue or profit a company 
   expects to earn from a customer over the entire duration of their relationship.*/
SELECT 
    c.CustomerSK,
    c.Name,
    SUM(f.ExtendedPriceUS) AS TotalSpent,
    SUM(f.ProfitUSD) AS TotalProfit
FROM FactSales f
JOIN DimCustomer c ON f.CustomerSK = c.CustomerSK
GROUP BY c.CustomerSK, c.Name
ORDER BY TotalSpent DESC;

--==================================================================
SELECT 
    s.Country,
    
    SUM(f.ExtendedPriceUS) AS Revenue,
    RANK() OVER (PARTITION BY s.Country ORDER BY SUM(f.ExtendedPriceUS) DESC) AS StoreRank
FROM FactSales f
JOIN DimStore s ON f.StoreKey = s.StoreKey
GROUP BY s.Country
ORDER BY s.Country, StoreRank;


