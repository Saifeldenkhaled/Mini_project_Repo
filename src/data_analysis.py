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


# 4. Monthly Sales
def monthly_sales(df):
    monthly = (
        df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
        .sum()
    )

    monthly.index = monthly.index.strftime("%b %Y")

    return monthly


# 5. Monthly Profit
def monthly_profit(df):
    monthly = (
        df.groupby(df["Order Date"].dt.to_period("M"))["Profit"]
        .sum()
    )

    monthly.index = monthly.index.strftime("%b %Y")

    return monthly


# 6. Discount vs Profit
def discount_vs_profit(df):
    return df[["Discount", "Profit"]]


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
        "monthly_sales": monthly_sales(df),
        "monthly_profit": monthly_profit(df),
        "discount_vs_profit": discount_vs_profit(df),
        "profit_distribution_by_category": profit_distribution_by_category(df),
        "profit_by_region_category": profit_by_region_category(df)
    }

    return analysis