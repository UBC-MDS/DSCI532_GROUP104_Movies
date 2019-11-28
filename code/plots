def make_plot_1(genre="Action", director="James Cameron"):

    def get_top_director(genre_1="Action"):
        """
        Finds the number of movies of the most productive directors in the selected genre
        """
        mdfg = movie_df.groupby('Major_Genre')
        return (mdfg.get_group(genre_1)
                .groupby('Director')
                .count()
                .sort_values(by = 'Title', ascending = False)
                .head(30)
                .reset_index()
                .iloc[:, :2]
                .rename(columns = {'Title': 'Count'}))

    def get_top_df(chosen_genre="Action"):
        """
        Finds movie information from the most productive directors in the selected genre
        """
        top_director = get_top_director(genre)
        top_director['Major_Genre'] = chosen_genre
        return pd.merge(movie_df, 
                    top_director, 
                    how = "inner", 
                    on = ['Major_Genre', 'Director'])
    
    df_genre = get_top_df(genre)
    df_genre['profit'] = (df_genre['Worldwide_Gross'] - df_genre['Production_Budget'])/1000000
    df_director = df_genre[df_genre.Director.isin(director)]
    
    #df_director = df_genre[(df_genre['Director'] == director)]

    # Create a plot of the Displacement and the Horsepower of the cars dataset
    
    brush = alt.selection(type='single', resolve='global');
    #selection = alt.selection_single();
    base = alt.Chart(df_director).mark_circle(size=80).add_selection(brush
    ).encode(
                alt.X("Year:O"),
                color=alt.condition(brush, "Director:N", alt.value('grey')),
                opacity=alt.condition(brush, alt.value(0.8), alt.value(0.1))
            ).properties(width=400, height=250).interactive()

    plot = (base.encode(alt.Y("IMDB_Rating:Q", axis=alt.Axis(title="Mark"), scale=alt.Scale(zero=False)),
                       tooltip = ['Title', 'Major_Genre', 'Director', 'IMDB_Rating']).properties(title='Rating',) & base.encode(alt.Y("profit:Q", axis=alt.Axis(title="Profit (M USD)"), scale=alt.Scale(zero=False)),
                       tooltip = ['Title', 'Major_Genre', 'Director', 'profit']).properties(title='Profit',))
    
    return plot
make_plot_1(genre="Action", director=["James Cameron", "Michael Bay"])
