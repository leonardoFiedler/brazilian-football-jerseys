import pandas as pd

INPUT_FILE = "raw/brazil-teams-jersey-price.csv"


def column_value_int(df: pd.DataFrame, column_name="name_int") -> pd.DataFrame:
    df[column_name] = df["value"].apply(lambda x: int(x))
    return df


if __name__ == "__main__":
    df = pd.read_csv(INPUT_FILE)

    df = column_value_int(df)
