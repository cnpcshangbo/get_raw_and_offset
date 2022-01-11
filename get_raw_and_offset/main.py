#!/usr/bin/env python
"""
here is a main function
"""
import os
import sys
from get_raw_and_offset import get_raw_and_offset

help = """
get_raw_and_offset script

get_raw_and_offset file_to_process [output_file_name]

get raw value from string
"""


def main():
    """
    startup function for running a capitalize as a script
    """
    try:
        infilename = sys.argv[1]
    except IndexError:
        print("you need to pass in a file name to process")
        print(help)
        sys.exit()
    try:
        outfilename = sys.argv[2]
    except IndexError:
        root, ext = os.path.splitext(infilename)
        outfilename = root + "_raw" + ext

    # do the real work:
    print("Get raw value from: %s and storing it in %s" % (infilename, outfilename))

    get_raw_and_offset.get_raw(infilename, outfilename)

    print("I'm done")
