import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('tweets.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error en el dato: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

# Credendiales de app twitter
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#Python'])
