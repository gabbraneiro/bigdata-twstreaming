import tweepy
from kafka import KafkaConsumer, KafkaProducer
import time

credentials = {
    "consumer_key": "oNpNwmR05Yb0E0lPpkwBMSkhH",
    "consumer_secret": "H66yQHTkK7PYOh56rHnc1Y1xBDRAXwsApaVVtdl1m69dza3waJ",
    "oauth_token": "1469089382-ZLcRCjpotJcHUP5agdm7DDQfJHMRc0NEWbdxBKd",
    "oauth_token_secret": "4Uo9PJTwRv1oZ2wNyrzQMwTzcvXw3y79JmcVTrlvQt7u8"
}

# Authenticate to Twitter
auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
auth.set_access_token(credentials['oauth_token'], credentials['oauth_token_secret'])

# Create API object
api = tweepy.API(auth)

producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic_name = 'twitter'

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        producer.send(topic_name, str.encode(status.text))
        time.sleep(2)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.sample(languages=['es'])