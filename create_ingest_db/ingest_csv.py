from constants import con, data_path, table_name

def create_replace_table():
    con.execute(f"""
    CREATE OR REPLACE TABLE staging.{table_name} AS
    SELECT * FROM read_csv_auto('{str(data_path)}', header=True);
    """)
    
    print(f"Data loaded into staging.{table_name}")

    con.close()

if __name__ == "__main__":
    create_replace_table()