from pathlib import Path
import duckdb

# Connection to database

con = duckdb.connect("database/näringsportalen.duckdb")

# Path to csv and table name for staging schema in duckdb

data_path = Path(__file__).parents[1] / "data" / "data_livsmedelsverket.csv"

table_name = "data_Livsmedelsverket"