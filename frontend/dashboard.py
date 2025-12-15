import taipy.gui.builder as tgb
from frontend.constants import connect_to_db
from frontend.KPI import df_KPI_total
from frontend.charts import d_vitamin_chart, protein_chart_scatter

con = connect_to_db()
df_protein = con.execute("SELECT * FROM marts.chart_protein_comparison").fetchdf()
con.close()

# KPI
products, groups, nutrients = df_KPI_total.iloc[0]

# charts
fig_D_vitamin = d_vitamin_chart()
fig_protein_scatter = protein_chart_scatter()

# State variables
selected_product = None
protein_value = ""
fat_value = ""
carbs_value = ""
fibre_value = ""
kcal_value = ""

def load_protein(state):
    if not state.selected_product:
        state.protein_value = ""
        state.fat_value = ""
        state.carbs_value = ""
        state.fibre_value = ""
        state.kcal_value = ""
        return

    query = f"""
        SELECT value, unit
        FROM marts.filtering
        WHERE food_name = '{state.selected_product}' AND nutrient_name IN (
            'Protein',
            'Fett, totalt',
            'Kolhydrater, tillgängliga',
            'Fibrer',
            'Energi (kcal)'
        )
        ORDER BY nutrient_name
    """
    con = connect_to_db()
    df = con.execute(query).fetchdf()
    print(df)
    con.close()

    if not df.empty:
        state.protein_value = f"{df['value'].iloc[4]} {df['unit'].iloc[4]}"
        state.carbs_value = f"{df['value'].iloc[3]} {df['unit'].iloc[3]}"
        state.fibre_value = f"{df['value'].iloc[2]} {df['unit'].iloc[2]}"
        state.fat_value = f"{df['value'].iloc[1]} {df['unit'].iloc[1]}"
        state.kcal_value = f"{df['value'].iloc[0]:.0f} {df['unit'].iloc[0]}"


con = connect_to_db()
product_list = con.execute("SELECT DISTINCT food_name FROM marts.filtering ORDER BY food_name").fetchdf()['food_name'].tolist()
con.close()


with tgb.Page() as dashboard_page:
    with tgb.part(class_name="container-card"):
        tgb.navbar()

    with tgb.part(class_name="dashboard-container"):
        tgb.text("# KPI", mode="md")                                # KPI
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

        with tgb.part(class_name="dashboard-container"):
            tgb.selector(
                value="{selected_product}",
                lov="{product_list}",
                on_change=load_protein,
                label="Välj livsmedel",
                dropdown=True)
            with tgb.layout(class_name="kpi-layout", columns="1 1 1"):            # filtering
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Protein", mode="md")
                    tgb.text("### {protein_value}", mode="md") 
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Fett", mode="md")
                    tgb.text("### {fat_value}", mode="md") 
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Kolhydrater", mode="md")
                    tgb.text("### {carbs_value}", mode="md") 
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Fibrer", mode="md")
                    tgb.text("### {fibre_value}", mode="md") 
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Kalorier", mode="md")
                    tgb.text("### {kcal_value}", mode="md") 

            tgb.chart(figure="{fig_D_vitamin}")                     # D-vitamin scatter (Lägga till en linje vid 10 för RDI)
        with tgb.part():
            tgb.chart(figure="{fig_protein_scatter}")               # Protein scatter
        with tgb.part():
            tgb.text(
            "### Nedan visas en rekommendationstabell med dagliga referensvärden för vuxna (18–70 år),\n"
            "### baserad på Livsmedelsverkets näringsrekommendationer.\n"
            "*Värdena är avsedda som vägledning och används som referens vid jämförelse av livsmedel.*",
            mode="md"
        )
            tgb.image("/assets/DRI_table.png", width="100%")
        with tgb.part():
            tgb.text("Datakälla: Livsmedelsverkets Livsmedelsdatabas version 2025-10-29.")