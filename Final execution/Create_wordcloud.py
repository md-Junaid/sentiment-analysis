#wordcloud

from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
stopwords = nltk.corpus.stopwords.words('english')
from nltk.stem.snowball import SnowballStemmer
ss = SnowballStemmer("english")
text = open('tweetshillary.txt').read()
text2 = ''
for word in text.split():
    if len(word) == 1 or word in stopwords:
        continue
    text2 += ' {}'.format(word)
ss.stem(text2)

wordcloud = WordCloud(max_font_size=150,width=800,height=400).generate(text)

plt.figure(figsize=(20,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()