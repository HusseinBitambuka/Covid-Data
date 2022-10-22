from dash import Dash, html, dcc,Input,Output
import plotly.express as pt
import pandas as pd
'open the data set'
df=pd.read_csv('Covid Live.csv')
app = Dash(__name__)
app.layout= html.Div(children=[
    html.H1(children='Covid Informaion',style={'textAlign':'center','font-weigh':'bold'}),

    html.Div(children='''
        Countries 
    ''',
    ),
    
    html.Div(
        [
            
             dcc.Dropdown( df.Country,
             id='x-axis',
    value='Burundi',
    clearable=False,),],
    style={'width': '40%', 'display': 'inline-block'},
    ),
    dcc.Graph(id='graph'),
],
)
@app.callback(
    Output('graph','figure'),
    Input('x-axis','value')
)
def display(x_axis):
    dff=df[df.Country==x_axis]
    fig=pt.pie(dff, names='Population',values='Total Cases')
    return fig
if __name__ == '__main__':
    app.run_server(debug=True, port=8080)