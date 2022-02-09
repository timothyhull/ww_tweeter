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
from sqlalchemy.orm import (
    declarative_base, sessionmaker
)
import sqlalchemy

# Imports - Local

# Constants
AUTO_FLUSH = True
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


# Create custom SQLAlchemy Session class, disable automatic transaction flush
Session = sessionmaker(
    autoflush=AUTO_FLUSH
)


# Functions
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
                Instance of the SQLAlchemy Engine class.
    """

    # Create an sqlalchemy.engine.Engine object
    engine = create_engine(
        DB_URL,
        echo=DB_LOGGING
    )

    return engine


def create_db_tables(
    engine: Engine
) -> None:
    """ Create database tables.

        Create database tables for any class object with the
        BASE object passed as an argument.  For example:
            class User(BASE):

        References:
            https://docs.sqlalchemy.org/en/14/orm/tutorial.html#create-a-schema

        Args:
            engine (sqlalchemy.engine.Engine):
                Instance of the SQLAlchemy Engine class.

        Returns:
            None.
    """

    # Call the BASE object's create_all method to create database tables
    BASE.metadata.create_all(engine)

    return None


def get_user_schema() -> None:
    """ Get an instance the User class schema,

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


def config_session_db_engine(
    engine: Engine
) -> None:
    """ Bind an SQLAlchemy Engine object to a Session object.

        Add an sqlalchemy.engine.Engine binding to the custom Session
        class.

        References:
            https://docs.sqlalchemy.org/en/14/orm/tutorial.html#creating-a-session

        Args:
            engine (sqlalchemy.engine.Engine):
                Instance of the SQLAlchemy Engine class.

        Returns:
            session (sqlalchemy.orm.Session):
                Instance of the Session class with an engine binding.
    """

    # Configure the Session class with an engine binding
    Session.configure(
        bind=engine
    )

    # Create a Session class instance
    session = Session()

    return session


def add_db_session_user_object(
    session: sqlalchemy.orm.Session,
    user_object: User
) -> sqlalchemy.orm.Session:
    """ Add User objects to an instance of the sqlalchemy.orm.Session.

        References:
            https://docs.sqlalchemy.org/en/14/orm/tutorial.html#adding-and-updating-objects

        Args:
            session (sqlalchemy.orm.Session):
                Instance of the Session class with an engine binding.

        Returns:
            session (sqlalchemy.orm.Session):
                Updated instance of the Session class with a User
                class in the format:
                    User(
                        name='Timothy',
                        fullname='Timothy Hull',
                        nickname='Tim'
                    )
    """

    # Add the User object to the session instance
    session.add(
        instance=user_object
    )

    # Display the in progress session details
    print(
        '"session.dirty" output:\n'
        f'{session.dirty}\n'
    )

    # Commit the changes to the database
    session.commit()  # Not necessary with sessionmaker autoflush set to True

    return session


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
    print(f'Database engine: "{engine}"\n')

    # Create database tables
    print('Creating database tables...')
    create_db_tables(engine)
    print()

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
        'User instance:\n'
        f'Name: {user_1.name}\n'
        f'Nickname: {user_1.nickname}\n'
        f'ID: {repr(user_1.id)}\n'
    )

    # Bind the Engine instance to a Session instance and display the Session
    session = config_session_db_engine(
        engine=engine
    )
    print(
        'SQLAlchemy Session object:\n'
        f'{repr(session)}\n'
    )

    # Add user information to the session instance and display the Session
    new_user = User(
                name='Timothy',
                fullname='Timothy Hull',
                nickname='Tim'
            )
    session = add_db_session_user_object(
        session=session,
        user_object=new_user
    )
    th = session.query(User).filter_by(name="Timothy").first()
    print(
        '\nNew user object returned by the database (th) is equal to the '
        '"new_user" object sent to the database: '
        f'{th is new_user}\n'
    )


if __name__ == '__main__':
    main()
