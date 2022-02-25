#!/usr/bin/env pytest
""" Tests for db/db.py. """

# Imports - Python Standard Library
import re
from typing import Callable, List
from unittest.mock import MagicMock, patch

# Imports - Third-Party
import sqlalchemy

# Imports - Local
from app.db.db import (
    truncate_tables, get_hashtags, add_hashtags,
    get_tweets, add_tweets
)

# Constants
DB_TEST_SESSION_NAME = 'postgresql'
DB_TEST_SESSION_BINDING = 'postgresql://root:***@db:5432/ww_tweeter_test'
GET_HASHTAGS_RESPONSE = [1, 'hashtag_1', 25]


# Test classes
class SessionBindURLMock:
    """ Mock sqlalchemy.orm.session.get_bind.url object. """

    def render_as_string(self):
        url_as_string = DB_TEST_SESSION_BINDING

        return str(url_as_string)


# Define an OrderByMock class for the test methods
class OrderByMock:
    """ Mock of the Session.query.orderby method response object. """

    def __init__(
        self,
        query_result: List
    ) -> List:
        """ Class initialization method. """

        # Set an instance variable based on the query_result argument
        self.query_result = GET_HASHTAGS_RESPONSE

        return None

    def all(self) -> List:
        """ Mock of the all method.

            Args:
                None.

            Returns:
                self.query_result (List):
                    Mock of all objects returned by a query.
        """

        return self.query_result


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

    def order_by(
        self,
        criterion
    ) -> List:
        """ Mock of the order_by method.

            Args:
                criterion:
                    Mock criterion to order results by, in the form of
                    a database class attribute (Hashtag.name.asc()).

            Returns:
                ordered_query (List):
                    Mock ordered list of query results.
        """

        # Create a mock ordered list of query results
        ordered_query = OrderByMock(query_result=criterion)

        return ordered_query


# Define a SessionMock class for the test methods
class SessionMock(QueryMock):
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

    def get_bind(self) -> Callable:
        """ get_bind method mock.

        Args:
            None.

        Returns:
            self.get_bind (Callable):
                Callable self.get_bind object.
        """

        return self.get_bind

    get_bind.name = DB_TEST_SESSION_NAME
    get_bind.url = SessionBindURLMock()

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
                query_mock (class):
                    Instance of the QueryMock class.
        """

        # Create an instance of QueryMock
        query_mock = QueryMock()

        # Append the return value to self.transactions
        self.transactions.append(query_mock)

        return query_mock


# Test functions
@patch.object(
    target=sqlalchemy.orm,
    attribute='Session'
)
def test_create_session(
    mock_session: MagicMock
) -> None:
    """ Test the _create_session function.

        Args:
            mock_session (unittest.mock.MagicMock):
                unittest MagicMock object.

        Returns:
            None.
    """

    # Create a mock Session object
    session_mock = SessionMock()

    assert session_mock.get_bind().name == DB_TEST_SESSION_NAME
    assert session_mock.get_bind().url.render_as_string() == \
        DB_TEST_SESSION_BINDING

    return None


@patch.object(
    target=sqlalchemy.orm,
    attribute='Session'
)
def test_truncate_tables(
    mock_session: MagicMock
) -> None:
    """ Test the truncate_tables function.

        A call to truncate_tables will return False when the session
        successfully commits, while a return value of True indicates
        the session has pending transactions and did not successfully
        commit.

        Args:
            mock_session (unittest.mock.MagicMock):
                unittest MagicMock object.

        Returns:
            None.
    """

    # Create a mock Session object
    session_mock = SessionMock()

    # Call truncate_tables and pass the mock Session object
    session_in_transaction = truncate_tables(
        session=session_mock
    )

    assert session_in_transaction is False

    return None


@patch.object(
    target=sqlalchemy.orm,
    attribute='Session'
)
def test_get_hashtags(
    mock_session: MagicMock
) -> None:
    """ Test the get_hashtags function.

        Args:
            mock_session (unittest.mock.MagicMock):
                unittest MagicMock object.

        Returns:
            None.
    """

    session_mock = SessionMock()

    hashtags = get_hashtags(
        session=session_mock
    )

    assert hashtags == GET_HASHTAGS_RESPONSE

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
