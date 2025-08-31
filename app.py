from dash import Dash, dcc, html
import pandas as pd
import plotly.graph_objs as go

# Example sales data; replace with your actual dataset
data = {
    'Date': [
        '2020-12-15', '2020-12-22', '2020-12-29', '2021-01-05', '2021-01-12',
        '2021-01-19', '2021-01-26', '2021-02-02', '2021-02-09'
    ],
    'Pink Morsel Sales': [130, 125, 128, 124, 127, 119, 117, 120, 118]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsels Sales Visualizer"),  # Header
    dcc.Graph(
        id='sales-line-chart',
        figure={
            'data': [go.Scatter(
                x=df['Date'],
                y=df['Pink Morsel Sales'],
                mode='lines+markers',
                name='Sales'
            )],
            'layout': go.Layout(
                title='Pink Morsels Sales Over Time',
                xaxis={'title': 'Date'},
                yaxis={'title': 'Sales Count'},
                shapes=[{
                    'type': 'line',
                    'x0': '2021-01-15',
                    'y0': min(df['Pink Morsel Sales']),
                    'x1': '2021-01-15',
                    'y1': max(df['Pink Morsel Sales']),
                    'line': {
                        'color': 'red',
                        'width': 2,
                        'dash': 'dash'
                    }
                }],
                annotations=[{
                    'x': '2021-01-15',
                    'y': max(df['Pink Morsel Sales']),
                    'xref': 'x',
                    'yref': 'y',
                    'text': 'Price Increase',
                    'showarrow': True,
                    'arrowhead': 2,
                    'ax': -20,
                    'ay': -40
                }]
            )
        }
    )
])

if __name__ == '__main__':
    app.run(debug=True)
