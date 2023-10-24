import tweepy
import sys
import os

# Get key, token, and secrets, stored as GitHub secrets, from GitHub Actions as environmental variables
consumer_key = os.getenv('YOUR_CONSUMER_KEY')
consumer_secret = os.getenv('YOUR_CONSUMER_SECRET')
access_token = os.getenv('YOUR_ACCESS_TOKEN')
access_secret = os.getenv('YOUR_ACCESS_SECRET')

# Create a client object
client = tweepy.Client(consumer_key=consumer_key,consumer_secret=consumer_secret,access_token=access_token,access_token_secret=access_secret)

# Get the tweet text from the command line arguments
tweet_text = ' '.join(sys.argv[1:])

# Create a tweet
client.create_tweet(text=tweet_text)
