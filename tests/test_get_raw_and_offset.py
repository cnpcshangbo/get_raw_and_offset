#!/usr/bin/env python

"""
test code for capitalize module

can be run with py.test
"""

import os
from pathlib import Path

import pytest

from get_raw_and_offset import get_raw_and_offset

# fixture that creates and removes a file with some test lines in it.
@pytest.fixture(scope='module')
def test_file_path():
    """
    Fixture to generate a file with some sample data in it
    """
    # A couple words for the file
    temp_path = Path("input_test_file.txt")
    with open(temp_path, 'w') as outfile:
        outfile.write("""This is a really simple Text file.
It is here so that I can test the capitalize script.

And that's only there to try out packaging.

So there.
""")
    # the file wil be created and filled, then the path passed on
    yield temp_path
    # at "teardown", the file will be removed
    os.remove(temp_path)


def test_capitalize_line():
    special = {'is', 'a', 'to'}
    line =     "D_Pos 9314 / Raw -4.233928 / offs 4.200000 /"
    expected = "-4.233928"

    result = get_raw_and_offset.get_raw_line(line)
    assert  result == expected
