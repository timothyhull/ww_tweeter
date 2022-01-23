#!/usr/bin/env python3
""" Twitter analyzer for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library
from os import getenv
from collections import namedtuple

# Imports - Third-Party
import dotenv
import tweepy

# Imports - Local

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


def twitter_api_auth() -> tweepy.API:
    """ Create a Twitter API object with access keys/tokens/secrets.

        Args:
            None.

        Returns:
            api (tweepy.API):
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


def get_tweets(
    api: tweepy.API
) -> None:
    """ Collect tweets using tweepy.Cursor.

        Args:
            api (tweepy.API):
                tweepy API object with credentials.

        Returns:
            None.
    """

    return None


def main() -> None:
    """ Main program.

        Args:
            None.

        Returns:
            None.
    """

    api = twitter_api_auth()
    print(api)

    return None


if __name__ == '__main__':
    main()
