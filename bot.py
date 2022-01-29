import tweepy

client = tweepy.Client(consumer_key="3Bh4BzDfe40ciAKHIvwx5Pehe",
                    consumer_secret="sIEZlTUeQLxACnsiOrp4rsh8kD1uEFoph7WI27kUmOAj6mQEoV",
                    access_token="1484434372061188096-lU0VPJyP2FSajDfbiwqt8TYvJdSCYA",
                    access_token_secret="zQX3w6LfUbpSHn0X8VH6ilyZg4ZRkEws6KCtjC7reJDi3")
                    
# Replace the text with whatever you want to Tweet about
response = client.create_tweet(text='hello world')