from twython import TwythonStreamer
from unidecode import unidecode
import sys

tweet_text = []
num=20

CONSUMER_KEY = '1XlO7bDLYARB1tTjZ4cspV1Q2'
CONSUMER_SECRET = 'othIx7WctmMQ38NEwXja2hKGsamKpVeohvAGgQfuxXoZlyFoZ3'
ACCESS_TOKEN = '846796640811933697-ttfVB5ekh6zLLh73DdUjFWy5ZpEjYWH'
ACCESS_TOKEN_SECRET = 'UJqdU8ZrjR7FmcsJlReJMmI2KcMKFyVxz4d5eLk0F33qA'

tweet_locations = {
    'dfw': "-97.48,32.31,-96.49,33.26,",
    'jfk': "-74,40,-73,41",
    'sfo': "-122.75,36.8,-121.75,37.8",
    'lax': "-118.43,33.73,-117.93,34.21",
    'ord': "-88.47,41.46,-87.16,42.35",
    'dca': "-77.26,38.73,-76.87,39.10",
    'atl': "-84.54,33.62,-84.18,33.96"
}

class MyStreamer(TwythonStreamer):
     # overriding
    def on_success(self, data):
        if data['lang'] == 'en':
            
            # filter tweet
            twitter_words = [u'http',u'https',u'RT','https','http',u's://t.co','rt','amp',u'amp',u'u2026',u'u2019']   
            text=unidecode(data['text'])
            for word in twitter_words:
                text=text.replace(word,'')
            text=text.strip()              
            text=text.replace('\n','')  #to remove newline
            tweet_text.append(text)
      
        if len(tweet_text) >= num:
            self.disconnect()

    # overriding
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()
        
# download 
keyword = 'obama'
location = 'sfo'
bounds = tweet_locations[location]
stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#stream.statuses.filter(track=keyword,locations=bounds)
stream.statuses.filter(track=keyword)
f=open('Obama/sfo.txt','w')
for i in range(num):
    f.write(tweet_text[i]+'\n')
f.close()
print(len(tweet_text))