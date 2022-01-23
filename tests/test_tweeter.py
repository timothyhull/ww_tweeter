#!/usr/bin/env pytest
""" Tests for tweeter.py. """

# Imports - Python Standard Library

# Imports - Third-Party

# Imports - Local
from app.tweeter import (
    twitter_api_auth,  # get_tweets
)

# Constants


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


def test_get_tweets() -> None:
    """ Test the get_tweets function.

        Args:
            None.

        Returns:
            None.
    """

    # Call the get_tweets function
    # get_tweets()

    return None
