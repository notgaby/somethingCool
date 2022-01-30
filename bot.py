import tweepy
import os
from time import sleep
#from config import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
from reply import replyTweets, getActivity

client = tweepy.Client(consumer_key = os.environ['consumer_key'],
                    consumer_secret = os.environ['consumer_secret'],
                    access_token = os.environ['access_token'],
                    access_token_secret = os.environ['access_token_secret'],
                    bearer_token= os.environ['bearer_token'])

def run():
  while True:
    replyTweets(client) ####Replying
    sleep(5)


if __name__ == '__main__':
  run()