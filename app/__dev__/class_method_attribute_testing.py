#!/usr/bin/env python3
""" Tests for adding attributes with methods to class methods.

    The intent is to return two objects:
        test_method_1().name
        test_method_1().url.test_method_2()
"""


# Define a url class for the test method
class URL:

    # Define test method #2
    def test_method_2(self, url):

        # Return a string of the url parameter
        return str(url)


# Class objects
class Test:

    # Define test method #1
    def test_method(self):

        # Return the test method as an object, not a function call
        return self.test_method

    # Add the name attribute to the test method
    test_method.name = 'test_name'

    # Add the url attribute to the test method, instantiating the URL class
    test_method.url = URL()
