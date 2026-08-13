import pandas as pd


def add_profit_margin(df):
    df = df.copy()

    df["Profit Margin"] = (
        df["Profit"]
        .div(df["Sales"].replace(0, pd.NA))
    )

    return df


def add_shipping_duration(df):
    df = df.copy()

    df["Shipping Duration"] = (
        df["Ship Date"] - df["Order Date"]
    ).dt.days

    return df


def add_sales_performance_category(df):
    df = df.copy()

    df["Sales Performance Category"] = pd.qcut(
        df["Sales"],
        q=3,
        labels=["Low", "Medium", "High"],
        duplicates="drop"
    )

    return df


def engineer_features(df):
    df = df.copy()

    df = add_profit_margin(df)
    df = add_shipping_duration(df)
    df = add_sales_performance_category(df)

    return df