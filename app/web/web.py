#!/usr/bin/env python3
""" Twitter analyzer web view for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library
from typing import Dict

# Imports - Third-Party
from bottle import Bottle, run

# Imports - Local
from app.db import db

# Constants
APP_DEBUG = True
APP_HOST = 'web'
APP_PORT = 8080

# Create a bottle object
app = Bottle()


# Function for HTTP request routing
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

    # Get tweets from the database
    tweets = db.get_tweets(
        search_tag=f'#{filter}'
    )

    # Get hashtags from the database
    hashtags = db.get_hashtags()

    tweets_hashtags = {
        'filter': filter,
        'tweets': tweets,
        'hashtags': hashtags
    }

    tweets_hashtags = str(f"Tweet count: {len(tweets_hashtags.get('tweets'))}")

    return tweets_hashtags


# Run the bottle service
run(
    app=app,
    host=APP_HOST,
    port=APP_PORT,
    debug=APP_DEBUG
)
