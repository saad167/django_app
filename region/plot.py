import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from region.models import Region
from dash import Dash, html, dcc
from django_plotly_dash import DjangoDash 
from dash.dependencies import Input, Output
import dash
import numpy as np


rows = Region.objects.all().values_list("year","population","nb_lits_touristiques","chomage",
    "activity","nb_medecin","nuitees_touristiques", "nb_eleves_primaire","nb_eleves_college","nb_eleves_lycee")


data_value = []

for row in rows :
    row = list(row)
    data_value.append(row)


data = pd.DataFrame(data_value,columns=["year","population","nb_lits_touristiques","chomage",
    "activity","nb_medecin","nuitees_touristiques", "nb_eleves_primaire","nb_eleves_college","nb_eleves_lycee"])


data.sort_values(by=["year"],inplace=True)


med_par_pop=[list(data["population"].values)[i]/list(data["nb_medecin"].values)[i] for i in range(len(data))]
data["pop_pour_UN_med"]=med_par_pop

years_string = [str(year) for year in data["year"]]
colors = {
    'background': '#0E0E0E'
}

app = DjangoDash('SimpleExample')   # replaces dash.Dash

app.layout = html.Div(style={'backgroundColor': colors['background'],
                            "height": "100%" ,
                        },children=[
    html.Div([
        html.Div([
            html.H1("Panorama économique de la région DAKHLA-OUAD DAHAB", style={'color': '#DE2342','textAlign':'center','font-weight': 'bold'}),
            ],style={'width': '90%', 'display': 'inline-block'}),
        html.Div([
            html.H1("                                                              ")
        ]),
        html.Div([
            html.H1("                                                              ")
        ]),
        html.Div([
            html.H1("                                                              ")
        ]),
        html.Div([
            html.Div([
            
            dcc.Slider(
                id="slider",
                min=np.min(data["year"]),max=np.max(data["year"]),step= 1, value=np.min(data["year"]), marks=None,
            tooltip={"placement": "bottom", "always_visible": True})
            #    id="slider",
            #    min=2016,
            #    max=2020,
            #    value=2016,
                
            #    marks={data.values[i,0]:year_test[i] for i in range(len(year_test))},
            #   included=False)
        ]),
        html.Div([
            html.H1("                                                              ")
        ]),
        html.Div([
            html.H1("                                                              ")
        ]),
        html.Div([
            html.H4("Population :",style={'color':'#90BFDC'})
        ]),
         html.Div([
            html.P(id='pop', style={
                       'textAlign': 'center',
                       'color': 'yellow',
                       'fontSize': 40,
                       'margin-top': '-18px'})
        ]),
        html.Div([
            html.H4("L'éducation : primaire, collège et lycée :",style={'color':'#90BFDC'})
        ]),
        html.Div([
            html.P('Pourcentage des étudiants sous 18 ans', style={
                       'textAlign': 'center',
                       'color': '#F3D51A',
                       'fontSize': 15,
                       'margin-top': '-18px'}),
            html.P(id='etd', style={
                       'textAlign': 'center',
                       'color': '#F3D51A',
                       'fontSize': 25,
                       'margin-top': '-18px'})
        ]),
        html.Div([
            html.P('pourcentge des étudiants du primaire', style={
                       'textAlign': 'center',
                       'color': '#dd1e35',
                       'fontSize': 15,
                       'margin-top': '-18px'}),
            html.P(id='prm', style={
                       'textAlign': 'center',
                       'color': '#dd1e35',
                       'fontSize': 25,
                       'margin-top': '-18px'})
        ]),
        html.Div([
            html.P('pourcentge des étudiants du collége',style={
                       'textAlign': 'center',
                       'color': 'green',
                       'fontSize': 15,
                       'margin-top': '-18px'}), 
            html.P(id='col',style={
                       'textAlign': 'center',
                       'color': 'green',
                       'fontSize': 25,
                       'margin-top': '-18px'})
        ]),
        html.Div([
            html.P('pourcentge des étudiants du lycée',style={
                       'textAlign': 'center',
                       'color': '#e55467',
                       'fontSize': 15,
                       'margin-top': '-18px'}), 
            html.P(id='lyc',style={
                       'textAlign': 'center',
                       'color': '#e55467',
                       'fontSize': 25,
                       'margin-top': '-18px'})
        ]),
        html.Div([
            html.H4("La relation entre le nombre des médecins et la population :",style={'color':'#90BFDC'})
        ]),
        html.Div([
            html.P('population pour un médecin',style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 15,
                       'margin-top': '-18px'}), 
            html.P(id='med',style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 25,
                       'margin-top': '-18px'})
        ]),
        html.Div([
        html.Div([
            dcc.RadioItems(
                id="radio_1",
                options=[{'label':i, 'value':i} for i in ["chomage","activity"]],
                value="chomage",
                style={'color': 'white',
                       'fontSize': 23},
                labelStyle={"display":"inline-block"})
        ]),
        html.Div([dcc.Graph(id="chomage")])
    ]),
    html.Div([
        html.Div([
            dcc.RadioItems(
                id="radio_2",
                options=[{'label':i, 'value':i} for i in ["nb_lits_touristiques","nuitees_touristiques"]],
                value="nuitees_touristiques",
                style={'color': 'white',
                       'fontSize': 23},
                labelStyle={"display":"inline-block"})
        ]),
        html.Div([dcc.Graph(id="tourisme")])
        ])
    ])
    ])
])
@app.callback(
    Output('pop', 'children'),
    Input('slider', 'value'))
