
import plotly as py
import plotly.figure_factory as ff
import pandas as pd


trump = Sem_Analysis()
trump.sent_tweet("Trump/sfo.txt")
hillary = Sem_Analysis()
hillary.sent_tweet("Hillary/sfo.txt")
bernie = Sem_Analysis()
bernie.sent_tweet("tweetsbernie.txt")
data_matrix = [['Name', 'Number of<br>Positive<br>comments', 'Number of<br>Neutral<br>comments','Number of<br>Negative<br>comments',
                '% Positive ','% Neutral','% Negative ',
                'Average<br>Polarity','Average<br>Subjectivity'],
               ['Trump', trump.count_positive, trump.count_neutral,trump.count_negative,trump.percent_positive,
                trump.percent_neutral,trump.percent_negative,
                trump.Average_polarity, trump.Average_subjectivity],
               ['Hillary', hillary.count_positive, hillary.count_neutral, hillary.count_negative, hillary.percent_positive,
                hillary.percent_neutral,hillary.percent_negative,
                hillary.Average_polarity, hillary.Average_subjectivity],
               ['bernie', bernie.count_positive, bernie.count_neutral, bernie.count_negative,bernie.percent_positive,
                bernie.percent_neutral,bernie.percent_negative, bernie.Average_polarity, bernie.Average_subjectivity]
              ]

table = ff.create_table(data_matrix)
table.layout.width=1000 #width in pixels
py.offline.iplot(table, filename='jupyter/table')