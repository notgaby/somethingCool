import random
import tweepy
import string
import pandas as pd
from time import sleep

#Search tweets that @ the account and have #activitiesjsc2022
def replyTweets(client):
  query = '@hellospace101 #activitiesjsc2022 -is:retweet '  #Don't include retweets
  tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at'], expansions = 'author_id', max_results=10) 

  for tweet in tweets.data: #Filter from queries
    #check if already replied
    with open('lastTweet.txt') as f:
      if str(tweet.id) in f.read():
        print("SKIP")
        continue
    
    authorId = tweet.author_id  #get id of person who tweeted
    userName = (client.get_user(id = authorId)).data  #get username of person who tweeted

    #write id in text file
    f = open('lastTweet.txt', 'a')
    f.write(str(tweet.id) + '\n')
    f.close()

    
    status = '@' + str(userName) + '\n' + getActivity() #Tweet that the bot will produce
    #print("TWEETING NEW: " + status)
    client.create_tweet(text = status, in_reply_to_tweet_id = tweet.id) 



    sleep(5) 
  
  #print('finished')

#Get random activity to add to tweet
def getActivity():
  df = pd.read_csv('activities.csv')

  #Get number of entries
  print("numEntries: " + numEntries)
  numEntries = len(df.index)
  randomEntry = random.randint(0, numEntries) #create a list from [0, numEntries] and choose a random number

  #print("NUMMM: " + str(randomEntry))
  #Create a tweet from the random index corresponding to csv row

  #Generate random to avoid same tweet being executed twice
  uniqueId = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(2)])

  print("UNIW: " + uniqueId)

  status = df.iloc[randomEntry].Title + ' ' + uniqueId + '\n' + df.iloc[randomEntry].Description + '\n' + df.iloc[randomEntry].URL 

  print(str(status) + '\n')

  return status
 
  

#Stretch: reply to tweet based on command (similar to discord bot)