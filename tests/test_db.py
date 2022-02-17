#!/usr/bin/env pytest
""" Tests for db/db.py. """

# Imports - Python Standard Library
from unittest.mock import patch

# Imports - Third-Party
import sqlalchemy

# Imports - Local
from app.db.db import (
    _create_session, truncate_tables, get_hashtags, add_hashtags,
    get_tweets, add_tweets
)

# Constants
DB_TEST_SESSION_NAME = 'postgresql'
# DB_TEST_SESSION_BINDING = 'postgresql://root:***@db:5432/ww_tweeter_test'
DB_TEST_SESSION_BINDING = 12345


# Test classes
class SQLAlchemyORMSessionMockBindURL:
    """ Mock sqlalchemy.orm.session.get_bind.url object. """

    def __init__(self) -> None:

        self.url = DB_TEST_SESSION_BINDING

    def render_as_string(self):

        return str(self.url)


class SQLAlchemyORMSessionMock:
    """ Mock sqlalchemy.orm.session object. """

    def get_bind(self) -> None:
        """ get_bind method mock.

        Args:
            None.

        Returns:
            None.
        """

        return self.get_bind

    get_bind.name = DB_TEST_SESSION_NAME
    get_bind.url = DB_TEST_SESSION_BINDING


# Test functions
@patch.object(
    target=sqlalchemy,
    attribute='orm.Session'
)
def test_create_session() -> None:
    """ Test the _create_session function.

        Args:
            None.

        Returns:
            None.
    """

    session = _create_session()
    assert session.get_bind().name == DB_TEST_SESSION_NAME
    assert session.get_bind().url.render_as_string() == DB_TEST_SESSION_BINDING

    return None


def test_truncate_tables() -> None:
    """ """

    return None


def test_get_hashtags() -> None:
    """ """

    return None


def test_add_hashtags() -> None:
    """ """

    return None


def test_get_tweets() -> None:
    """ """

    return None


def test_add_tweets() -> None:
    """ """

    return None
