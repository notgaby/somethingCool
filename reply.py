import tweepy

#Search tweets that @ the account
def searchTweets(client):
  #tweetedAt = client.get_user_mentions('hellospace101', tweet_fields=['context_annotations', 'created_at'], max_results=100)
  #tweetedAt = tweepy.Client.get_user_mentions('hellospace101', tweet_fields=['context_annotations', 'created_at'], max_results=100)
  query = 'from:suhemparack -is:retweet'

  tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)
  print(tweets)

#Reply to tweet


#Stretch: reply to tweet based on command (similar to discord bot)