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
DB_TEST_SESSION_BINDING = 'postgresql://root:***@db:5432/ww_tweeter_test'


# Test classes
class SQLAlchemyORMSessionMockBindURL:
    """ Mock sqlalchemy.orm.session.get_bind.url object. """

    def render_as_string(self):
        url_as_string = DB_TEST_SESSION_BINDING

        return str(url_as_string)


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
    get_bind.url = SQLAlchemyORMSessionMockBindURL()


# Test functions
@patch.object(
    target=sqlalchemy.orm,
    attribute='Session'
)
def test_create_session(mock_session) -> None:
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
