import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("MKRxouO4qhfq5GcZiNypdypmS", #api key
    "T9IsYM7iEdcuyjZTiC75mQB2286JhcibhJByc5zmy8HXw3QQju")
auth.set_access_token("1484434372061188096-Ks4WzWGHgjOfupsfXCAfSSXy1QO6rk", 
    "GVjVhNtYRi1bpUSqCcL5QOg2pcRz9tI09YHlmC9U3P6k8")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")