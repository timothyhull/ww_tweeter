#!/usr/bin/env pytest
""" Tests for tweeter.py. """

# Imports - Python Standard Library
from types import GeneratorType
from unittest.mock import MagicMock, patch

# Imports - Third-Party
import tweepy

# Imports - Local
from app.tweeter import (
    twitter_api_auth, get_tweets
)


# class objects
class TweepyAPIMock:

    def __init__(self) -> None:
        return None

    def user_timeline(self) -> None:
        return None


# Constants
TWEEPY_API_MOCK = TweepyAPIMock()

TWEET_MOCK = {
    'created_at': 'Thu Jan 20 19:35:26 +0000 2022',
    'id': 1484248219051827202,
    'text': '1 in 3 customers will leave a brand they love after...',
    'user': {
        'id': 370255074,
        'id_str': '370255074',
        'name': 'World Wide Technology',
        'screen_name': 'wwt_inc',
        'location': 'Global',
        'description': 'Combining strategy and execution to help...',
        'url': 'https://t.co/KYeroT8Oj6'
    }
}


def tweet_mock() -> GeneratorType:
    """ Mock one iteration of a tweepy.cursot.Cursor response.

        Args:
            None.

        Returns:
            TWEET_MOCK (GeneratorType):
                Generator function with one available tweet iteration.
    """

    yield TWEET_MOCK


def test_twitter_auth() -> None:
    """ Test the twitter_auth function.

        Args:
            None.

        Returns:
            None
    """

    # Call the twitter_auth function
    api = twitter_api_auth()

    # Assert credential values are set
    assert api.auth.consumer_key
    assert api.auth.consumer_secret
    assert api.auth.access_token
    assert api.auth.access_token_secret

    return None


@patch.object(
    target=tweepy,
    attribute='Cursor'
)
def test_get_tweets(
    cursor: MagicMock
) -> None:
    """ Test the get_tweets function.

        Args:
            cursor (unittest.mock.MagicMock):
                Mocked cursor object.

        Returns:
            None.
    """

    # Call the get_tweets function
    get_tweets(
        api_object=TWEEPY_API_MOCK
    )

    mocked_tweet = tweet_mock()

    assert next(mocked_tweet)['text'].startswith('1 in 3')

    return None
