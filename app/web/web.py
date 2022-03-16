#!/usr/bin/env python3
""" Twitter analyzer web view for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library
from os.path import dirname, join
from pathlib import Path
from typing import Dict, Union

# Imports - Third-Party
from bottle import (
    Bottle, HTTPError, HTTPResponse, run, static_file,
    TEMPLATE_PATH, view
)

# Imports - Local
from app.db import db

# Constants
APP_DEBUG = True
APP_HOST = 'web'
APP_PATH = Path(dirname(__file__))
APP_PORT = 8080
APP_RELOADER = True
APP_STATIC_DIR = 'static'
APP_STATIC_PATH = join(APP_PATH, APP_STATIC_DIR)
APP_VIEW_DIR = 'views'
APP_VIEW_PATH = join(APP_PATH, APP_VIEW_DIR)

# Create a bottle object
app = Bottle()


# Setup path to static files
# Reference: https://bottlepy.org/docs/dev/tutorial.html#static-files
@app.route(path='/static/<filename:path>')
def send_static(
    filename: str
) -> Union[HTTPError, HTTPResponse]:
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
        root=APP_STATIC_PATH
    )

    return static_file_path


# Set a path to bottle view templates
TEMPLATE_PATH.insert(0, APP_VIEW_PATH)


# Function for HTTP request routing
@app.get(path='/')
@app.get(path='/<filter>')
@app.get(path='/<filter>/')
@view(tpl_name='index')
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

    # Get tweets from the database, use a filter if present
    if filter is not None:
        filter = f'#{filter}'

    tweets = db.get_tweets(
        search_tag=filter
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
    # tweets_hashtags = str(
    #     f"Tweet count: {len(tweets_hashtags.get('tweets'))}"
    # )

    return tweets_hashtags


# Run the bottle service
run(
    app=app,
    host=APP_HOST,
    port=APP_PORT,
    debug=APP_DEBUG,
    reloader=APP_RELOADER
)
