#!/usr/bin/env pytest
""" Tests for db/db.py. """

# Imports - Python Standard Library

# Imports - Third-Party

# Imports - Local
from app.db.db import (
    _create_session, truncate_tables, get_hashtags, add_hashtags,
    get_tweets, add_tweets
)

# Constants

# Test functions
