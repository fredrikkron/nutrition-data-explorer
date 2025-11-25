from pathlib import Path
from api_functions import create_dataframe


def csv_creation():
    df = create_dataframe()

    data_path = Path(__file__).parents[1] / "data" / "data_livsmedelsverket.csv"

    df.to_csv(data_path, index=False)   

if __name__ == "__main__":
    csv_creation()