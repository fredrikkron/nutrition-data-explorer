from constants import con, data_path, table_name

def create_replace_table():
    try:
        con.execute(f"""
        CREATE OR REPLACE TABLE staging.{table_name} AS
        SELECT * FROM read_csv_auto('{data_path}', header=True);
        """)
    finally:
        con.close()

if __name__ == "__main__":
    create_replace_table()