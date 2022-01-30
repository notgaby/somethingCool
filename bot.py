import tweepy

from config import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
from reply import replyTweets, getActivity

client = tweepy.Client(consumer_key = consumer_key,
                    consumer_secret = consumer_secret,
                    access_token = access_token,
                    access_token_secret = access_token_secret,
                    bearer_token= bearer_token)

                    
# Replace the text with whatever you want to Tweet about
#response = client.create_tweet(text='bing bong3')
####Replying
replyTweets(client)

