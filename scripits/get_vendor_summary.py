import sqlite3
import pandas as pd
import numpy as np  # Imported to easily handle infinity values

conn = sqlite3.connect('inventory.db')

query = """
WITH FreightSummary AS (
    SELECT
        VendorNumber,
        SUM(Freight) AS FreightCost
    FROM vendor_invoice
    GROUP BY VendorNumber
),

PurchaseSummary AS (
    SELECT
        p.VendorNumber,
        p.VendorName,
        p.Brand,
        p.Description,
        p.PurchasePrice,
        pp.Price AS ActualPrice,
        pp.Volume,
        SUM(p.Quantity) AS TotalPurchaseQuantity,
        SUM(p.Dollars) AS TotalPurchaseDollars
    FROM purchases p
    JOIN purchase_prices pp
        ON p.Brand = pp.Brand
    WHERE p.PurchasePrice > 0
    GROUP BY
        p.VendorNumber,
        p.VendorName,
        p.Brand,
        p.Description,
        p.PurchasePrice,
        pp.Price,
        pp.Volume
),

SalesSummary AS (
    SELECT
        VendorNo,
        Brand,
        SUM(SalesQuantity) AS TotalSalesQuantity,
        SUM(SalesDollars) AS TotalSalesDollars,
        SUM(SalesPrice) AS TotalSalesPrice,
        SUM(ExciseTax) AS TotalExciseTax
    FROM sales
    GROUP BY VendorNo, Brand
)

SELECT
    ps.VendorNumber,
    ps.VendorName,
    ps.Brand,
    ps.Description,
    ps.PurchasePrice,
    ps.ActualPrice,
    ps.Volume,
    ps.TotalPurchaseQuantity,
    ps.TotalPurchaseDollars,
    ss.TotalSalesQuantity,
    ss.TotalSalesDollars,
    ss.TotalSalesPrice,
    ss.TotalExciseTax,
    fs.FreightCost
FROM PurchaseSummary ps
LEFT JOIN SalesSummary ss
    ON ps.VendorNumber = ss.VendorNo
    AND ps.Brand = ss.Brand
LEFT JOIN FreightSummary fs
    ON ps.VendorNumber = fs.VendorNumber
ORDER BY ps.TotalPurchaseDollars DESC
"""

df = pd.read_sql_query(query, conn)

# Safer way to convert to float, forcing errors to NaN if any weird strings exist
df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')

# Initial fill for missing values coming from the LEFT JOINs
df.fillna(0, inplace=True)

# Strip whitespace
df['VendorName'] = df['VendorName'].str.strip()
df['Description'] = df['Description'].str.strip()

# Calculations
df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']

df['ProfitMargin'] = (df['GrossProfit'] / df['TotalSalesDollars']).fillna(0) * 100
df['StockTurnover'] = (df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']).fillna(0)
df['SalesToPurchaseRatio'] = (df['TotalSalesDollars'] / df['TotalPurchaseDollars']).fillna(0)

# CRITICAL FIX: Replace infinity values (caused by dividing by 0) with 0
df.replace([np.inf, -np.inf], 0, inplace=True)

print(df.head())

conn.close()
