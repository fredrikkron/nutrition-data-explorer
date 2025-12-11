import taipy.gui.builder as tgb
from frontend.constants import connect_to_db
from frontend.KPI import df_KPI_total
from frontend.charts import protein_chart, d_vitamin_chart, protein_chart_scatter
from frontend.tables import carb_table

con = connect_to_db()
df_protein = con.execute("SELECT * FROM marts.chart_protein_comparison").fetchdf()
con.close()

# KPI
products, groups, nutrients = df_KPI_total.iloc[0]

# charts
fig_protein = protein_chart()
fig_D_vitamin = d_vitamin_chart()
fig_protein_scatter = protein_chart_scatter()

# tables
df_carbs_table = carb_table()

with tgb.Page() as dashboard_page:
    with tgb.part(class_name="container-card"):
        tgb.navbar()

    with tgb.part(class_name="dashboard-container"):
        tgb.text("# KPI", mode="md")
        with tgb.layout(class_name="kpi-layout", columns="1 1 1"):
            with tgb.part(class_name="metric-card"):
                tgb.text("### Livsmedel", mode="md")
                tgb.text(f"### {products}", mode="md")
            with tgb.part(class_name="metric-card"):
                tgb.text("### Matgrupperingar", mode="md")
                tgb.text(f"### {groups}", mode="md")
            with tgb.part(class_name="metric-card"):
                tgb.text("### Näringsämnen", mode="md")
                tgb.text(f"### {nutrients}", mode="md")
        with tgb.part():
            tgb.chart(figure="{fig_protein}")
        with tgb.part():
            tgb.chart(figure="{fig_D_vitamin}")
        with tgb.part():
            tgb.chart(figure="{fig_protein_scatter}")
        with tgb.part(class_name="df-layout"):
            tgb.table("{df_carbs_table}")