import duckdb

con = duckdb.connect("database/näringsportalen.duckdb")

df_KPI_total = con.execute("""
    SELECT
        *
    FROM
        marts.KPI
    """).fetchdf()

con.close()