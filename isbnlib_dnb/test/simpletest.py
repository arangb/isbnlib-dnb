# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""Simple checks with a few examples. Just to see if it works."""

from nose.tools import assert_equals
import isbnlib
from .._dnb import query
#from _dnb import query

def test_mcu():
    """Simple tests for some remarkable cases."""
    print(query('9783899419979')) # Nora Roberts
    print(query('9783881006224')) # Children's book 
    print(query('9783551354044')) # Harry potter

    #for i in ['9783498030438', '9783981929959', '9783864930614']:
    #    print(query(i))

#test_mcu()
