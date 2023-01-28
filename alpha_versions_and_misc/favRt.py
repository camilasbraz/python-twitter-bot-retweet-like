from config import CreateApi
import tweepy
import logging
import json

from dotenv import load_dotenv
import os
load_dotenv()
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class FavRetweetListener(tweepy.Stream):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, api):
        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret)
        self.api = api
        self.me = api.get_user(screen_name="felipeAmorinBot")

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it
            try:
                tweet.retweet()
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)

def main(keywords):
    api = CreateApi()
    stream = tweepy.Stream(consumer_key, consumer_secret, access_token, access_token_secret)
    stream.filter(track=["Tweepy"])
    #tweets_listener = FavRetweetListener(api)
    #printer = FavRetweetListener(consumer_key, consumer_secret, access_token, access_token_secret,api)
    #printer.sample()
    #stream = tweepy.Stream(consumer_key, consumer_secret, access_token, access_token_secret)
    #stream.filter(track=keywords, languages=["en"])

if __name__ == "__main__":
    main(["Python", "Tweepy"])