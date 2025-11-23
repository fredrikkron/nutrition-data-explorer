import duckdb

def carb_table(): 
    con = duckdb.connect("database/näringsportalen.duckdb")
    df_carbs = con.execute("SELECT * FROM marts.carbs_table").fetchdf()
    con.close()

    return df_carbs