#!/usr/bin/env python3
""" SQLAlchemy Object Relational Tutorial (1.x API).

    Code to support the SQLAlchemy tutorial at:
    https://docs.sqlalchemy.org/en/14/orm/tutorial.html
"""

# Imports - Python Standard Library

# Imports - Third-Party
import sqlalchemy

# Imports - Local

# Constants


def sqlalchemy_version() -> str:
    """ Display the SQLAlchemy version.

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
        f'* {version_str}* \n'
        f'{header_str}\n'
    )

    return version


def main() -> None:
    """ Main program.

        Args:
            None.

        Returns:
            None.
    """

    # Display SQLAlchemy version
    print(sqlalchemy_version())


if __name__ == '__main__':
    main()
