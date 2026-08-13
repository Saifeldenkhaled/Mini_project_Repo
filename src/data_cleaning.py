import pandas as pd



# 1. DATA LOADING

def load_data(file_path):
    """
    Load an Excel dataset using Pandas.
    """

    try:
        df = pd.read_excel(file_path)
        print("Dataset loaded successfully.")
        return df

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

    except ValueError as e:
        print(f"Invalid Excel file or format: {e}")
        return None

    except Exception as e:
        print(f"Error while loading the dataset: {e}")
        return None

# 2. DATA INSPECTION


def inspect_structure(df):

    print("Dataset Shape:", df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)


def inspect_missing_values(df):
    missing_summary = (
        df.isnull()
        .sum()
        .loc[lambda x: x > 0]
        .sort_values(ascending=False)
        .to_frame("Missing Count")
    )

    return missing_summary


def inspect_duplicates(df):
    
    duplicate_count = df.duplicated().sum()

    return duplicate_count


def inspect_memory_usage(df):
   
    memory_usage = (
        df.memory_usage(deep=True)
        .sort_values(ascending=False)
        .to_frame("Memory Usage (bytes)")
    )

    return memory_usage


def inspect_unique_values(df):
    
    unique_summary = (
        df.nunique()
        .sort_values()
        .to_frame("Unique Values")
    )

    return unique_summary


def inspect_numerical_summary(df):
   
    numerical_summary = df.describe().T

    return numerical_summary



###############################
 # Data Cleaning
###############################

# 2. MISSING VALUES

def handle_missing_values(df):

    df = df.copy()

    if "Postal Code" in df.columns:
        df["Postal Code"] = df["Postal Code"].astype("Int64")

    return df


# 3. DUPLICATES

def remove_duplicates(df):
  
    df = df.copy()

    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        df = df.drop_duplicates().reset_index(drop=True)
        print(f"Removed {duplicate_count} duplicate records.")
    else:
        print("No duplicate records found.")

    return df


# 4. DATA TYPE OPTIMIZATION

def optimize_data_types(df):

    df = df.copy()

    # Integer columns
    integer_columns = [
        "Row ID",
        "Quantity"
    ]

    for column in integer_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                downcast="integer"
            )

    # Float columns
    float_columns = [
        "Sales",
        "Discount",
        "Profit"
    ]

    for column in float_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                downcast="float"
            )

    # Categorical columns
    categorical_columns = [
        "Ship Mode",
        "Segment",
        "Country/Region",
        "Region",
        "Category",
        "Sub-Category"
    ]

    for column in categorical_columns:
        if column in df.columns:
            df[column] = df[column].astype("category")

    return df


# 5. INCONSISTENT VALUES


def clean_inconsistent_values(df):
   
    df = df.copy()

    text_columns = df.select_dtypes(include=["object"]).columns

    for column in text_columns:
        df[column] = df[column].str.strip()

    return df



# 6. OUTLIER DETECTION

def detect_outliers_iqr(df, columns=None):

    if columns is None:
        columns = df.select_dtypes(
            include=["number"]
        ).columns.tolist()

    outlier_summary = []

    for column in columns:

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = (
            (df[column] < lower_bound)
            | (df[column] > upper_bound)
        )

        outlier_summary.append({
            "Column": column,
            "Q1": q1,
            "Q3": q3,
            "IQR": iqr,
            "Lower Bound": lower_bound,
            "Upper Bound": upper_bound,
            "Outlier Count": outliers.sum()
        })

    return pd.DataFrame(outlier_summary)



# 7. DATA VALIDATION


def validate_cleaned_data(df):
   
    validation = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum(),
        "Duplicate Records": df.duplicated().sum(),
        "Negative Sales": (df["Sales"] < 0).sum(),
        "Negative Quantity": (df["Quantity"] < 0).sum(),
        "Invalid Discount": (
            (df["Discount"] < 0)
            | (df["Discount"] > 1)
        ).sum()
    }

    return pd.Series(validation)



# 8. MEMORY OPTIMIZATION


def get_memory_usage(df):
   

    memory_usage = df.memory_usage(deep=True).sum()

    return memory_usage / (1024 ** 2)




# 9. COMPLETE CLEANING PIPELINE

def clean_dataset(df):
    
    df = df.copy()

    # Clean text formatting
    df = clean_inconsistent_values(df)

    # Handle missing values
    df = handle_missing_values(df)

    # Remove duplicates
    df = remove_duplicates(df)

    # Optimize data types
    df = optimize_data_types(df)

    return df