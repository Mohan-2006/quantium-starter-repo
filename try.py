import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.graph_objs as go

# Example data with region column added (replace with actual region data)
df = pd.read_csv('pink_morsel_sales.csv', parse_dates=['date'])
# Simulated regions column for demo purposes:
regions = ['north', 'east', 'south', 'west']
df['region'] = [regions[i % len(regions)] for i in range(len(df))]


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Soul Foods Sales Visualiser', style={'textAlign': 'center', 'color': '#4CAF50'}),
    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'}
        ],
        value='all',
        labelStyle={'display': 'inline-block', 'margin-right': '15px', 'font-weight': 'bold', 'color': '#555'}
    ),
    dcc.Graph(id='sales-graph'),
    
    # Custom CSS styling for padding and borders
], style={'maxWidth': '700px', 'margin': '40px auto', 'padding': '20px', 'border': '2px solid #4CAF50', 'borderRadius': '10px', 'backgroundColor': '#f9f9f9'})

@app.callback(
    Output('sales-graph', 'figure'),
    [Input('region-filter', 'value')]
)
def update_graph(region):
    if region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == region]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=filtered_df['date'],
        y=filtered_df['sales'],
        mode='lines+markers',
        name=f'Sales ({region.capitalize()})' if region != 'all' else 'Sales (All)'
    ))

    fig.add_shape(
        type="line",
        x0='2021-01-15', x1='2021-01-15',
        y0=filtered_df['sales'].min() if not filtered_df.empty else 0,
        y1=filtered_df['sales'].max() if not filtered_df.empty else 1,
        line=dict(color="red", width=2, dash="dash"),
    )
    fig.add_annotation(
        x='2021-01-15',
        y=filtered_df['sales'].max() if not filtered_df.empty else 1,
        text="Pink Morsel Price Increase",
        showarrow=True,
        arrowhead=2
    )

    fig.update_layout(
        title="Soul Foods Sales Visualiser",
        xaxis_title="Date",
        yaxis_title="Total Sales ($)",
        template='plotly_white'
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)

