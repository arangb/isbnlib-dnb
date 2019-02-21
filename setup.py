# -*- coding: utf-8 -*-
# flake8: noqa
# isort:skip_file

# isbnlib-dnb -- an isbnlib plugin for the Deutsche National Bibliothek (Germany)
# Copyright (C) 2018  Aran Garcia-Bellido

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
from isbnlib_dnb import __version__

setup(
    name='isbnlib-dnb',
    version=__version__,
    author='arangb',
    author_email='arangbellido@gmail.com',
    url='https://github.com/arangb/isbnlib-dnb',
    download_url='https://github.com/arangb/isbnlib-dnb/archive/v0.0.3.zip',
    packages=['isbnlib_dnb/'],
    entry_points={'isbnlib.metadata': ['dnb=isbnlib_dnb:query']},
    install_requires=["isbnlib>=3.9.3,<3.10.0"],
    license='LGPL v3',
    description='A plugin for isbnlib that pulls metadata from the Deutsche National Bibliothek (Germany)',
    long_description=open('README.rst').read(),
    keywords='ISBN isbnlib dnb bibliographic-references',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'Topic :: Text Processing :: General',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    tests_require=['nose', 'coverage'],
    test_suite='nose.collector',
)
