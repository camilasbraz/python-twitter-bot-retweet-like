import tweepy
from time import sleep
import datetime

import os
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


def api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)


def retweet(tweepy_api: tweepy.API, hashtag: str, delay=60, items=10):
    print(f"*** \n{datetime.datetime.now()}\n***")

    for tweet in tweepy.Cursor(tweepy_api.search_tweets, q=hashtag).items(items):
        try:
            # print(tweet) # prints all the metadata that the tweet has
            tweet_id = dict(tweet._json)["id"]
            tweet_text = dict(tweet._json)["text"]

            print("id: " + str(tweet_id))
            print("text: " + str(tweet_text)[0:70] + "...")

            # Retweets the tweet
            tweepy_api.retweet(tweet_id)

            # Adds the tweet as a favourite
            tweepy_api.create_favorite(tweet_id)

        except tweepy.TweepyException as error:
            print(error)
            sleep(.5)

    print("")
    sleep(delay)


if __name__ == '__main__':
    api = api()

    while True:
        retweet(api, 'Felipe Amorin', delay=10, items=10)