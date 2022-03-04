#!/usr/bin/env python3
""" Twitter analyzer for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library
from itertools import islice
from os import getenv
from collections import namedtuple

# Imports - Third-Party
from tweepy.api import API
from tweepy.cursor import Cursor
import dotenv
import tweepy

# Imports - Local
from app.db.db import (
    add_tweets, truncate_tables
)

# namedtuple objects
Tweet = namedtuple(
    typename='Tweet',
    field_names=[
        'id',
        'text',
        'created',
        'likes',
        'retweets'
    ]
)

# Load environment variables
dotenv.load_dotenv()

# Constants
TWITTER_ACCOUNT = 'wwt_inc'
TWITTER_KEY = getenv('TWITTER_KEY')
TWITTER_SECRET = getenv('TWITTER_SECRET')
TWITTER_ACCESS_TOKEN = getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_SECRET = getenv('TWITTER_ACCESS_SECRET')
TWITTER_TIMEOUT = 5
TWEET_SLICE = 100


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

    # Return a slice of the tweets generator object
    tweets = islice(tweets, TWEET_SLICE)

    return tweets


def main() -> None:
    """ Main program.

        Args:
            None.

        Returns:
            None.
    """

    # Clear the database tables
    truncate_tables()

    # Create a twitter API authentication object
    api = twitter_api_auth()

    # Collet tweets from the Twitter API
    tweets = get_top_n_tweets(
        api_object=api
    )

    # Add tweets to the database
    add_tweets(
        tweets=list(tweets)
    )

    return None


if __name__ == '__main__':
    main()
