#!/usr/bin/env python3
""" SQLAlchemy Models for db.py """

# Imports - Python Standard Library
from sqlalchemy import (
    Column, DateTime, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base

# Imports - Third-Party

# Imports - Local

# Constants
BASE = declarative_base()


class Hashtag(BASE):
    """ Create table for hashtags and hitcounts.

        Args:
            BASE (sqlalchemy.ext.declarative.declarative_base)
    """

    # Assign table name
    __tablename__ = 'hashtags'

    # Assign table columns
    id = Column(
        type_=Integer,
        primary_key=True
    )
    name = Column(String(20))
    count = Column(Integer)

    # Create repr function
    def __repr__(self):
        """ Function that returns the hashtag name and count.

            Args:
                None.

            Returns:
                repr_string (str):
                    Returns a string with the hashtag and hashtag
                    count.
        """

        repr_string = (
            f'<Hashtag(name={self.name}, count={self.count})>'
        )

        return repr_string


class TweetData(BASE):
    """ Create table for hashtags and hitcounts.

        Args:
            BASE (sqlalchemy.ext.declarative.declarative_base)
    """

    # Assign table name
    __tablename__ = 'tweets'

    # Assign table columns
    id = Column(
        type_=Integer,
        primary_key=True
    )
    tweet_id = Column(String(22))
    tweet_text = Column(String(300))
    created = Column(DateTime)
    likes = Column(Integer)
    retweets = Column(Integer)

    # Create repr function
    def __repr__(self):
        """ Function that returns the tweet ID and text.

            Args:
                None.

            Returns:
                repr_string (str):
                    Returns a string with the tweet ID and tweet
                    text.
        """

        repr_string = (
            f'<Tweet(id={self.id}), tweet_id={self.tweet_id}, '
            f'text={self.tweet_text}), tweet_created={self.created}, '
            f'likes={self.likes}, retweets={self.retweets})>'
        )

        return repr_string
