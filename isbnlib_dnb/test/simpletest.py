# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""Simple checks with a few examples. Just to see if it works.
To run: python3 -m isbnlib_mcues.test.simpletest   # no .py at the end"""

from .._dnb import query


def test_dnb():
    """Simple tests for some remarkable cases."""
    #print(query('9783897215672'))
    print(query('9783658161408'))
    #print(query('9783788804312'))
    #print(query('9783437583032'))
    #print(query('365816140X'))
    #print(query('978-3-9818084-4-5')) # two languages


if __name__ == '__main__':
    test_dnb()
