#!/usr/bin/env pytest
""" Tests for tweeter.py. """

# Imports - Python Standard Library
from types import GeneratorType
from typing import Dict
from unittest.mock import MagicMock, patch

# Imports - Third-Party
from tweepy.api import API
import tweepy

# Imports - Local
from app.tweeter.tweeter import (
    twitter_api_auth, get_top_n_tweets, hashtag_counter, TWEET_SLICE
)


# class objects
class TweepyAPIMock:
    """ Mock a tweepy.api.API object to retreive mock tweets. """

    def __init__(self) -> None:
        return None

    def user_timeline(self) -> None:
        return None


class Status:
    """ Mock a Status object in the tweepy.Cursor response object. """

    def __init__(
        self,
        mock_api: API,
        mock_tweets: Dict
    ) -> None:
        """ Populate the Status object with mocked attributes.

            Args:
                mock_api (tweepy.api.API):
                    mock_api (tweepy.api.API):
                    Pass a tweepy.api.API object to this argument in
                    the format "Status(mock_api=API)".

                mock_tweets (Dict):
                    Pass a dictionary with one or more mocked tweets.
                    For this test, pass the value TWEET_MOCK in the
                    format "Status(mock_api=API, mock_json=TWEET_MOCK".

            Returns:
                None.
        """

        # Create attributes that match the mocked Status object
        self._api = mock_api,
        self._json = mock_tweets
        self.text = self._json.get('text')

        return None


class CursorMock:
    """ Mock a tweepy.cursor.Cursor object to return mocked tweets. """

    def __init__(
        self,
        _status: Status
    ) -> None:
        """ Create attributes for a tweepy.cursor.Cursor object.

            Call the items method after creating the self.status
            attribute.

            Args:
                _status (Status):
                    Status class object with _api and _json attributes.

            Returns:
                None.
        """

        self._status = _status
        self.items()

        return None

    def items(self) -> GeneratorType:
        """ Mock the response to the tweepy.Cursor items method.

            The tweepy.Cursor.items method returns a generator with all
            tweets.  This function returns a generator with one or more
            tweets.

            Args:
                None.

            Yields:
                self.status (GeneratorType)
        """

        self.status = self._status

        yield self.status


# Constants
TWEEPY_API_MOCK = TweepyAPIMock()

TWEET_MOCK = {
    'created_at': 'Thu Jan 20 19:35:26 +0000 2022',
    'id': 1484248219051827202,
    'text': '1 in 3 customers will leave a #brand they love after...',
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

CURSOR_STATUS_MOCK = Status(
    mock_api=API,
    mock_tweets=TWEET_MOCK
)

CURSOR_MOCK = CursorMock(
    _status=CURSOR_STATUS_MOCK
)


# Test functions
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
    attribute='Cursor',
    return_value=CURSOR_MOCK
)
def test_get_top_n_tweets(
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
    tweets = get_top_n_tweets(
        api_object=TWEEPY_API_MOCK
    )

    # Read the next iteration from the tweets generator object
    tweet_mock = next(tweets)._json

    # Assert the number of tweets is <= TWEET_SLICE
    assert len(list(tweet_mock)) <= TWEET_SLICE

    # Assert the mocked tweet's text matches the expected value
    assert tweet_mock.get('text') == TWEET_MOCK.get('text')

    return None


def test_hashtag_counter() -> None:
    """ Test the get_tweets function.

        Args:
            None.

        Returns:
            None.
    """

    # Call the hashtag_counter function
    hashtag_count = hashtag_counter(
        tweets=CURSOR_STATUS_MOCK.text
    )

    # Look for the count of the hashtag #brand
    assert hashtag_count[0][1] == 1

    return None
