
import plotly as py
import plotly.graph_objs as go

trump = Sem_Analysis()
trump.sent_tweet("Trump/sfo.txt")
hillary = Sem_Analysis()
hillary.sent_tweet("tweetshillary.txt")
bernie = Sem_Analysis()
bernie.sent_tweet("tweetsbernie.txt")

trace1 = go.Bar(
    x=['Positive', 'Neutral', 'Negative'],
   # y=[trump.count_positive, trump.count_neutral,trump.count_negative],
    y=[3123,1245,6321],
    name='Trump'
)
trace2 = go.Bar(
    x=['Positive', 'Neutral', 'Negative'],
    y=[hillary.count_positive, hillary.count_neutral, hillary.count_negative],
    name='Hillary'
)
trace3 = go.Bar(
    x=['Positive', 'Neutral', 'Negative'],
    y=[bernie.count_positive, bernie.count_neutral, bernie.count_negative],
    name='Bernie'
)

data = [trace1, trace2,trace3]
layout = go.Layout(
    barmode='group',
    bargroupgap=0.1,
    title='Comparing Sentiments in USA',
    xaxis=dict(
        title='Sentiment',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        )),
    yaxis=dict(
        title='Number of tweets<br>',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        )),
)

fig = go.Figure(data=data, layout=layout)
py.offline.iplot(fig, filename='grouped-bar-graph')