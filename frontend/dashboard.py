import taipy.gui.builder as tgb
from frontend.constants import connect_to_db
from frontend.KPI import df_KPI_total
from frontend.charts import d_vitamin_chart, protein_chart_scatter

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
A_value = ""
B12_value = ""
C_value = ""
D_value = ""
E_value = ""
kalcium_value = ""
iron_value = ""
magnesium_value = ""
zinc_value = ""
kalium_value = ""


def load_protein(state):
    if not state.selected_product:
        state.protein_value = ""
        state.fat_value = ""
        state.carbs_value = ""
        state.fibre_value = ""
        state.kcal_value = ""
        state.A_value = ""
        state.B12_value = ""
        state.C_value = ""
        state.D_value = ""
        state.E_value = ""
        state.kalcium_value = ""
        state.iron_value = ""
        state.magnesium_value = ""
        state.zinc_value = ""
        state.kalium_value = ""
        return

    query = f"""
        SELECT value, unit
        FROM marts.filtering
        WHERE food_name = '{state.selected_product}'
        ORDER BY nutrient_name
    """
    con = connect_to_db()
    df = con.execute(query).fetchdf()
    print(df)
    con.close()

    if not df.empty:
        state.kcal_value = f"{df['value'].iloc[0]:.0f} {df['unit'].iloc[0]}"
        state.fat_value = f"{df['value'].iloc[1]} {df['unit'].iloc[1]}"
        state.fibre_value = f"{df['value'].iloc[2]} {df['unit'].iloc[2]}"
        state.iron_value = f"{df['value'].iloc[3]} {df['unit'].iloc[3]}"
        state.kalcium_value = f"{df['value'].iloc[4]:.0f} {df['unit'].iloc[4]}"
        state.kalium_value = f"{df['value'].iloc[5]:.0f} {df['unit'].iloc[5]}"
        state.carbs_value = f"{df['value'].iloc[6]} {df['unit'].iloc[6]}"
        state.magnesium_value = f"{df['value'].iloc[7]:.0f} {df['unit'].iloc[7]}"
        state.protein_value = f"{df['value'].iloc[8]} {df['unit'].iloc[8]}"
        state.A_value = f"{df['value'].iloc[9]} {df['unit'].iloc[9]}"
        state.B12_value = f"{df['value'].iloc[10]} {df['unit'].iloc[10]}"
        state.C_value = f"{df['value'].iloc[11]} {df['unit'].iloc[11]}"
        state.D_value = f"{df['value'].iloc[12]} {df['unit'].iloc[12]}"
        state.E_value = f"{df['value'].iloc[13]} {df['unit'].iloc[13]}"
        state.zinc_value = f"{df['value'].iloc[14]} {df['unit'].iloc[14]}"

con = connect_to_db()
product_list = con.execute("SELECT DISTINCT food_name FROM marts.filtering ORDER BY food_name").fetchdf()['food_name'].tolist()
con.close()


with tgb.Page() as dashboard_page:
    with tgb.part(class_name="header-flex"):
        tgb.image("assets/nutrition_logo.png")
        tgb.text("# Näringsportalen", mode="md")

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
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Vitamin A", mode="md")
                    tgb.text("### {A_value}", mode="md") 
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Vitamin B12", mode="md")
                    tgb.text("### {B12_value}", mode="md") 
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Vitamin C", mode="md")
                    tgb.text("### {C_value}", mode="md") 
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Vitamin D", mode="md")
                    tgb.text("### {D_value}", mode="md") 
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Vitamin E", mode="md")
                    tgb.text("### {E_value}", mode="md") 
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Kalcium", mode="md")
                    tgb.text("### {kalcium_value}", mode="md") 
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Järn", mode="md")
                    tgb.text("### {iron_value}", mode="md") 
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Magnesium", mode="md")
                    tgb.text("### {magnesium_value}", mode="md") 
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Zink", mode="md")
                    tgb.text("### {zinc_value}", mode="md") 
                with tgb.part(class_name="metric-card"):
                    tgb.text("### Kalium", mode="md")
                    tgb.text("### {kalium_value}", mode="md")
            tgb.chart(figure="{fig_D_vitamin}", class_name="chart-bottom-space")       # D-vitamin scatter
        with tgb.part():
            tgb.chart(figure="{fig_protein_scatter}", class_name="chart-bottom-space") # Protein scatter
        with tgb.part():
            tgb.text(
            "### Nedan visas en rekommendationstabell med dagliga referensvärden\n"
            "### baserad på Livsmedelsverkets näringsrekommendationer.\n"
            "*Värdena är avsedda som vägledning och används som referens vid jämförelse av livsmedel.*",
            mode="md"
        )
            tgb.image("/assets/DRI_table.png", width="100%")
        with tgb.part():
            tgb.text("*Datakälla: Livsmedelsverkets Livsmedelsdatabas version 2025-10-29.*", mode="md")