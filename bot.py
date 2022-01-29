import tweepy

from config import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
from reply import replyTweets

client = tweepy.Client(consumer_key = consumer_key,
                    consumer_secret = consumer_secret,
                    access_token = access_token,
                    access_token_secret = access_token_secret,
                    bearer_token= bearer_token)

####Replying
replyTweets(client)



