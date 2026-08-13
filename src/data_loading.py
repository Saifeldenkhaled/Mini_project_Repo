import pandas as pd


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


    