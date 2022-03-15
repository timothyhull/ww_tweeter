#!/usr/bin/env python3
""" Twitter analyzer web view for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library
from typing import Dict, Union

# Imports - Third-Party
from bottle import (
    Bottle, HTTPError, HTTPResponse, route, run, static_file
)

# Imports - Local
from app.db import db


# Setup path to static files
# Reference: https://bottlepy.org/docs/dev/tutorial.html#static-files
@route('/static/<filename:path>')
def send_static(filename: str) -> Union[HTTPError, HTTPResponse]:
    """ WW-Tweeter static file route.

        Args:
            filename (str):
                Static file name to load.

        Returns:
            static_file_path (Union[HTTPError, HTTPResponse]):
                HTTP Response or HTTP error object.
    """

    static_file_path = static_file(
        filename=filename,
        root='static'
    )

    return static_file_path


# Constants
APP_DEBUG = True
APP_HOST = 'web'
APP_PORT = 8080
APP_RELOADER = True

# Create a bottle object
app = Bottle()


# Function for HTTP request routing
@app.get(path='/')
@app.get(path='/<filter>')
@app.get(path='/<filter>/')
def index(
    filter: str = None
) -> Dict:
    """ WW-Tweeter web view route.

        Args:
            filter (str, optional):
                Keyword filter for search.

        Returns:
            tweets_hashtags (Dict):
                Dict of tweet and hashtag data.
    """

    # Get tweets from the database
    tweets = db.get_tweets(
        search_tag=f'#{filter}'
    )

    # Get hashtags from the database
    hashtags = db.get_hashtags()

    # Create response dictionary object
    tweets_hashtags = {
        'filter': filter,
        'tweets': tweets,
        'hashtags': hashtags
    }

    # Temporary return string value for testing
    '''
    tweets_hashtags = str(
        f"Tweet count: {len(tweets_hashtags.get('tweets'))}"
    )
    '''

    return tweets_hashtags


# Run the bottle service
run(
    app=app,
    host=APP_HOST,
    port=APP_PORT,
    debug=APP_DEBUG,
    reloader=APP_RELOADER
)
