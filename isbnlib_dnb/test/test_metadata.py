# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""nose tests for metadata."""

from nose.tools import assert_equals
from isbnlib import meta
from .._dnb import query


def test_query():
    """Test the query of metadata (dnb.de) with 'low level' queries."""
    assert_equals(len(repr(query('9781849692341'))) == 2, True)
    assert_equals(len(repr(query('9781849692343'))) == 2, True)

    assert_equals(len(repr(query('9788491043508'))) > 100, True)
    assert_equals(len(repr(query('9788437604947'))) > 100, True)
    assert_equals(len(repr(query('9788474234046'))) > 100, True)

    assert_equals(len(repr(query('9780000000'))) == 2, True)
