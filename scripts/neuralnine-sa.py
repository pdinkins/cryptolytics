# NeuralNine twitter sentiment analysis
#https://www.youtube.com/watch?v=dSOUd9Sm1gI

import tweepy
import textblob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# must set up twitter developer account and project to obtain keys
all_keys = open('twitterkeys', 'w').read().splitlines()

api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]

# authenticator to send the access token to the api 
authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)
api = tweepy.API(authenticator, wait_on_rate_limit=True)

topic = "Bitcoin"

search = f'#{topic} -filter:retweets'

tweet_cursor = tweepy.Cursor(api.search, q=search, lang='en', tweet_mode='extended').items(100)

# list of all of the tweets for the twitter api based on our parameters
tweets = [tweet.full_text for tweet in tweet_cursor]
