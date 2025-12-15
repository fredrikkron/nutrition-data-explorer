import duckdb
import plotly.express as px

con = duckdb.connect("database/näringsportalen.duckdb")

df_vitamin_d = con.execute("SELECT * FROM marts.D_Vitamin").fetch_df()
df_protein_scatter = con.execute("SELECT * FROM marts.protein").fetch_df()
con.close()

def d_vitamin_chart():
    fig = px.scatter(
        df_vitamin_d,
        x='food_name',
        y='Vitamin_D_amount',
        color='food_group',
        labels={"food_name": "Livsmedel", "food_group": "Matgrupp", "Vitamin_D_amount": "D-vitamin (µg/100g)"},
        size='Vitamin_D_amount',
        hover_data=['food_name', 'Vitamin_D_amount', 'food_group']
    )

    fig.update_xaxes(visible=False, showticklabels=False)
    
    fig.add_hline(
        y=10,
        line_dash="dot",
        line_color="green",
        annotation_text="DRI 10 µg",
        annotation_position="top right",
        annotation_font=dict(color="white", size=16)
    )

    fig.update_layout(
        showlegend=False,
        title={
            'text': 'I solens frånvaro under vintertid skiner dessa produkter lite extra för att ge folket D-vitamin vid de norra breddgraderna',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'family': 'Arial', 'size': 20, 'color': 'white', 'weight': 'bold'}
        },
        yaxis_title=""
    )

    return fig

def protein_chart_scatter():
    fig = px.scatter(
        df_protein_scatter,
        x='food_name',
        y='protein_amount',
        color='food_group',
        labels={"food_name": "Livsmedel", "food_group": "Matgrupp", "protein_amount": "Protein (g/100g)"},
        size='protein_amount',
        hover_data=['food_name', 'protein_amount', 'food_group']
    )

    fig.update_xaxes(visible=False, showticklabels=False)
    
    fig.add_hline(
        y=57.27,
        line_dash="dot",
        line_color="red",
        annotation_text="Kvinna 69 kg, DRI 57.27 g",
        annotation_position="top right",
        annotation_font=dict(color="white", size=14)
    )

    fig.add_hline(
        y=69.72,
        line_dash="dot",
        line_color="blue",
        annotation_text="Man 84 kg, DRI 69.72 g",
        annotation_position="top right",
        annotation_font=dict(color="white", size=14)
    )

    fig.update_layout(
        showlegend=False,
        title={
            'text': 'Alternativen för att effektivisera sitt proteinintag finns för många olika dieter och matgrupper',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'family': 'Arial', 'size': 20, 'color': 'white', 'weight': 'bold'}
        },
        yaxis_title=""
    )

    return fig