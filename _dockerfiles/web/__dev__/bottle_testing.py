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

# Create a route object
app = Bottle()


# Hello world test function
@app.route('/')
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


# Call the run function to start the web service
run(
    host='0.0.0.0',
    port=8080,
    debug=True
)
