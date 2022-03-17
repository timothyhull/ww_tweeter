#!/usr/bin/env python3
""" Twitter analyzer for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library
from collections import Counter
from itertools import islice
from os import getenv
from typing import Dict, Iterable

# Imports - Third-Party
from tweepy.api import API
from tweepy.cursor import Cursor
import dotenv
import tweepy

# Imports - Local
from app.db import db

# Load environment variables
dotenv.load_dotenv()

# Constants
TWITTER_ACCOUNT = 'wwt_inc'
TWITTER_KEY = getenv('TWITTER_KEY')
TWITTER_SECRET = getenv('TWITTER_SECRET')
TWITTER_ACCESS_TOKEN = getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_SECRET = getenv('TWITTER_ACCESS_SECRET')
TWITTER_TIMEOUT = 30
TWEET_SLICE = 500  # Sets the limit of tweets, set to None for no limit


def twitter_api_auth() -> API:
    """ Create a Twitter API object with access keys/tokens/secrets.

        Args:
            None.

        Returns:
            api (tweepy.api.API):
                tweepy API object with credentials.
    """

    # Create an authentication object with the consumer key & secret
    auth = tweepy.OAuthHandler(
        consumer_key=TWITTER_KEY,
        consumer_secret=TWITTER_SECRET
    )

    # Add the access token & secret to the authentication object
    auth.set_access_token(
        key=TWITTER_ACCESS_TOKEN,
        secret=TWITTER_ACCESS_SECRET
    )

    # Authenticate and create a connection to the Twitter API
    api = tweepy.API(
        auth=auth,
        timeout=TWITTER_TIMEOUT
    )

    return api


def get_top_n_tweets(
    api_object: API
) -> Cursor:
    """ Collect tweets using tweepy.Cursor.

        Args:
            api_object (tweepy.api.API):
                tweepy API object with credentials.

        Returns:
            tweets (tweepy.cursor.Cursor):
                tweepy Cursor iterator object with tweet data
    """

    # Use tweepy.Cursor to get tweets from the Twitter API
    tweets = tweepy.Cursor(
        method=api_object.user_timeline,
        screen_name=TWITTER_ACCOUNT,
        exclude_replies=False,
        include_rts=True
    ).items()

    # If TWEET slice is set, return only a slice of the tweets generator object
    if TWEET_SLICE is not None:
        tweets = islice(tweets, TWEET_SLICE)

    return tweets


def hashtag_counter(
    tweets: Iterable
) -> Dict:
    """ Counts and sorts hashtags in a list of tweets.

        Args:
            tweets (Iterable):
                Iterable object with tweets.

        Returns:
            hashtag_count (Dict):
                Counter object of hashtags converted to a list when
                sorted using the Counter.most_common method. Converted
                to a Dict before returning.
    """

    # Create a space-separated sting of all words in all tweets
    tweet_text = ' '.join(tweet.text.lower() for tweet in tweets)

    # Create a sorted Counter object of hashtags from tweet_text
    hashtag_count = Counter(
        db.VALID_HASHTAG.findall(tweet_text)
    ).most_common()

    # Convert hashtag_count to a dictionary
    hashtag_count = dict(hashtag_count)

    return hashtag_count


def main() -> None:
    """ Main program.

        Args:
            None.

        Returns:
            None.
    """

    # Clear the database tables
    db.truncate_tables()

    # Create a twitter API authentication object
    api = twitter_api_auth()

    # Collet tweets from the Twitter API
    tweets = get_top_n_tweets(
        api_object=api
    )

    # Convert tweets to from an islice to a list
    tweets = list(tweets)

    # Add tweets to the database
    db.add_tweets(tweets=tweets)

    # Collect a count of hashtags
    hashtag_count = hashtag_counter(tweets=tweets)

    # Add hashtags to the database
    db.add_hashtags(hashtags=hashtag_count)

    return None


if __name__ == '__main__':
    main()
