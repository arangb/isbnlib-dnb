# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""nose tests for metadata."""

from isbnlib import meta
from .._dnb import query


def test_query():
    """Test the query of metadata (dnb.de) with 'low level' queries."""
    assert (len(repr(query('9783897215672'))) > 100) == True
    assert (len(repr(query('9783658161408'))) > 100) == True
    assert (len(repr(query('9783788804312'))) > 100) == True

def test_query_missing():
    """Test DNB with 'low level' queries (missing data)."""
    assert (len(repr(query('9781849692341'))) <= 2) == True
    assert (len(repr(query('9781849692343'))) <= 2) == True

def test_query_wrong():
    """Test DNB with 'low level' queries (wrong data)."""
    assert (len(repr(query('9780000000'))) <= 2) == True
    
if __name__ == '__main__':
    test_query()
    test_query_missing()
    test_query_wrong()
