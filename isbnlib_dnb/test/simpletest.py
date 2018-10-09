# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""Simple checks with a few examples. Just to see if it works."""

from .._dnb import query


def test_mcu():
    """Simple tests for some remarkable cases."""
    print(query('9783897215672'))
    print(query('9783658161408'))
    print(query('9783788804312'))



if __name__ == '__main__':
    test_mcu()
