### Reflections on the Altair Dashboard

#### Strengths

Our dashboard does well in letting the users interact with the various directors for a given genre. We kept the dashboard simple to make it more effective in looking at the plots and filters available while still answering our research questions. The bar plot was chosen to show the relationship between the directors and the number of movies for users to identify potential directors to compare. This plot answers our first research question on the top 30 most productive directors for a given genre. The line charts for "IMDB Ratings" and "Worldwide Profits" were chosen to show the different movies and their respective ratings and profits over time answering our research questions on what the profits and ratings for a specific director are. The interactivity between the most productive directors' chart and the other charts, gives the user the flexibility to choose the directors that are of interest to them. Our app allows multiple selection which allows the comparison of as many directors as the user wants. 

We took Ellen's feedback to not include the movie list as it would've been a lot of movies and text plotted. We instead re-arranged our prototype to focus on the graphs that better conveyed and answered our research questions. We also made sure to include our progress and roles in GitHub issues.

#### Weaknesses 

There are quite features we wish we could have added or refined if we had more time. We made the most productive directors' chart interactive to filter our rating and profit charts. However, since the rating and profit charts rely on the selection of the most productive directors' chart, we wanted to be able to pre-select 1-2 directors when the dashboard loaded. We can pre-select a director in a Jupyter notebook, but unfortunately, we cannot reproduce the pre-selection effect in the dashboard, which leads to an overplotted ratings and profit line chart upon loading the dashboard. These initial charts of many coloured lines are not an effective visualization. Besides, the legend of the rating and profit charts is truncated after translating Altair plots to HTML. We have been [in touch with Jake Vanderplas from Altair](https://github.com/UBC-MDS/DSCI532_GROUP104_Movies/issues/49) to discuss implementation to achieve our goals with these features.

#### Feedback and Reflection

Our peers found our app easy to use following the app instruction. They were able to choose multiple directors to explore their statistics as we expected. We got some suggestions and concluded here:
   
- Separate the app instruction from the plot label so that the instruction stands out.

- Point out the interactive feature between graphs in the instruction so that users know how to interact with the graphs.

- Change the initial state for the rating and profit plots so that not all directors show.

- Change the bar chart title when there are fewer than 30 directors in a selected genre.

- Make the points in the line charts bigger.


After reviewing the feedback, we find out that users can explore the functions of our app with the help of app instruction. Overall, they can use the app in an expected way. However, most of them point out that the app instruction would be more obvious and concise so that they can use the important interactive features more easily. Another common feedback is that changing the initial profit and rating plots and having a default selected director so that not all the directors show.

Based on the feedback, we think it is appropriate to adjust the app layout and the instruction text to make it more obvious and clear. It is also useful to add a description of the relationship between filtering in the bar chart and the effects on the line charts. Besides, we could modify the code to make the bar chart title show the actual number of directors in the bar chart. However, we think it is unnecessary to make points in line charts bigger since it doesn't make charts more effective. Another thing we are unable to implement is having a default selected director in the initial. We have tried that and contacted Jake last week, but it seems impossible to manage this feature in Dash.

We consider all the feedback valuable and the suggestion on the function instruction is the most valuable. The interactive component of clicking the bar to show the related movie ratings and profits in the right plots is the most important feature, so we should make sure the users know how to do that. The first part of the feedback process, "fly-on-the-wall", was most valuable since it gave us a great opportunity to test the usability of our app. We can learn if the app reaches our expectation by observing our "users". The observation and feedback gave us invaluable suggestions on how to improve and polish our app and led to an improved app after our adjustment.

#### Changes and Maintenance Strategy 

We decide to make the following changes:

- The first two suggestions say that our app instruction does not stand out and is not effective enough. Those suggestions are very helpful. And we decided to change the instruction layout and add descriptions to clarify the relationship between graphs and instruct on how to filter multiple directors.

- We would like to pre-select directors. But according to [Jake Vanderplas from Altair](https://github.com/UBC-MDS/DSCI532_GROUP104_Movies/issues/49), the pre-selection feature has not been implemented in the dashboard. So we are able to change the initial state for now.

- The last suggestion is reasonable, so we decided to change the bar chart title according to the number of directors shown in the chart.  

Details about those changes are in this [issue](https://github.com/UBC-MDS/DSCI532_GROUP104_Movies/issues/69).
