#!/usr/bin/env pytest
""" Tests for db/db.py. """

# Imports - Python Standard Library
from collections import namedtuple
from typing import Callable, List
from unittest.mock import MagicMock, patch

# Imports - Third-Party
from pytest import fixture
import sqlalchemy

# Imports - Local
from app.db.db import (
    commit_session, truncate_tables, get_hashtags,
    add_hashtags, get_tweets, add_tweets
)

# namedtuple objects
NewTweet = namedtuple(
    typename='NewTweet',
    field_names=[
        'tweet_id',
        'tweet_text',
        'created',
        'likes',
        'retweets'
    ]
)

# Constants
DB_TEST_SESSION_NAME = 'postgresql'
DB_TEST_SESSION_BINDING = 'postgresql://root:***@db:5432/ww_tweeter_test'
GET_DB_DATA_RESPONSE = [1, 'test_data', 10]
NEW_HASHTAGS = {
    'hashtag_1': 10,
    'hashtag_2': 20,
    'hashtag_3': 30,
}
GET_TWEETS_SEARCH_STRING = 'Hashtag'
NEW_TWEETS = [
    NewTweet(
        tweet_id='Tweet #1',
        tweet_text='This is a tweet #1',
        created='2022-03-01 22:25:28.357434',
        likes=10,
        retweets=20
    )
]


# Test classes
class SessionBindURLMock:
    """ Mock sqlalchemy.orm.session.get_bind.url object. """

    def render_as_string(self):
        url_as_string = DB_TEST_SESSION_BINDING

        return str(url_as_string)


# Define a QueryMock class for the SessionMock.query method response object
class QueryMock:
    """ Mock of the Session.query method response object. """

    def __init__(
        self,
        instance: str
    ) -> None:
        """ Class initialization method.

            Args:
                instance (str):
                    Placeholder/mock for database table class.

            Returns:
                None.
        """

        # Set an instance variable based on the database table name
        self.instance = instance

        # Set an instance variable based on the query_result argument
        self.query_result = GET_DB_DATA_RESPONSE

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

    def delete(self) -> str:
        """ Mock of the delete method.

            Args:
                None.

            Returns:
                None.
        """

        return None

    def filter(
        self,
        criterion
    ) -> List:
        """ Mock of the filter method.

            Args:
                criterion:
                    Mock criterion to filter results by, in the form of
                    a database class attribute:
                        (filter(TweetData.tweet_text.ilike(filter)).

            Returns:
                filtered_query (List):
                    Mock filtered list of query results.
        """

        # Create a mock ordered list of query results
        filtered_query = QueryMock(
            instance=self.instance)

        return filtered_query

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
        ordered_query = QueryMock(
            instance=self.instance)

        return ordered_query


# Define a SessionMock class for the test methods
class SessionMock(QueryMock):
    """ Mock of the sqlalchemy.orm.Session class. """

    def __init__(self) -> None:
        """ Class initialization method. """

        # Initialize an empty list for database transactions
        self.transactions = []

    def add(
        self,
        instance: str
    ) -> None:
        """ Mock of the add method.

            Args:
                instance (str):
                    Placeholder/mock for database table class.

            Returns:
                None.
        """

        # Add a mock transaction to the transactions list
        self.transactions.append(instance)

        return None

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
        instance: str
    ) -> QueryMock:
        """ Mock of the query method.

            Args:
                instance (str):
                    Database table class definition.

            Return:
                query_mock (class):
                    Placeholder/mock for database table class.
        """

        # Create an instance of QueryMock
        query_mock = QueryMock(
            instance=instance
        )

        # Append the return value to self.transactions
        self.transactions.append(query_mock)

        return query_mock


# pytest fixtures
@fixture
def session_mock() -> SessionMock:
    """ A pytest fixture to create a SessionMock object.

        Mocks the sqlalchemy.orm.Session object.

        Args:
            None.

        Returns:
            mock_session (SessionMock):
                Mock of an sqlalchemy.orm.Session object.
    """

    # Create a mock Session object
    mock_session = SessionMock()

    return mock_session


