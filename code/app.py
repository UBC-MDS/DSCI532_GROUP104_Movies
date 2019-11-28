import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import sqlalchemy
import altair as alt
import vega_datasets

app = dash.Dash(__name__, assets_folder='assets')
server = app.server
app.title = 'Dash app with pure Altair HTML'

movie_df = pd.read_csv('https://raw.githubusercontent.com/UBC-MDS/DSCI532_GROUP104_Movies/master/data/clean/movies_clean_df.csv', index_col = 0)
genres = movie_df.Major_Genre.unique()
directors = movie_df.Director.unique()

def make_plot(genre = 'Action'):
    # Don't forget to include imports
    def mds_special():
        font = "Arial"
        axisColor = "#000000"
        gridColor = "#DEDDDD"
        return {
            "config": {
                "title": {
                    "fontSize": 24,
                    "font": font,
                    "anchor": "start", # equivalent of left-aligned.
                    "fontColor": "#000000"
                },
                'view': {
                    "height": 300, 
                    "width": 400
                },
                "axisX": {
                    "domain": True,
                    #"domainColor": axisColor,
                    "gridColor": gridColor,
                    "domainWidth": 1,
                    "grid": False,
                    "labelFont": font,
                    "labelFontSize": 12,
                    "labelAngle": 0, 
                    "tickColor": axisColor,
                    "tickSize": 5, # default, including it just to show you can change it
                    "titleFont": font,
                    "titleFontSize": 16,
                    "titlePadding": 10, # guessing, not specified in styleguide
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
                #"ticks": False, # even if you don't have a "domain" you need to turn these off.
                "titleFont": font,
                "titleFontSize": 16,
                "titlePadding": 10, # guessing, not specified in styleguide
                "title": "Y Axis Title (units)", 
                # titles are by default vertical left of axis so we need to hack this 
                #"titleAngle": 0, # horizontal
                #"titleY": -10, # move it up
                #"titleX": 18, # move it to the right so it aligns with the labels 
            },
        }
    }    
    
    # register the custom theme under a chosen name
    alt.themes.register('mds_special', mds_special)
    # enable the newly registered theme
    alt.themes.enable('mds_special')
    #alt.themes.enable('none') # to return to default
    
    def get_top_df(df, num, genre):
        """
        Finds the number of movies of the most productive directors in the selected genre and 
        movie information from the most productive directors in the selected genre.

        Parameters
        ----------
        df: pandas.DataFrame
            The data frame to work on
        num: int
            The number of directors to keep in each genre
        genre: string
            The selected genre

        Returns
        -------
        (pandas.DataFrame, pandas.DataFrame)
            The data frame only contains movie information from the most productive directors in the selected genre and 
            The data frame contains the number of movies of the most productive directors in the selected genre  
            
        """

        mdfg = df.groupby('Major_Genre')
        top_director = (mdfg.get_group(genre)
                        .groupby('Director')
                        .count()
                        .sort_values(by='Title', ascending = False)
                        .head(num)
                        .reset_index()
                        .iloc[:, :2]
                        .rename(columns={'Title': 'Count'}))    
        top_director['Major_Genre'] = genre
        top_df = pd.merge(df, 
                          top_director, 
                          how="inner",
                          on=['Major_Genre', 'Director'])
        return (top_director, top_df)

   
    brush = alt.selection(type='multi', encodings=['y'])

    
    # get the clean movies data
    movies_df = pd.read_csv('../data/clean/movies_clean_df.csv', index_col = 0)
    
    # get information from the 30 most productive directors in the selected genre
    top_director, top_df = get_top_df(movies_df, 30, genre)
    
    chart_1 = alt.Chart(top_director).mark_bar().encode(
                alt.Y('Director:N', 
                      title='Director', 
                      sort=alt.EncodingSortField(field="Count:Q",
                                                 order="ascending")),
                alt.X('Count:Q', 
                      title='Number of movies'),
                opacity=alt.condition(brush, 
                                      alt.value(0.75), 
                                      alt.value(0.05)),
              ).properties(
                title='Top 30 productive directors in ' + genre,
                width=200, 
                height=650
              ).add_selection(brush)
    
    chart_2 = alt.Chart(top_df).mark_circle().encode(
                alt.X("Year:O", 
                      axis=alt.Axis(title="Year")),
                alt.Y("IMDB_Rating:Q", 
                      axis=alt.Axis(title="IMDB Rating 1-10"), 
                      scale=alt.Scale(zero=False)),
                alt.Color('Director:N'),
                opacity=alt.condition(brush, alt.value(0.75), alt.value(0.05)),
                tooltip = ['Title', 'Major_Genre', 'Director', 'IMDB_Rating']
              ).properties(
                title='IMDB Rating',
                width=400, height=250
              ).interactive()
    
    chart_3 = alt.Chart(top_df).mark_circle().encode(
                alt.X("Year:O",
                      axis=alt.Axis(title="Year")),
                alt.Y("Profit_Million:Q", 
                      axis=alt.Axis(title="Profit (million USD)"), 
                      scale=alt.Scale(zero=False)),
                alt.Color('Director:N'),
                opacity=alt.condition(brush, alt.value(0.75), alt.value(0.05)),
                tooltip = ['Title', 'Major_Genre', 'Director', 'IMDB_Rating']
            ).properties(title='Worldwide Profit',
                        width=400, height=250).interactive()
    
    return chart_1 | (chart_2 & chart_3)


app.layout = html.Div([
    html.Iframe(
        sandbox='allow-scripts',
        id='plot1',
        height='650',
        width='550',
        style={'border-width': '0'},
        ################ The magic happens here
        srcDoc=make_plot().to_html()
        ################ The magic happens here
        ), 
    
    html.Div([

        html.Div([
            dcc.Dropdown(
        id='genre',
        options=[{'label': i, 'value': i} for i in genres],
        value='Action',
        style=dict(width='50%', verticalAlign="middle"),
        multi=False,
        searchable=True
        ),
        ]),
    
        html.Div([
            dcc.Dropdown(
                id='director',
                options=[{'label': i, 'value': i} for i in directors],
                value=['James Cameron', 'Michael Bay'],
                style=dict(width='50%',
                    verticalAlign="middle"),
                multi=True,
                searchable=True
        ),
        ])
    ])

    
        
])


@app.callback(
    dash.dependencies.Output('plot1', 'srcDoc'),
    [dash.dependencies.Input('genre', 'value'),
    dash.dependencies.Input('director', 'value')])
def update_plot(genre_value,
                director_value):
    """
    Takes in the genre and director and calls make_plot to update the plot
    """
    updated_chart = make_plot(genre_value, director_value).to_html()
    return updated_chart



if __name__ == '__main__':
    app.run_server(debug=True)
