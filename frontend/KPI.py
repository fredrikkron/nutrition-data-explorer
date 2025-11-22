import duckdb

con = duckdb.connect("database/näringsportalen.duckdb")

df_KPI_protein = con.execute("""
    SELECT
        *
    FROM
        marts.KPI_Protein
    """).fetchdf()

df_KPI_sugar = con.execute("""
    SELECT
        *
    FROM
        marts.KPI_Sugar
    """).fetchdf()

df_KPI_kcal = con.execute("""
    SELECT
        *
    FROM
        marts.KPI_Kcal
    """).fetchdf()

con.close()