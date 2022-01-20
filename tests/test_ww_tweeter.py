#!/usr/bin/env pytest
""" Tests for ww_tweeter.py. """

# Imports - Python Standard Library
from datetime import datetime
from sys import path

# Imports - Third-Party
from _pytest.capture import CaptureFixture

# Imports - Local
# Set relative import path
path.append('/Users/hullt/Dropbox/code/personal/ww-tweeter')
from app.ww_tweeter import current_time

# Constants
DATE_PREFIX = 'The current date and time is'
NOW_DAY = datetime.now().day


# Initial code for Better Code Hub Analysis
def test_current_time(
    capsys: CaptureFixture
) -> None:
    """ Test the current_time function.

        Args:
            capsys (_pytest.captureCaptureFixture):
                pytest fixture to capture STDOUT output.

        Returns:
            None.
    """

    # Call the current_time function
    date_time = current_time()

    # Capture STDOUT output
    output = capsys.readouterr().out

    # Assert the return string matches the test string
    assert f'{DATE_PREFIX}' in date_time, \
           f'{NOW_DAY}' in date_time

    # Assert the STDOUT contains the test string
    assert f'{DATE_PREFIX}' in output, \
           f'{NOW_DAY}' in output
