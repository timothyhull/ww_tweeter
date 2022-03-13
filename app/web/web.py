#!/usr/bin/env python3
""" Twitter analyzer web view for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library
from typing import Dict

# Imports - Third-Party
from bottle import Bottle, run

# Imports - Local

# Constants
APP_DEBUG = True
APP_HOST = 'web'
APP_PORT = 8080

# Create a bottle object
app = Bottle()


# Function for HTTP requests
@app.get(path='/')
@app.get(path='/<filter>')
@app.get(path='/<filter>/')
def tweeter_view(
    filter: str = None
) -> Dict:
    """ WW-Tweeter web view route.

        Args:
            filter (str, optional):
                Keword filter for search.

        Returns:
            tweets_hashtags (Dict):
                Dict of tweet and hashtag data.
    """

    # Test strings
    if filter:
        output = (
            f'Filter is "{filter}"'
        )
    else:
        output = 'No filter supplied'

    return output


# Run the bottle service
run(
    app=app,
    host=APP_HOST,
    port=APP_PORT,
    debug=APP_DEBUG
)
