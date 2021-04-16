import tweepy
from kafka import KafkaConsumer, KafkaProducer
import time
import config

# Authenticate to Twitter
auth = tweepy.OAuthHandler(config.tw_credentials["consumer_key"], config.tw_credentials["consumer_secret"])
auth.set_access_token(config.tw_credentials["oauth_token"], config.tw_credentials["oauth_token_secret"])

# Create API object
api = tweepy.API(auth)

producer = KafkaProducer(bootstrap_servers=config.server["ip"]+':'+config.server["port"])
topic_name = 'twitter'

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        producer.send(topic_name, str.encode(status.text))
        time.sleep(2)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.sample(languages=['es'])