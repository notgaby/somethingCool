from time import sleep
import tweepy

#Search tweets that @ the account and have #activitiesjsc2022
def replyTweets(client):
  query = '@hellospace101 #activitiesjsc2022 -is:retweet'  #Don't include retweets
  tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at'], expansions = 'author_id', max_results=10)

  for tweet in tweets.data:
    authorId = tweet.author_id
    userName = (client.get_user(id = authorId)).data
    status = '@' + str(userName) + ' i am replying again'
    client.create_tweet(text = status, in_reply_to_tweet_id = tweet.id)
    sleep(10) 

#Stretch: reply to tweet based on command (similar to discord bot)