### Reflections on the Altair Dashboard

#### Strengths

Our dashboard does well in letting the users interact with the various directors for a given genre. We kept the dashboard simple to make it more effective in looking at the plots and filters available while still answering our research questions. The bar plot was chosen to show the relationship between the directors and the number of movies for users to identify potential directors to compare. This plot answers our first research question on the top 30 most productive directors for a given genre. The line charts for "IMDB Ratings" and "Worldwide Profits" were chosen to show the different movies and their respective ratings and profits over time answering our research questions on what the profits and ratings for a specific director are. The interactivity between the most productive directors' chart and the other charts, gives the user the flexibility to choose the directors that are of interest to them. Our app allows multiple selection which allows the comparison of as many directors as the user wants. 

We took Ellen's feedback to not include the movie list as it would've been a lot of movies and text plotted. We instead re-arranged our prototype to focus on the graphs that better conveyed and answered our research questions. We also made sure to include our progress and roles in GitHub issues.

#### Weaknesses 

There are quite features we wish we could have added or refined if we had more time. We made the most productive directors' chart interactive to filter our rating and profit charts. However, since the rating and profit charts rely on the selection of the most productive directors' chart, we wanted to be able to pre-select 1-2 directors when the dashboard loaded. We can pre-select a director in a Jupyter notebook, but unfortunately, we cannot reproduce the pre-selection effect in the dashboard, which leads to an overplotted ratings and profit line chart upon loading the dashboard. These initial charts of many coloured lines are not an effective visualization. Besides, the legend of the rating and profit charts is truncated after translating Altair plots to HTML. We have been [in touch with Jake Vanderplas from Altair](https://github.com/UBC-MDS/DSCI532_GROUP104_Movies/issues/49) to discuss implementation to achieve our goals with these features.

#### Feedback and Reflection

Our peers found our app easy to use following the instructions on our app. They were able to choose multiple directors to explore their statistics as we expected. We compiled our suggestion below:
   
- Separate the instructions from the plot title, so that the instructions stand out.

- Describe the interactive feature between graphs in the instructions so that users know how to interact with the graphs.

- Change the initial state for the rating and profit plots so that not all directors show.

- Change the number on bar chart title when there are fewer than 30 directors in a selected genre.

- Make the points in the line charts bigger.

- Remove the scroll from the line charts since it doesn't add additional information.

- Put a cap on the number of directors that can be selected to not overplot the line charts.

- Make the title of the bar chart two lines because if you select a long movie title it adds a scroll bar to the bottom.

After reviewing the feedback, we found that users can explore the functions of our app with the help of app's instructions. Overall, they can use the app in an expected way. However, most of them pointed out that the instructions could be more obvious and concise to be able to use the interactive features more easily. Another common feedback comment is to change the initial profit and rating plots and having a default selected director so that not all the directors show. We agree with this comment, but could not implement it in the timeframe. We included this weakness in our weakness section above. 

Based on the feedback, we think it is appropriate to adjust the app layout and the text for the instructions to make it more obvious and clear. It is also useful to add a description of the relationship between filtering in the bar chart and the effects on the line charts. We also modify the code to make the bar chart title show the actual number of directors in the bar chart. However, we think it is unnecessary to make points in line charts bigger since it doesn't make charts more effective. Another thing we were unable to implement is having a default selected director in the initial loading of the dashboard. We agree that is is an important feature to address, but we contacted Jake last week and it seems impossible to manage this feature in Dash.

We compiled all the feedback and broke them down into priorities for our implementation this week. We found the suggestion on the updating and clarifying functionality instructions was the most valuable. The interactive component of clicking the bar to show the related movie ratings and profits in the right plots is the most important feature, so we should make sure the users know how to do that. The first part of the feedback process, "fly-on-the-wall", was most valuable since it gave us a great opportunity to test the usability of our app. We can learn if the app reaches our expectation by observing our "users". The observation and feedback gave us invaluable suggestions on how to improve and polish our app and led to an improved app after our adjustment.

#### Changes and Maintenance Strategy 

We decided to make the following changes:

- The first two suggestions say that the instructions on our app do not stand out and are not effective enough. Those suggestions are very helpful to understand users’ perspectives on our app. We took the feedback and decided to change the instructions layout and add descriptions to clarify the relationship between graphs and instruct on how to filter multiple directors. We used bold to make the important multi-selection interactivity stand out. 

- We would like to pre-select directors, but according to [Jake Vanderplas from Altair](https://github.com/UBC-MDS/DSCI532_GROUP104_Movies/issues/49), the pre-selection feature has not been implemented in  Dash. So we are able to change the initial state for now.

- The suggestion on changing the title for the number of directors was reasonable, so we decided to change the title according to the number of directors shown in the chart. 

- We removed the zooming in and out of the line charts and set the y-axis to start at zero. 

- We looked into making the title of the bar chart two lines since a scroll bar appears when you select Thriller/Suspense as a genre. We researched this feature, but it seems to still be an [issue in Vega-lite](https://github.com/altair-viz/altair/issues/262) with no update on how to do it. 

- We looked into selecting a maximum amount of directors, but it was not implemented due to the low priority and short timeframe for the complexity of the problem. This would also require more instructions on the app as this would be something that would confuse users if they were unable to select additional directors.  It would be a future improvement for the dashboard and would tie in to pre-selecting directors as it would be a condition upon loading. 

Details about all feedback and priority list are in this [issue](https://github.com/UBC-MDS/DSCI532_GROUP104_Movies/issues/69).

