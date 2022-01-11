#!/usr/bin/env python
"""Main module."""


def get_raw_line(instr):
    words = instr.split()
    # if len(words) > 3:

    # else:
    #     raw = 0

    return words[4]


def get_raw(infilename, outfilename):
    """
    reads the contents of infilename, and writes it to outfilename, but with
    every word capitalized

    note: very primitive -- it will mess some files up!

    this is called by the capitalize script

    :param infilename: The file name you want to process
    :type infilename: string

    :param outfilename: the name of the new file that will be created
    :type outfilename: string

    :returns: None

    :raises: IOError if infilename doesn't exist.
    """
    infile = open(infilename, 'U')
    outfile = open(outfilename, 'w')

    for line in infile:
        if len(line) > 3:
            outfile.write(get_raw_line(line))
            outfile.write("\n")

    return None
