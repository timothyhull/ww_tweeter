#!/usr/bin/env python3
""" SQLAlchemy Object Relational Tutorial (1.x API).

    Code to support the SQLAlchemy tutorial at:
    https://docs.sqlalchemy.org/en/14/orm/tutorial.html
"""

# Imports - Python Standard Library
from os import getenv

# Imports - Third-Party
from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base
import sqlalchemy

# Imports - Local

# Constants
BASE = declarative_base()
DB_LOGGING = True
DB_URL = getenv('DB_TEST_URL')


# Class objects
class User(BASE):
    """ Class mapping to the users table.

        References:
            https://docs.sqlalchemy.org/en/14/orm/tutorial.html#declare-a-mapping

        Args:
            BASE (sqlalchemy.orm.decl_api.DeclarativeMeta)
    """

    __tablename__ = 'users'

    id = Column(
        type_=Integer,
        primary_key=True
    )
    name = Column(type_=String)
    fullname = Column(type_=String)
    nickname = Column(type_=String)

    def __repr__(self) -> str:
        repr_string = (
            f'<User('f'name={self.name}, '
            f'fullname={self.fullname}, '
            f'nickname={self.fullname})>'
        )

        return repr_string


def sqlalchemy_version() -> str:
    """ Display the SQLAlchemy version.

        Reference:
            https://docs.sqlalchemy.org/en/14/orm/tutorial.html#version-check

        Args:
            None.

        Returns:
            version (str):
                SQLAlchemy version.
    """

    # Create a version display string for formatting
    version_str = (
        f'SQLAlchemy Version {sqlalchemy.__version__}'
    )

    # Create a header string
    header_str = f'{"*" * (len(version_str) + 4)}'

    # Create a formatted header string
    version = (
        f'\n{header_str}\n'
        f'* {version_str} * \n'
        f'{header_str}\n'
    )

    return version


def create_db_engine() -> Engine:
    """ Create SQLAlchemy Engine object.

        Creates core database interface through the PostgreSQL dialect.

        References:
            https://docs.sqlalchemy.org/en/14/orm/tutorial.html#connecting
            https://docs.sqlalchemy.org/en/14/glossary.html#term-dialect
            https://docs.sqlalchemy.org/en/14/glossary.html#term-DBAPI
            https://docs.sqlalchemy.org/en/14/core/engines.html#postgresql

        Args:
            None.

        Returns:
            engine (sqlalchemy.engine.Engine):
                SQLAlchemy Engine object.
    """

    # Create an sqlalchemy.engine.Engine object
    engine = create_engine(
        DB_URL,
        echo=DB_LOGGING
    )

    return engine


def get_user_schema() -> None:
    """ Get an instance the User class schema 

        The User class construction takes place via the Declarative
        system.  The Declarative system creates a Table object for the
        users table.

        References:
            https://docs.sqlalchemy.org/en/14/orm/tutorial.html#create-a-schema
            https://docs.sqlalchemy.org/en/14/orm/tutorial.html#create-an-instance-of-the-mapped-class

        Args:
            None.

        Returns:
            user (User):
                Instance of the User class.
    """

    # Display the user table schema object
    user = User

    return user


def main() -> None:
    """ Main program.

        Args:
            None.

        Returns:
            None.
    """

    # Display SQLAlchemy version
    print(sqlalchemy_version())

    # Create SQLAlchemy engine
    engine = create_db_engine()

    # Display engine object
    print(f'Database Engine: "{engine}"\n')

    # Display the user table schema
    user = get_user_schema()
    print(
        'Users table schema:\n'
        f'{repr(user.__table__)}\n'
    )

    # Inspect an instance of the User class
    user_1 = get_user_schema()
    user_1.name = 'Timothy'
    user_1.nickname = 'Tim'
    print(
        'Users instance:\n'
        f'\nName: {user_1.name}\n'
        f'Nickname: {user_1.nickname}\n'
        f'ID: {repr(user_1.id)}\n'
    )


if __name__ == '__main__':
    main()
