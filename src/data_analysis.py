import pandas as pd


# 1. Category Performance
def category_performance(df):
    return (
        df.groupby("Category", observed=True)[["Sales", "Profit"]]
        .sum()
        .sort_values("Sales", ascending=False)
    )


# 2. Sub-Category Profitability
def profit_by_subcategory(df):
    return (
        df.groupby("Sub-Category", observed=True)["Profit"]
        .sum()
        .sort_values(ascending=False)
    )


# 3. Regional Sales vs Profit
def regional_performance(df):
    return (
        df.groupby("Region", observed=True)[["Sales", "Profit"]]
        .sum()
        .sort_values("Sales", ascending=False)
    )


# 4. City Performance
def city_performance(df):
    return (
        df.groupby("City")[["Sales", "Profit"]]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
    )


# 5. Discount vs Profit Margin
def discount_vs_profit_margin(df):
    return df[["Discount", "Profit Margin"]]


# 6. Sales Seasonality
def sales_seasonality(df):
    monthly = (
        df.groupby(df["Order Date"].dt.month)["Sales"]
        .sum()
        .sort_index()
    )

    monthly.index = pd.to_datetime(
    monthly.index,
    format="%m"
).strftime("%B")

    return monthly


# 7. Profit Distribution by Category
def profit_distribution_by_category(df):
    return df[["Category", "Profit"]]


# 8. Region × Category Profitability
def profit_by_region_category(df):
    return pd.pivot_table(
        df,
        values="Profit",
        index="Region",
        columns="Category",
        aggfunc="sum"
    )


# Complete Analysis
def analyze_data(df):

    analysis = {
        "category_performance": category_performance(df),
        "profit_by_subcategory": profit_by_subcategory(df),
        "regional_performance": regional_performance(df),
        "city_performance": city_performance(df),
        "discount_vs_profit_margin": discount_vs_profit_margin(df),
        "sales_seasonality": sales_seasonality(df),
        "profit_distribution_by_category": profit_distribution_by_category(df),
        "profit_by_region_category": profit_by_region_category(df)
    }

    return analysis