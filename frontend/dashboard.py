import taipy.gui.builder as tgb
from frontend.KPI import df_KPI_protein, df_KPI_sugar, df_KPI_kcal

with tgb.Page() as dashboard_page:
    with tgb.part(class_name="container-card"):
        tgb.navbar()

        with tgb.part():
            tgb.text("# KPI", mode="md")
            with tgb.layout(class_name="kpi-layout", columns="1 1 1"):
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Minst 10 g protein", mode="md")
                    tgb.text(f"### {len(df_KPI_protein)}", mode="md")
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Minst 30 g socker", mode="md")
                    tgb.text(f"### {len(df_KPI_sugar)}", mode="md")
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Minst 400 kcal", mode="md")
                    tgb.text(f"### {len(df_KPI_kcal)}", mode="md")