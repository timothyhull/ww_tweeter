#!/usr/bin/env python3
""" Database/controller interactions for ww-tweeter. """

# Imports - Python Standard Library
from os import getenv
import re
from sys import argv

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
VALID_HASHTAG = (r'^[a-z0-9]+$')


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


# Create a global session object
session = _create_session()


def truncate_tables() -> None:
    """ """

    return None


def get_hashtags() -> None:
    """ """

    return None


def add_hashtags() -> None:
    """ """

    return None


def get_tweets() -> None:
    """ """

    return None


def add_tweets() -> None:
    """ """

    return None
