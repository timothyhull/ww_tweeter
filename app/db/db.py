#!/usr/bin/env python3
""" TODO """

# Imports - Python Standard Library
from os import getenv
import re

# Imports - Third-Party
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import sessionmaker

# Imports - Local
from app.db.db_models import (
    BASE, Hashtag, TweetData
)

# Constants
VALID_HASHTAG = (r'^[a-z0-9]+$')


# Functions
def _create_session() -> None:
    """ """

    return None


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
