#!/usr/bin/env python3
""" Database/controller interactions for ww-tweeter. """

# Imports - Python Standard Library
from os import getenv
import re
from sys import argv
from typing import Dict, List, Tuple, Union

# Imports - Third-Party
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import dotenv
import sqlalchemy

# Imports - Local
from app.db.db_models import (
    BASE, Hashtag, TweetData
)

# Load environment variables
env_vars = dotenv.load_dotenv()


# Constants
AUTO_FLUSH = True
DB_LOGGING = True
DB_URL = getenv(key='DB_URL', default=None)
DB_TEST_URL = getenv(key='DB_TEST_URL', default=None)
VALID_HASHTAG = re.compile(r'^[a-z0-9]+$')


# Classes
Session = sessionmaker(
    autoflush=AUTO_FLUSH
)


# Functions
def _create_session() -> sqlalchemy.orm.Session:
    """ Create and Bind an Engine object to a Session object.

        Add an sqlalchemy.engine.Engine binding to the custom Session
        class.

        Args:
            None.

        Returns:
            session (sqlalchemy.orm.Session):
                Instance of the Session class with an engine binding.
    """

    # Set the context appropriate DB URL
    if 'pytest' in argv[0]:
        db_url = DB_TEST_URL
    else:
        db_url = DB_URL

    # Verify db_url is not None
    if db_url is None:
        raise EnvironmentError(
            '\nSet the "DB_URL" and/or "DB_TEST_URL" environment variables\n'
        )

    # Create an sqlalchemy.engine.Engine object
    engine = create_engine(
        db_url,
        echo=DB_LOGGING
    )

    # Call the BASE object's create_all method to create database tables
    BASE.metadata.create_all(engine)

    # Bind the Session class to a database URL
    Session.configure(
        bind=engine
    )

    # Create a session class instance
    session = Session()

    return session


# Create a session object using _create_session, or set to None for pytest
if 'pytest' in argv[0]:
    session = None
else:
    session = _create_session()


def commit_session(
    session: sqlalchemy.orm.Session = session
) -> bool:
    """ Commit the SQLAlchemy session to the database.

        Args:
            session (sqlalchemy.orm.Session, optional):
                By default, uses the session object created by the
                _create_session function.  Allows the ability to pass a
                mock Session object for pytest testing.

        Returns:
            session_in_transaction (bool):
                False if the transaction is complete, True if the
                transaction is neither committed nor rolled back.
    """

    # Commit the changes to the database
    session.commit()

    # Collect the session transaction status
    session_in_transaction = session.in_transaction()

    return session_in_transaction


def truncate_tables(
    session: sqlalchemy.orm.Session = session
) -> bool:
    """ Remove all rows from the database tables.

        Args:
            session (sqlalchemy.orm.Session, optional):
                By default, uses the session object created by the
                _create_session function.  Allows the ability to pass a
                mock Session object for pytest testing.

        Returns:
            session_active (bool):
                False if the transaction is complete, True if the
                transaction is neither committed nor rolled back.
    """

    # Delete data returned by a query of the TweetData and Hashtag tables
    session.query(TweetData).delete()
    session.query(Hashtag).delete()

    # Commit the changes to the database
    session_active = commit_session(
        session=session
    )

    return session_active


def get_hashtags(
    session: sqlalchemy.orm.Session = session
) -> List:
    """ Get all hashtags from the database.

        Args:
            session (sqlalchemy.orm.Session, optional):
                By default, uses the session object created by the
                _create_session function.  Allows the ability to pass a
                mock Session object for pytest testing.

        Returns:
            hashtags (List):
                All entries in the hashtags table.
    """

    # Retreive and sort all entries from the hashtags table
    hashtags = session.query(Hashtag).order_by(Hashtag.name.asc()).all()

    return hashtags


def add_hashtags(
    hashtags: Dict,
    session: sqlalchemy.orm.Session = session
) -> bool:
    """ Add hashtags to the database.

        Args:
            hashtags (Dict):
                Dictionary object with new hashtags.

        session (sqlalchemy.orm.Session, optional):
            By default, uses the session object created by the
            _create_session function.  Allows the ability to pass a
            mock Session object for pytest testing.

        Returns:
           session_active (bool):
                False if the transaction is complete, True if the
                transaction is neither committed nor rolled back.
    """

    # Add new hashtags to the session object
    for hashtag, count in hashtags.items():
        session.add(
            instance=Hashtag(
                name=hashtag,
                count=count
            )
        )

    # Commit the changes to the database
    session_active = commit_session(
        session=session
    )

    return session_active


def get_tweets(
    search_tag: str = None,
    session: sqlalchemy.orm.Session = session
) -> List:
    """ Get all hashtags from the database.

        Args:
            search_tag (str, optional):
                Hashtag search string for query filter.  Default value
                is None, and will return all results.

            session (sqlalchemy.orm.Session, optional):
                By default, uses the session object created by the
                _create_session function.  Allows the ability to pass a
                mock Session object for pytest testing.

        Returns:
            tweets (List):
                All entries in the tweets table.
    """

    # Get tweets from the database
    tweets = session.query(TweetData)

    # Attemt to filter tweet results
    if search_tag is not None:
        valid_hashtag = VALID_HASHTAG.match(
            string=search_tag.lower()
        )

        # Check the validity of the hashtag
        if valid_hashtag is not None:
            filter = search_tag.lower()

            # Apply a filter to the tweet data
            tweets = tweets.filter(TweetData.tweet_text.ilike(filter))

    # Return all tweets from the query
    tweets = tweets.all()

    return tweets


def add_tweets(
    tweets: Union[Dict, List, Tuple],
    session: sqlalchemy.orm.Session = session
) -> bool:
    """ Add hashtags to the database.

        Args:
            tweets (Dict, List, or Tuple):
                Dictionary object with new tweets.

        session (sqlalchemy.orm.Session, optional):
            By default, uses the session object created by the
            _create_session function.  Allows the ability to pass a
            mock Session object for pytest testing.

        Returns:
           session_active (bool):
                False if the transaction is complete, True if the
                transaction is neither committed nor rolled back.
    """

    # Determine the object type of tweets, and set/reset the value accordingly
    if isinstance(tweets, list) or isinstance(tweets, tuple):
        tweets = tweets
    elif isinstance(tweets, dict):
        tweets = tweets.items()
    else:
        raise ValueError(
            '"tweets" must be of type "list" or "dict"'
        )

    # Add new tweets to the session object
    for tweet in tweets:
        session.add(
            instance=TweetData(
                tweet_id=tweet.id,
                tweet_text=tweet.text,
                created=tweet.created_at,
                likes=tweet.favorite_count,
                retweets=tweet.retweet_count
            )
        )

    # Commit the changes to the database
    session_active = commit_session(
        session=session
    )

    return session_active
