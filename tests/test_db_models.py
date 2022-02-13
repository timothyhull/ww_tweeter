#!/usr/bin/env pytest
""" Tests for db/db_models.py. """

# Imports - Python Standard Library

# Imports - Third-Party

# Imports - Local
from app.db.db_models import (
    Hashtag, TweetData
)

# Constants


# Test functions
def test_instantiate_hashtag() -> None:
    """ Create instance of the Hashtag class.

        Args:
            None.

        Returns:
            None.
    """

    hashtag_instance = Hashtag()
    assert hashtag_instance.__tablename__ == 'hashtags'

    return None


def test_instantiate_tweet_data() -> None:
    """ Create instance of the TweetData class.

        Args:
            None.

        Returns:
            None.
    """

    tweet_data_instance = TweetData()
    assert tweet_data_instance.__tablename__ == 'tweets'

    return None
