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


# Define a QueryMock class for the SessionMock.query method response object
class QueryMock:
    """ Mock of the Session.query method response object. """

    def delete(self) -> str:
        """ Mock of the delete method.

            Args:
                None.

            Returns:
                None.
        """

        return None


# Define a SessionMock class for the test methods
class SessionMock:
    """ Mock of the sqlalchemy.orm.Session class. """

    def __init__(self) -> None:
        """ Class initialization method. """

        # Initialize an empty list for database transactions
        self.transactions = []

    def commit(self) -> None:
        """ Mock of the commit method.

            Args:
                None.

            Returns:
                None.
        """

        # Clear the list of transactions
        self.transactions.clear()

        return None

    def in_transaction(self) -> bool:
        """ Mock of the in_transaction method.

            A return value of False indicates the session has been
            committed, while a return value of True indicates the
            session has pending transactions and is not committed.

            Args:
                None.

            Returns:
                in_transaction (bool).
        """

        # Determine if the self.transactions list is contains items, or not
        if self.transactions:
            in_transaction = True
        else:
            in_transaction = False

        return in_transaction

    def query(
        self,
        db_table: str
    ) -> QueryMock:
        """ Mock of the query method.

            Args:
                None.

            Return:
                None.
        """

        # Create an instance of QueryMock
        query_mock = QueryMock()

        # Append the return value to self.transactions
        self.transactions.append(query_mock)

        return QueryMock()


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


@patch.object(
    target=sqlalchemy.orm.Query,
    attribute='delete'
)
@patch.object(
    target=sqlalchemy.orm.Query,
    attribute='delete'
)
@patch.object(
    target=sqlalchemy.orm.Session,
    attribute='commit'
)
@patch.object(
    target=sqlalchemy.orm.Session,
    attribute='in_transaction'
)
def test_truncate_tables(
    session_query_1,
    session_query_2,
    session_commit,
    session_in_transaction
) -> None:
    """ Test the truncate_tables function.

        A return value of False indicates the session successfully
        committed, while a return value of True indicates the session
        has pending transactions and did not successfully commit.

        Args:
            None.

        Returns:
            None.
    """

    session = SessionMock()
    session_query_1.return_value = session.query('TweetData').delete()
    session_query_2.return_value = session.query('Hashtag').delete()
    session_commit.return_value = session.commit()
    session_in_transaction.return_value = session.in_transaction()

    assert truncate_tables() is False

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
