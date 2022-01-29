import tweepy

from config import consumer_key, consumer_secret, access_token, access_token_secret

client = tweepy.Client(consumer_key = consumer_key,
                    consumer_secret = consumer_secret,
                    access_token = access_token,
                    access_token_secret = access_token_secret)
                    
# Replace the text with whatever you want to Tweet about
response = client.create_tweet(text='hello world3')