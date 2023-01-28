import tweepy
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(format='%(levelname)s [%(asctime)s] %(message)s', datefmt='%m/%d/%Y %r', level=logging.INFO)
logger = logging.getLogger()

search_keywords = "Felipe Amorin OR felipe amorin"
# search_keywords = "Python OR bot"

# Time to wait between processing a request in seconds 
# Information about TwitterAPI limits here: https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits
delay = 10

# Specify what type of search results you want to get
# 'recent', 'popular', or 'mixed'
result_type = 'mixed'

# Specify the number of tweets you want the bot to iterate through
number_of_tweets = 5
# OR change run_continuously to True if you want it to run continuously (or for deploying)
# if True, number_of_tweets will not be used
run_continuously = True

# Change booleans depending on if you want to only retweet, only like, or do both
retweet_tweets = True
like_tweets = True


def CreateApi():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info(f"API created! Connection to @{api.get_user(screen_name='felipeAmorinBot').name}")
    return api