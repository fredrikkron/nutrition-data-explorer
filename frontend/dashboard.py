import taipy.gui.builder as tgb
from frontend.constants import connect_to_db
from frontend.KPI import df_KPI_protein, df_KPI_sugar, df_KPI_kcal
from frontend.charts import protein_chart

con = connect_to_db()
df_protein = con.execute("SELECT * FROM marts.chart_protein_comparison").fetchdf()
con.close()

# charts
fig_protein = protein_chart()

with tgb.Page() as dashboard_page:
    with tgb.part(class_name="container-card"):
        tgb.navbar()

    with tgb.part(class_name="dashboard-container"):
        tgb.text("# KPI", mode="md")
        with tgb.layout(class_name="kpi-layout", columns="1 1 1"):
            with tgb.part(class_name="metric-card"):
                tgb.text("### > 10 g protein", mode="md")
                tgb.text(f"### {len(df_KPI_protein)}", mode="md")
            with tgb.part(class_name="metric-card"):
                tgb.text("### > 20 g socker", mode="md")
                tgb.text(f"### {len(df_KPI_sugar)}", mode="md")
            with tgb.part(class_name="metric-card"):
                tgb.text("### > 400 kcal", mode="md")
                tgb.text(f"### {len(df_KPI_kcal)}", mode="md")
        with tgb.part():
            tgb.chart(figure="{fig_protein}")
        