def pop(year):
    a=list(list(data.loc[data["year"]==int(year)].values)[0])[1] # + 2013
    p=str(int(a))
    popul=p[:3]+"."+p[3:]
    return popul+ "  habitants"
@app.callback(
    Output('etd', 'children'),
    Input('slider', 'value'))
def etudiant(year):
    a=list(list(data.loc[data["year"]==int(year)].values)[0])[7]+list(list(data.loc[data["year"]==int(year)].values)[0])[8]+list(list(data.loc[data["year"]==int(year)].values)[0])[9]
    b=a/list(list(data.loc[data["year"]==int(year)].values)[0])[1]*100
    s=str(round(b,2))+"%"
    return s

@app.callback(
    Output('prm', 'children'),
    Input('slider', 'value'))
def prim(year):
    a_list=list(list(data.loc[data["year"]==int(year)].values)[0])
    a=a_list[7]+a_list[8]+a_list[9]
    b=(a_list[7]/a)*100
    s=str(round(b,2))+"%"
    return s

@app.callback(
    Output('col', 'children'),
    Input('slider', 'value'))
def col(year):
    a_list=list(list(data.loc[data["year"]==int(year)].values)[0])
    a=a_list[7]+a_list[8]+a_list[9]
    b=(a_list[8]/a)*100
    s=str(round(b,2))+"%"
    return s

@app.callback(
    Output('lyc', 'children'),
    Input('slider', 'value'))
def lyc(year):
    a_list=list(list(data.loc[data["year"]==int(year)].values)[0])
    a=a_list[7]+a_list[8]+a_list[9]
    b=(a_list[9]/a)*100
    s=str(round(b,2))+"%"
    return s


@app.callback(
    Output('med', 'children'),
    Input('slider', 'value'))
def med(year):
    a=list(list(data.loc[data["year"]==int(year)].values)[0])[10]
    return int(a)

@app.callback(
    Output("chomage",'figure'),
    Input("radio_1","value")
)
def update_graph_chomage(input_value):
    if input_value=="chomage":
        input_radio="chomage"
    else:
        input_radio="activity"
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["year"], y=data[input_radio],
                    mode='lines+markers', line_color="orange",
                    name=input_value))
    fig.update_layout(
           xaxis = dict(dtick = 1),
        title="Variation du pourcentage du "+input_value+" entre "+str(np.min(data["year"]))+" et "+str(np.max(data["year"])),
        plot_bgcolor='#0E0E0E',
        font_color='#FFFFFF',
        paper_bgcolor='#0E0E0E',
        legend=dict(
            bgcolor='#363b56',
            bordercolor='#363b56'
        ))
    return fig

@app.callback(
    Output("tourisme",'figure'),
    Input("radio_2","value")
)
def update_graph_touris(input_value):
    if input_value=="nuitees_touristiques": #"nb_lits_touristiques","nuitees_touristiques"
        input_radio="nuitees_touristiques"
    else:
        input_radio="nb_lits_touristiques"
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data["year"], y=data[input_radio],marker_color='yellow',name=input_value))
    fig.update_layout(
        title="Variation du pourcentage du "+input_value+" entre "+str(np.min(data["year"]))+" et "+str(np.max(data["year"])),
        plot_bgcolor='#0E0E0E',
        font_color='#FFFFFF',
        paper_bgcolor='#0E0E0E',
        legend=dict(
            bgcolor='#363b56',
            bordercolor='#363b56'
        ))
    return fig




