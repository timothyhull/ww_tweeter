#!/usr/bin/env python3
""" Tests for collections.Counter.

    Determine the function of the Counter object when used for
    inserting hashtags into the database.
"""

# Imports - Python Standard Library
from collections import Counter

# Imports - Local
from app.db.db import VALID_HASHTAG
from app.tweeter.tweeter import (
    twitter_api_auth, get_top_n_tweets
)

# Authenticate to Twitter
auth = twitter_api_auth()

# Get the top N tweets
tweets = get_top_n_tweets(auth)

# Create a space separated string of all tweet text
tweet_text = ' '.join(tweet.text.lower() for tweet in tweets)

# Create a Counter object for hashtags
hashtag_counter = Counter(VALID_HASHTAG.findall(tweet_text))
