from pathlib import Path
import duckdb

# Connection to database

con = duckdb.connect("database/näringsportalen.duckdb")

# Path to csv and table name for staging schema in duckdb

data_path = Path(__file__).parents[1] / "data" / "csv_data_livsmedelsverket_melted_2025-10-29.csv"

table_name = "data_Livsmedelsverket"