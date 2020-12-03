import json
import os

import dotenv
import tweepy


from pprint import pprint
from dataclasses import dataclass


import pika
import logging

logging.getLogger().setLevel(logging.INFO)


import time
print("publisher sleeping and waiting for rmq")
time.sleep(10)

dotenv.load_dotenv()

RMQ_USERNAME = os.getenv("RMQ_USERNAME")
RMQ_PWD = os.getenv("RMQ_PWD")
RMQ_HOST = os.getenv("RMQ_HOST")
RMQ_PORT = os.getenv("RMQ_PORT")

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

rmq_url = f"amqp://{RMQ_USERNAME}:{RMQ_PWD}@{RMQ_HOST}:{RMQ_PORT}/%2F"
print(f"publishing at {rmq_url}")


parameters = pika.URLParameters(rmq_url)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='stream')


@dataclass
class RetweetedInfo:
    original_handle: str
    retweeted_handle: str
    delta: str


class TwitterStreamListener(tweepy.StreamListener):

    def on_status(self, status):

        print(status.id_str, status.user.screen_name ,status.text, status.source)

        if self.is_retweet_of_tweet(status.text) and self.is_retweet_not_from_a_bot(status.source):
            retweet_info = RetweetedInfo(
                original_handle=status._json["retweeted_status"]["user"]["screen_name"],
                retweeted_handle=status._json["user"]["screen_name"],
                delta=str((status.created_at - status.retweeted_status.created_at).total_seconds())
            )
            pprint(vars(retweet_info))
            tweet_info = json.dumps(vars(retweet_info))
            self.send_tweet_info_rmq(tweet_info)


    def is_retweet_of_tweet(self, tweet_text):

        return True if 'RT' in tweet_text[0:3] else False


    def is_retweet_not_from_a_bot(self, tweet_source):

        possible_sources = ["Twitter for iPhone", "Twitter for Android", "Twitter for Web", "Twitter Web App"]
        return True if tweet_source in possible_sources else False

    
    def send_tweet_info_rmq(self, tweet_info):
        channel.basic_publish(exchange='', routing_key='stream', body=tweet_info)



class TweetManager:

    __instance = None

    def __init__(self, celeb_handles):

        if TweetManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            TweetManager.__instance = self

        self.watching_celebs = celeb_handles
        self.watching_celeb_twitter_ids = []
        self.twitter_api = self.authenticate_creds()
        self.get_twitter_ids()
        self.start_streaming()        


    @staticmethod
    def get_instance():
        if TweetManager.__instance == None:
            TweetManager()
        return TweetManager.__instance


    def authenticate_creds(self):
        
        consumer_key = CONSUMER_KEY
        consumer_secret = CONSUMER_SECRET
        access_token = ACCESS_TOKEN
        access_token_secret = ACCESS_TOKEN_SECRET
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api


    def get_twitter_ids(self):
        self.watching_celeb_twitter_ids = [self.twitter_api.get_user(handle).id_str for handle in self.watching_celebs]


    def start_streaming(self):
        tsl = TwitterStreamListener()
        self.ongoing_stream = tweepy.Stream(auth = self.twitter_api.auth, listener=tsl)
        self.ongoing_stream.filter(follow=self.watching_celeb_twitter_ids, is_async=True)
        print("started a stream for celebs")


    def append_celebs(self, new_celeb_handle):
        self.watching_celebs.append(new_celeb_handle)
        self.watching_celeb_twitter_ids.append(self.twitter_api.get_user(new_celeb_handle).id_str)


    def kill_and_start(self):
        self.ongoing_stream.disconnect()
        delattr(self, "ongoing_stream")
        self.start_streaming()