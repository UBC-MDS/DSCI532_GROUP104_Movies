import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
# See Docs here: https://dash-bootstrap-components.opensource.faculty.ai
import dash_bootstrap_components as dbc

from codes.plot import make_plot

app = dash.Dash(__name__, assets_folder='assets')
app.config['suppress_callback_exceptions'] = True

server = app.server
app.title = 'Dash app with pure Altair HTML'


movie_df = pd.read_csv('data/clean/movies_clean_df.csv', index_col=0)
genres = movie_df.Major_Genre.unique()
directors = movie_df.Director.unique()

jumbotron = dbc.Jumbotron([
    dbc.Container([
        html.Div(
            [html.H1("Welcome to the Directors Production Tracker App",
                     style={
                         'textAlign': 'Left',
                         'color': '#0f3c63',
                         'width': '1000px',
                         'margin-top': '0px',
                         'margin-bottom': '10px',
                         'margin-right': '0px',
                         'margin-left': '0px',
                         'font-family': 'sans-serif',
                         'font-size': '25px',
                         'line-height': '20px'
                     }),
                html.P(
                    "This app is for you to explore different directors based on the number of movies they produce in a genre to find your director for your next movie.",
                    style={
                        'textAlign': 'Left',
                        'color': '#0f3c63',
                        'width': '1000px',
                        'margin-top': '0px',
                        'margin-bottom': '10px',
                        'margin-right': '0px',
                        'margin-left': '0px',
                        'font-family': 'sans-serif',
                        'font-size': '15px',
                        'line-height': '30px'
                    }
            )],
            style={
                'background-color': '#f2f8fd',
                'margin-top': '0px',
                'margin-bottom': '10px',
                'margin-right': '0px',
                'margin-left': '0px',
                'height': '30px',
                'padding': '30px'

            }

        )
    ],
        fluid=True,
    )
],
    fluid=True,
)

content1 = dbc.Container([
    html.Div(
        html.P('Select a genre'),
        style={
            'height': '30px',
            'width': 'fit-content',
            'float': 'left',
            'margin-left': '30px',
            'margin-right': '10px',
            'color': '#0f3c63',
            'font-family': 'sans-serif',
        }
    ),
    html.Div(
        dcc.Dropdown(
            id='genre',
            options=[{'label': i, 'value': i} for i in genres],
            value='Action',
            style=dict(width='100%', verticalAlign="middle"),
            multi=False,
            searchable=True
        ),
        style={
            'height': '30px',
            'width': '160px',
            'float': 'left',
        }
    ),
    html.Div(
        html.P(
            'and click on the bar chart to choose a director to explore. Press "shift" for multiple selections.'),
        style={
            'height': '30px',
            'float': 'left',
            'width': 'fit-content',
            'margin-left': '30px',
            'color': '#0f3c63',
            'font-family': 'sans-serif',
            # 'border': '1px solid blue'
        }
    ),
    html.Div(
        html.P(
            'Hover over a point in the "IMDB Rating" and "Worldwide Profit" plots to see the attributes of the movie.'),
        style={
            'height': '30px',
            'float': 'left',
            'width': 'fit-content',
            'margin-left': '30px',
            'color': '#0f3c63',
            'font-family': 'sans-serif',
            # 'border': '1px solid blue'
        }
    )

])


content = dbc.Container([
    html.Div(
        html.Iframe(
            sandbox='allow-scripts',
            id='plot1',
            height='800',
            width='1200',
            style={'border-width': '0'},
            # The magic happens here
            srcDoc=make_plot(movie_df).to_html()
            # The magic happens here
        ),
        style={
            'height': 'fit-content',
            'float': 'left',
            'width': 'fit-content',
            'margin-left': '30px',
            'margin-bottom': '0px',
            # 'border': '1px solid blue'
        }
    )
])

footer = dbc.Container(
    html.Div(
        html.P(
            'This Dash app was made collaboratively by the DSCI 532 class in 2019/20!'),
        style={
            'height': '30px',
            'float': 'left',
            'width': 'fit-content',
            'margin-left': '30px',
            'margin-bottom': '30px',
            'color': '#0f3c63',
            'font-family': 'sans-serif',
            # 'border': '1px solid blue'
        }
    )
)

app.layout = html.Div([jumbotron,
                       content1,
                       content,
                       footer

                       ])


@app.callback(
    dash.dependencies.Output('plot1', 'srcDoc'),
    [dash.dependencies.Input('genre', 'value')])
def update_plot(genre_value):
    """
    Takes in the genre and director and calls make_plot to update the plot
    """
    updated_chart = make_plot(movie_df, genre_value).to_html()
    return updated_chart


if __name__ == '__main__':
    app.run_server(debug=True)