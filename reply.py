import tweepy

#Search tweets that @ the account and have #activitiesjsc2022
def searchTweets(client):
  query = '@hellospace101 #activitiesjsc2022 -is:retweet'  #Don't include retweets

  tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)
  print(tweets)

#Reply to tweet


#Stretch: reply to tweet based on command (similar to discord bot)