from time import sleep
import tweepy

#Search tweets that @ the account and have #activitiesjsc2022
def replyTweets(client):
  query = '@hellospace101 #activitiesjsc2022 -is:retweet'  #Don't include retweets
  tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at'], expansions = 'author_id', max_results=10) 

  for tweet in tweets.data: #Filter from queries
    authorId = tweet.author_id  #get id of person who tweeted
    userName = (client.get_user(id = authorId)).data  #get username of person who tweeted

    status = '@' + str(userName) + ' i am replying again' #Tweet that the bot will produce
    client.create_tweet(text = status, in_reply_to_tweet_id = tweet.id) 
    sleep(10) 

#Get random activity to add to tweet

#Stretch: reply to tweet based on command (similar to discord bot)