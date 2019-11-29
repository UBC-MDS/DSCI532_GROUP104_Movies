import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import altair as alt
import vega_datasets

# See Docs here: https://dash-bootstrap-components.opensource.faculty.ai
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, assets_folder='assets')
app.config['suppress_callback_exceptions'] = True

server = app.server
app.title = 'Dash app with pure Altair HTML'

movie_df = pd.read_csv(
    'data/clean/movies_clean_df.csv', index_col=0)
genres = movie_df.Major_Genre.unique()
directors = movie_df.Director.unique()


def make_plot(genre='Action'):

    def mds_special():
        font = "Arial"
        axisColor = "#000000"
        gridColor = "#DEDDDD"
        return {
            "config": {
                "title": {
                    "fontSize": 24,
                    "font": font,
                    "anchor": "start",  # equivalent of left-aligned.
                    "fontColor": "#000000"
                },
                'view': {
                    "height": 300,
                    "width": 400
                },
                "axisX": {
                    "domain": True,
                    # "domainColor": axisColor,
                    "gridColor": gridColor,
                    "domainWidth": 1,
                    "grid": False,
                    "labelFont": font,
                    "labelFontSize": 12,
                    "labelAngle": 0,
                    "tickColor": axisColor,
                    "tickSize": 5,  # default, including it just to show you can change it
                    "titleFont": font,
                    "titleFontSize": 16,
                    "titlePadding": 10,  # guessing, not specified in styleguide
                    "title": "X Axis Title (units)",
                },
                "axisY": {
                    "domain": False,
                    "grid": True,
                    "gridColor": gridColor,
                    "gridWidth": 1,
                    "labelFont": font,
                    "labelFontSize": 14,
                    "labelAngle": 0,
                    # "ticks": False, # even if you don't have a "domain" you need to turn these off.
                    "titleFont": font,
                    "titleFontSize": 16,
                    "titlePadding": 10,  # guessing, not specified in styleguide
                    "title": "Y Axis Title (units)",
                    # titles are by default vertical left of axis so we need to hack this
                    # "titleAngle": 0, # horizontal
                    # "titleY": -10, # move it up
                    # "titleX": 18, # move it to the right so it aligns with the labels
                },
            }
        }

    # register the custom theme under a chosen name
    alt.themes.register('mds_special', mds_special)
    # enable the newly registered theme
    alt.themes.enable('mds_special')
    # alt.themes.enable('none') # to return to default

    def get_top_df(genre):
        """
        Finds the number of movies of the most productive directors in the selected genre and 
        movie information from the most productive directors in the selected genre.
        """

        mdfg = movie_df.groupby('Major_Genre')
        top_director = (mdfg.get_group(genre)
                        .groupby('Director')
                        .count()
                        .sort_values(by='Title', ascending=False)
                        .head(30)
                        .reset_index()
                        .iloc[:, :2]
                        .rename(columns={'Title': 'Count'}))
        top_director['Major_Genre'] = genre
        top_df = pd.merge(movie_df,
                          top_director,
                          how="inner",
                          on=['Major_Genre', 'Director'])
        return (top_director, top_df)

    # get information from the 30 most productive directors in the selected genre
    top_director, top_df = get_top_df(genre)

    brush = alt.selection(type='multi', fields=['Director'], init={
                          'Director': top_director.iloc[0, 0]})

    chart_1 = alt.Chart(top_director).mark_bar().encode(
        alt.Y('Director:N',
              title='Director',
              sort=alt.EncodingSortField(field="Count:Q",
                                         order="ascending")),
        alt.X('Count:Q',
              title='Number of movies'),
        opacity=alt.condition(brush, alt.value(0.75), alt.value(0.05)),
    ).properties(
        title='Top 30 most productive directors in ' + genre,
        width=200,
        height=650
    ).add_selection(brush)

    chart_2 = alt.Chart(top_df).mark_line(point=True).encode(
        alt.X("Year:O",
              axis=alt.Axis(title="Year")),
        alt.Y("IMDB_Rating:Q",
              axis=alt.Axis(title="IMDB Rating (1-10)"),
              scale=alt.Scale(zero=False)),
        alt.Color('Director:N'),
        opacity=alt.condition(brush, alt.value(0.75), alt.value(0.01)),
        tooltip=['Title', 'Major_Genre', 'Director', 'IMDB_Rating']
    ).properties(
        title='IMDB Rating',
        width=400,
        height=280
    ).interactive()

    chart_3 = alt.Chart(top_df).mark_line(point=True).encode(
        alt.X("Year:O",
              axis=alt.Axis(title="Year")),
        alt.Y("Profit_Million:Q",
              axis=alt.Axis(title="Profit (M USD)"),
              scale=alt.Scale(zero=False)),
        alt.Color('Director:N'),
        opacity=alt.condition(brush, alt.value(0.75), alt.value(0.01)),
        tooltip=['Title', 'Major_Genre', 'Director', 'IMDB_Rating']
    ).properties(
        title='Worldwide Profit',
        width=400,
        height=280
    ).interactive()

    return chart_1 | (chart_2 & chart_3)


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
            srcDoc=make_plot().to_html()
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
    updated_chart = make_plot(genre_value).to_html()
    return updated_chart


if __name__ == '__main__':
    app.run_server(debug=True)
