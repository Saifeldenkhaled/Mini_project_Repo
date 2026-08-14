import matplotlib.pyplot as plt


# 1. Category Performance
def plot_category_performance(data):
    plt.figure(figsize=(9, 6))

    data.plot(kind="bar")

    plt.title("Sales and Profit by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.xticks(rotation=0)

    plt.tight_layout()
    plt.show()


# 2. Sub-Category Profitability
def plot_profit_by_subcategory(data):
    plt.figure(figsize=(10, 7))

    data.sort_values().plot(kind="barh")

    plt.title("Profit by Sub-Category")
    plt.xlabel("Total Profit")
    plt.ylabel("Sub-Category")

    plt.tight_layout()
    plt.show()


# 3. Regional Sales vs Profit
def plot_regional_performance(data):
    plt.figure(figsize=(9, 6))

    plt.scatter(
        data["Sales"],
        data["Profit"]
    )

    for region in data.index:
        plt.annotate(
            region,
            (
                data.loc[region, "Sales"],
                data.loc[region, "Profit"]
            )
        )

    plt.title("Regional Sales vs Profit")
    plt.xlabel("Total Sales")
    plt.ylabel("Total Profit")

    plt.tight_layout()
    plt.show()


# 4. City / State Performance
def plot_city_performance(data):
    plt.figure(figsize=(10, 8))

    data.sort_values("Sales").plot(
        kind="barh",
        figsize=(10, 8)
    )

    plt.title("Sales and Profit by Top 10 Cities")
    plt.xlabel("Amount")
    plt.ylabel("City")

    plt.tight_layout()
    plt.show()


# 5. Discount vs Profit Margin
def plot_discount_vs_profit_margin(data):
    plt.figure(figsize=(9, 6))

    plt.scatter(
        data["Discount"],
        data["Profit Margin"],
        alpha=0.5
    )

    plt.title("Discount vs Profit Margin")
    plt.xlabel("Discount")
    plt.ylabel("Profit Margin")

    plt.tight_layout()
    plt.show()


# 6. Sales Seasonality

def plot_sales_seasonality(data):
    plt.figure(figsize=(12, 6))

    data.plot(kind="bar")

    plt.title("Sales Seasonality by Month Across All Years")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=0)

    plt.tight_layout()
    plt.show()


# 7. Profit Distribution by Category
def plot_profit_distribution(data):
    categories = data["Category"].unique()

    values = [
        data.loc[
            data["Category"] == category,
            "Profit"
        ]
        for category in categories
    ]

    plt.figure(figsize=(9, 6))

    plt.boxplot(
        values,
        tick_labels=categories
    )

    plt.title("Profit Distribution by Category")
    plt.xlabel("Category")
    plt.ylabel("Profit")

    plt.tight_layout()
    plt.show()


# 8. Region × Category Profitability
def plot_profit_by_region_category(data):
    plt.figure(figsize=(10, 6))

    plt.imshow(
        data,
        aspect="auto"
    )

    plt.colorbar(label="Total Profit")

    plt.xticks(
        range(len(data.columns)),
        data.columns
    )

    plt.yticks(
        range(len(data.index)),
        data.index
    )

    plt.title("Profit by Region and Category")
    plt.xlabel("Category")
    plt.ylabel("Region")

    plt.tight_layout()
    plt.show()