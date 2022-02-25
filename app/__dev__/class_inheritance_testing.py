#!/usr/bin/env python3
""" Tests for adding classes with methods as attributes to classes.

    The intent is to return an object in the format:
        session.query(Hashtag).order_by(Hashtag.name.asc()).all()
"""

from typing import List


# Define a OrderByMock class for the SessionMock.query.order_by response object
class OrderByMock:
    """ Mock of the Session.query method response object. """

    def __init__(
        self,
        query_result: List
    ) -> List:
        """ Class initialization method. """

        # Set an instance variable based on the query_result argument
        self.query_result = query_result

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
        query_result: List
    ) -> OrderByMock:
        """ Mock of the order_by method.

            Args:
                None.

            Returns:
                ordered_list (OrderByMock).
        """

        # Create a mock ordered query result object
        query_result = OrderByMock(query_result)

        return query_result


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
