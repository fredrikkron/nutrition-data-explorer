import duckdb
import plotly.express as px

con = duckdb.connect("database/näringsportalen.duckdb")

df_protein = con.execute("SELECT * FROM marts.chart_protein_comparison").fetchdf()
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