import duckdb
import plotly.express as px

con = duckdb.connect("database/näringsportalen.duckdb")

df_protein = con.execute("SELECT * FROM marts.chart_protein_comparison").fetchdf()
df_vitamin_d = con.execute("SELECT * FROM marts.D_Vitamin").fetch_df()
df_protein_scatter = con.execute("SELECT * FROM marts.protein").fetch_df()
con.close()

def protein_chart():
    fig = px.bar(
        df_protein,
        x='avg_protein',
        y='food_group',
        color='food_group',
        labels={'food_group': 'Kategori', 'avg_protein': 'Protein (g/100g)'},
    )

    fig.update_traces(
        hovertemplate='<b>%{y}</b><br>Protein: %{x:.1f} g<extra></extra>',
        marker_color='steelblue'
    )

    fig.update_yaxes(
        automargin=True
    )

    fig.update_layout(
        showlegend=False,
        title={
            'text': 'Livsmedel inom många olika kategorier är bra proteinkällor för en varierad kost',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'family': 'Arial', 'size': 20, 'color': 'white', 'weight': 'bold'}
        },
        xaxis_title={
            'text': 'Genomsnittligt protein (g/100g)',
            'font': {'family': 'Arial', 'size': 16, 'color': 'white', 'weight': 'bold'}
        },
        annotations=[
            dict(
                x=-0.065,
                y=1.1,
                xref='paper',
                yref='paper',
                text='Kategori',
                showarrow=False,
                font=dict(size=16, color='white', family='Arial', weight='bold'),
                textangle=0
            )
        ],
        yaxis_title= '',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    return fig

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
