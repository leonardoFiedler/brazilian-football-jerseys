import pandas as pd
from csv import QUOTE_ALL


def column_value_int(
    df: pd.DataFrame, column_name: str, int_column_name: str
) -> pd.DataFrame:
    """Convert column to Int.

    Args:
        df (pd.DataFrame): DataFrame with the column to convert to int
        column_name (str): Original column name
        int_column_name (str): Int column name created

    Returns:
        pd.DataFrame: DataFrame with new column
    """
    df[int_column_name] = df[column_name].apply(lambda x: int(x))
    return df


def create_column_add_percent_value(
    df: pd.DataFrame, column_name: str, percent: int, column_name_percent: str
) -> pd.DataFrame:
    """Create a column adding a percent of a value.

    Args:
        df (pd.DataFrame): DataFrame with column_name
        column_name (str): Original name of the column to calculate percentage
        percent (int): the percentage value (>0)
        column_name_percent (str): name of the generated column

    Returns:
        pd.DataFrame: DataFrame with the new column created
    """
    if percent < 1:
        raise ValueError("Percent must be greater than 0.")

    df[column_name_percent] = df[column_name].apply(
        lambda x: int(int(x) * (1 + percent / 100))
    )
    return df


def create_column_sub_percent_value(
    df: pd.DataFrame, column_name: str, percent: int, column_name_percent: str
) -> pd.DataFrame:
    """Create a column subtracting a percent of a value.

    Args:
        df (pd.DataFrame): DataFrame with column_name
        column_name (str): Original name of the column to calculate percentage
        percent (int): the percentage value (>0)
        column_name_percent (str): name of the generated column

    Returns:
        pd.DataFrame: DataFrame with the new column created
    """
    if percent < 1:
        raise ValueError("Percent must be greater than 0.")

    df[column_name_percent] = df[column_name].apply(
        lambda x: int(int(x) * (1 - percent / 100))
    )
    return df


if __name__ == "__main__":
    INPUT_FILE = "data/raw/brazil-teams-jersey-price.csv"
    INPUT_MIN_WAGE_FILE = "data/processed/minimum_wage_historical.csv"
    OUTPUT_FILE = "data/processed/brazil-teams-jersey-price-processed.csv"

    df = pd.read_csv(INPUT_FILE)

    # Create Int column
    df = column_value_int(df, "value", "value_int")

    # Create values with percent add along the year (5, 10, and 15%)
    df = create_column_add_percent_value(df, "value", 5, "value_add_05")
    df = create_column_add_percent_value(df, "value", 10, "value_add_10")
    df = create_column_add_percent_value(df, "value", 15, "value_add_15")

    # Create value with possible discounts (5, 10, and 15%)
    df = create_column_sub_percent_value(df, "value", 5, "value_sub_05")
    df = create_column_sub_percent_value(df, "value", 10, "value_sub_10")
    df = create_column_sub_percent_value(df, "value", 15, "value_sub_15")

    df.to_csv(
        OUTPUT_FILE,
        index=False,
        quoting=QUOTE_ALL,
        columns=[
            "team",
            "state",
            "year",
            "value",
            "value_int",
            "value_add_05",
            "value_add_10",
            "value_add_15",
            "value_sub_05",
            "value_sub_10",
            "value_sub_15",
            "access_date",
            "source",
        ],
    )
