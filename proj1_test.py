#!/usr/bin/env python
"""Proj1 Grading Script

Note: Do not run this directly, it is called by proj1.py.
"""

import proj1_make_plate
import re
from utilities import *

digits = proj1_make_plate.readDataFile("../../tests/proj1/digits.dat")

def plate(rawSpec):
    spec = proj1_make_plate.parseSpec(rawSpec)
    return proj1_make_plate.makeBoard(16, 76, digits, spec)

def ddr(stdin):
    """Test project1.

    >>> ddr(plate("9 @ 2,1 -1"))  # Can it handle Step 1a?
    '9 @ 2,1 -1'
    >>> ddr(plate("8 @ 2,1 0 @ 2,8 0 @ 2,15 8 @ 2,22 5 @ 2,29 -1"))  # Can it handle Step 1c?
    '8 @ 2,1 0 @ 2,8 0 @ 2,15 8 @ 2,22 5 @ 2,29 -1'
    >>> ddr(plate("7 @ 2,1 9 @ 2,65 -1"))  # Can it handle Step 2?
    '7 @ 2,1 9 @ 2,65 -1'
    >>> ddr(plate("2 @ 9,1 5 @ 8,8 6 @ 7,15 0 @ 0,22 -1"))  # Can it handle Step 3?
    '2 @ 9,1 5 @ 8,8 6 @ 7,15 0 @ 0,22 -1'
    >>> ddr(plate("0 @ 0,0 0 @ 9,0 0 @ 0,71 0 @ 9,71 8 @ 4,35 -1"))  # Can it handle Step 4?
    '0 @ 0,0 0 @ 9,0 8 @ 4,35 0 @ 0,71 0 @ 9,71 -1'
    >>> ddr(plate("-1"))  # Can it handle an empty plate?
    '-1'
    >>> ddr(plate("1 @ 0,0 2 @ 8,0 3 @ 0,6 4 @ 8,6 5 @ 8,13 6 @ 0,14 -1"))  # Does it return numbers in the correct order?
    '1 @ 0,0 2 @ 8,0 3 @ 0,6 4 @ 8,6 5 @ 8,13 6 @ 0,14 -1'
    """
    (code, out, err) = testRun("./ddr", ["digits.dat"], "\n".join(stdin))
    return out.strip()


if __name__ == "__main__":
    import doctest
    (failureCount, testCount) = doctest.testmod()
    correctCount = testCount - failureCount
    print "Project 1 Total: %s / %s" % (correctCount, testCount)

