#!/usr/bin/env python3
""" Tests for the bottle web/WSGI server.

    Documentation:
        http://bottlepy.org/docs/dev/

    PyPI:
        https://pypi.org/project/bottle/

    Installation:
        pip install bottle
"""

# Imports - Python Standard Library

# Imports - Third-Party
from bottle import Bottle, run

# Imports - Local

# Create Bottle object
app = Bottle()


# Hello world test function that listens on two paths (/ and /hello)
@app.route(
    path='/',
    method='GET'
)
@app.route(
    path='/hello',
    method='GET'
)
def hello_world() -> str:
    """ Display a hello world string.

        Args:
            None.

        Returns:
            display_string (str):
                String to display in a web browser.
    """

    # Set a string to display
    display_string = 'Hello World!'

    return display_string


# Dynamic route test function
@app.route(
    path='/hello/<name>',
    method='GET'
)
@app.route(
    path='/hello/<name>/',
    method='GET'
)
def hello_name(
    name: str
) -> None:
    """ Display a custom hello string.

        Args:
            name (str):
                Name value to display.

        Returns:
            display_string (str):
                String to display in a web browser.
    """

    # Set a string to display
    display_string = f'Hello {name.title()}'

    return display_string


# Dynamic route test function with two variables and .get instead of .route
@app.get(
    path='/hello/<first>/<last>'
)
@app.get(
    path='/hello/<first>/<last>/'
)
def hello_name_first_last(
    first: str,
    last: str
) -> None:
    """ Display a custom hello string.

        Args:
            first (str):
                First name value to display.

            Last (str):
                Last name value to display.

        Returns:
            display_string (str):
                String to display in a web browser.
    """

    # Set a string to display
    display_string = f'Hello {first.title()} {last.title()}'

    return display_string


# Call the run function to start the web service
run(
    app=app,
    host='web',
    port=8080,
    debug=True
)
