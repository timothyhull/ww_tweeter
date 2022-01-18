#!/usr/bin/env python3
""" Twitter analyzer for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library
from datetime import datetime

# Imports - Third-Party

# Imports - Local


# Initial code for Better Code Hub Analysis
def current_time() -> str:
    """ Display the current date and time.
    
        Args:
            None.

        Returns:
            date_time (str):
                String of the current date and time.
    """

    # Get a datetime object for now
    now = datetime.now()

    date_time = f'\nThe current date and time is {now.ctime()}\n'

    return date_time


def main() -> None:
    """ Main program.
    
        Args:
            None.

        Returns:
            None.
    """

    print(current_time())

    return None


if __name__ == '__main__':
    main()
