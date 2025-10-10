import duckdb
import os

def create_database(db_path="database/näringsportalen.duckdb"):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Connect/create database
    con = duckdb.connect(db_path)

    # Create schemas
    con.execute("CREATE SCHEMA IF NOT EXISTS staging;")
    con.execute("CREATE SCHEMA IF NOT EXISTS warehouse;")
    con.execute("CREATE SCHEMA IF NOT EXISTS marts;")

    # Close connection
    con.close()

if __name__ == "__main__":
    create_database()