import random
import tweepy
import pandas as pd
from time import sleep

#Search tweets that @ the account and have #activitiesjsc2022
def replyTweets(client):
  query = '@hellospace101 #activitiesjsc2022 -is:retweet'  #Don't include retweets
  tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at'], expansions = 'author_id', max_results=10) 

  for tweet in tweets.data: #Filter from queries
    authorId = tweet.author_id  #get id of person who tweeted
    userName = (client.get_user(id = authorId)).data  #get username of person who tweeted

    status = '@' + str(userName) + '\n' + getActivity() #Tweet that the bot will produce
    client.create_tweet(text = status, in_reply_to_tweet_id = tweet.id) 
    sleep(5) 
  
  print('finished')

#Get random activity to add to tweet
def getActivity():
  df = pd.read_csv('activities.csv')

  #Get number of entries
  numEntries = len(df.index)
  randomEntry = random.choice(list(range(0, numEntries + 1))) #create a list from [0, numEntries] and choose a random number

  #Create a tweet from the random index corresponding to csv row
  status = df.iloc[randomEntry].Title + '\n' + df.iloc[randomEntry].Description + '\n' + df.iloc[randomEntry].URL

  return status
 
  

#Stretch: reply to tweet based on command (similar to discord bot)