# Test functions
@patch.object(
    target=sqlalchemy.orm,
    attribute='Session'
)
def test_commit_session(
    mock_session: MagicMock,
    session_mock: SessionMock
) -> None:
    """ Test the commit_session function.

        Args:
            mock_session (unittest.mock.MagicMock):
                unittest MagicMock object.

            session_mock (SessionMock):
                Mock sqlalchemy.orm.Session object.

        Returns:
            None.
    """

    # Call commit_session and pass the mock Session object
    session_in_transaction = commit_session(
        session=session_mock
    )

    assert session_in_transaction is False

    return None


@patch.object(
    target=sqlalchemy.orm,
    attribute='Session'
)
def test_create_session(
    mock_session: MagicMock,
    session_mock: SessionMock
) -> None:
    """ Test the commit_session function.

        Args:
            mock_session (unittest.mock.MagicMock):
                unittest MagicMock object.

            session_mock (SessionMock):
                Mock sqlalchemy.orm.Session object.

        Returns:
            None.
    """

    assert session_mock.get_bind().name == DB_TEST_SESSION_NAME
    assert session_mock.get_bind().url.render_as_string() == \
        DB_TEST_SESSION_BINDING

    return None


@patch.object(
    target=sqlalchemy.orm,
    attribute='Session'
)
def test_truncate_tables(
    mock_session: MagicMock,
    session_mock: SessionMock
) -> None:
    """ Test the truncate_tables function.

        A call to truncate_tables will return False when the session
        successfully commits, while a return value of True indicates
        the session has pending transactions and did not successfully
        commit.

        Args:
            mock_session (unittest.mock.MagicMock):
                unittest MagicMock object.

            session_mock (SessionMock):
                Mock sqlalchemy.orm.Session object.

        Returns:
            None.
    """

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
    mock_session: MagicMock,
    session_mock: SessionMock
) -> None:
    """ Test the get_hashtags function.

        Args:
            mock_session (unittest.mock.MagicMock):
                unittest MagicMock object.

            session_mock (SessionMock):
                Mock sqlalchemy.orm.Session object.

        Returns:
            None.
    """

    # Call get_hashtags and pass the mock session object
    hashtags = get_hashtags(
        session=session_mock
    )

    assert hashtags == GET_DB_DATA_RESPONSE

    return None


@patch.object(
    target=sqlalchemy.orm,
    attribute='Session'
)
def test_add_hashtags(
    mock_session: MagicMock,
    session_mock: SessionMock
) -> None:
    """ Test the get_hashtags function.

        Args:
            mock_session (unittest.mock.MagicMock):
                unittest MagicMock object.

            session_mock (SessionMock):
                Mock sqlalchemy.orm.Session object.

        Returns:
            None.
    """

    # Call add_hashtags and pass the mock Session object
    session_in_transaction = add_hashtags(
        hashtags=NEW_HASHTAGS,
        session=session_mock
    )

    assert session_in_transaction is False

    return None


@patch.object(
    target=sqlalchemy.orm,
    attribute='Session'
)
def test_get_tweets(
    mock_session: MagicMock,
    session_mock: SessionMock
) -> None:
    """ Test the get_tweets function.

        Args:
            mock_session (unittest.mock.MagicMock):
                unittest MagicMock object.

            session_mock (SessionMock):
                Mock sqlalchemy.orm.Session object.

        Returns:
            None.
    """

    # Call add_hashtags and pass the mock Session object
    tweets = get_tweets(
        search_tag=GET_TWEETS_SEARCH_STRING,
        session=session_mock
    )

    assert tweets == GET_DB_DATA_RESPONSE

    return None


@patch.object(
    target=sqlalchemy.orm,
    attribute='Session'
)
def test_add_tweets(
    mock_session: MagicMock,
    session_mock: SessionMock
) -> None:
    """ Test the add_tweets function.

        Args:
            mock_session (unittest.mock.MagicMock):
                unittest MagicMock object.

            session_mock (SessionMock):
                Mock sqlalchemy.orm.Session object.

        Returns:
            None.
    """

    # Call add_tweets and pass the mock Session object
    session_in_transaction = add_tweets(
        tweets=NEW_TWEETS,
        session=session_mock
    )

    assert session_in_transaction is False

    return None
