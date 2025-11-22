import duckdb

DB_PATH = "database/näringsportalen.duckdb"

def connect_to_db():
    return duckdb.connect(DB_PATH)