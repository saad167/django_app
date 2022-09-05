import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px
from region.models import Region
from dash import Dash, html, dcc
from django_plotly_dash import DjangoDash 
from dash.dependencies import Input, Output


def plotly_plot(activity):
    """
    This function plots plotly plot
    """

    rows = Region.objects.all().values_list("year","population","nb_lits_touristiques","chomage",
    "activity","nb_medecin","nuitees_touristiques", "nb_eleves_primaire","nb_eleves_college","nb_eleves_lycee")
    
    table= [list(row) for row in rows]


    data = pd.DataFrame(table,columns = ["year","population","nb_lits_touristiques","chomage",
    "activity","nb_medecin","nuitees_touristiques", "nb_eleves_primaire","nb_eleves_college","nb_eleves_lycee"])



    fig1 = px.bar(data,x="year", y=activity, barmode="group")

    #Update layout for graph object Figure
    fig1.update_layout(title_text = 'Taux de '+str(activity),
                    xaxis_title = 'Années',
                    yaxis_title = 'taux de '+str(activity),
                    plot_bgcolor='#363b56',
                    font_color='#FFFFFF',
                    paper_bgcolor='#464C68',
                    legend=dict(
                    bgcolor='#363b56',
                    bordercolor='#363b56'
        ))
    #Turn graph object into local plotly graph
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=data["year"], y=data[str(activity)],
                    mode='lines+markers', line_color="orange"))
    fig2.update_layout(
        title="Variation du pourcentage du taux "+ str(activity) +" entre 2013 et 2020",
        plot_bgcolor='#363b56',
        font_color='#FFFFFF',
        paper_bgcolor='#464C68',
        legend=dict(
            bgcolor='#363b56',
            bordercolor='#363b56'
        ))

    return     plot({"data":fig1}, output_type='div') ,plot({"data":fig2}, output_type='div') 

