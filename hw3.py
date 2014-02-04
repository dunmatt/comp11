#!/usr/bin/env python
"""HW3 Grading Script

Usage:
    ./hw3.py <dir> <files>...
"""
#TODO: double check the args to this script

import re
from utilities import *

submission_filters = {
    "required": ["max3.cpp", "max3.data"
                 , "3wordsort.cpp", "3wordsort.data"
                 , "chkdate.cpp", "chkdate.data"]
    , "permitted": []
}

max3DataValidationRegex = r"(((?:-?\d*\.?\d+\s*){3}):\s*(-?\d*\.?\d+)\s*){4}"
max3LineRegex = r"^((?:-?\d*\.?\d+\s*){3}):\s*(-?\d*\.?\d+)\s+$"

def max3(stdin):
    r"""Test max3.

    >>> grep("max3.data", max3DataValidationRegex) is not None  # Is the data file in the correct format and long enough?
    True
    >>> all([max3(m.group(1)) == float(m.group(2)) for m in lineMatchesIn("max3.data", max3LineRegex)])  # Do all of the examples in the data file work?
    True
    >>> max3("4 2 3") == 4  # Does the simple case work?
    True
    >>> max3("-5 -5 -5") == -5  # Does it handle getting all the same input gracefully?
    True
    >>> max3("-5.5 -5 -.5") == -.5  # Does it handle negatives and fractions correctly?
    True
    >>> max3(".000000001 0 -.000000001") == .000000001  # Does it handle tiny fractions correctly?
    True
    """
    return max(map(lambda s: float(s), stdin.split()))
    # return float(run("max3", [], stdin)[1])

twsDataValidationRegex = r"(\S+\s+\S+\s+\S+\s*:\s*\S+\s+\S+\s+\S+\s*){4}"
twsLineRegex = r"^(\S+\s+\S+\s+\S+)\s*:\s*(\S+\s+\S+\s+\S+)\s*$"

def threeWordSort(stdin):
    r"""Test 3wordsort.

    >>> grep("3wordsort.data", twsDataValidationRegex) is not None  # Is the data file in the correct and long enough?
    True
    >>> all([threeWordSort(m.group(1)) == m.group(2) for m in lineMatchesIn("3wordsort.data", twsLineRegex)])  # Do all of the examples in the data file work?
    True
    >>> threeWordSort("a a a") == "a a a"  # Does it work when all inputs are the same?
    True
    >>> threeWordSort("aaa a aa") == "a aa aaa"  # Does it correctly use length to break ties?
    True
    >>> threeWordSort("as is oz") == "as is oz"  # Does it leave already sorted words alone?
    True
    >>> threeWordSort("4s 1s 0z") == "0z 1s 4s"  # Does it work with alphanumeric strings?
    True
    >>> threeWordSort("1 5 1000") == "1 1000 5"  # Does it sort numbers lexically instead of numerically?
    True
    >>> threeWordSort("0! a! !!") == "!! 0! a!"  # Does it sort mixed types correctly?
    True
    """
    return " ".join(sorted(stdin.split()))
    # return run("3wordsort", [], stdin)[1]

chkdateDataValidationRegex = r"(\d+\s+\d+\s+\d+\s*:\s*[YN]\s+){4}"
chkdateLineRegex = r"^(\d+\s+\d+\s+\d+)\s*:\s*([YN])\s*$"

def chkDate(stdin):
    r"""Test chkdate.

    >>> grep("chkdate.data", chkdateDataValidationRegex) is not None  # Is the data file in the correct and long enough?
    True
    >>> all([chkDate(m.group(1)) == m.group(2) for m in lineMatchesIn("chkdate.data", chkdateLineRegex)])  # Do all of the examples in the data file work?
    True
    """
    return False
    return run("chkdate", [], stdin)

# class TestChkDate(unittest.TestCase):
#     def test_data_file(self):
#         testDataFile(self, "chkdate.data"

#     def test_against_data_in_file(self):
#         testAgainstFile(self, "chkdate.data", "chkdate"

#     def test_corner_cases(self):
#         self.assertEqual(run("chkdate", [], "12 13 1415")[1], "Y")
#         self.assertEqual(run("chkdate", [], "1 1 1")[1], "Y")
#         self.assertEqual(run("chkdate", [], "1 1 0")[1], "N")
#         self.assertEqual(run("chkdate", [], "1 0 1")[1], "N")
#         self.assertEqual(run("chkdate", [], "0 1 1")[1], "N")
#         self.assertEqual(run("chkdate", [], "12 -1 9999")[1], "N")
#         self.assertEqual(run("chkdate", [], "12 31 9999")[1], "Y")
#         self.assertEqual(run("chkdate", [], "02 29 1900")[1], "N")
#         self.assertEqual(run("chkdate", [], "02 29 2000")[1], "Y")
#         self.assertEqual(run("chkdate", [], "02 29 2001")[1], "N")
#         self.assertEqual(run("chkdate", [], "02 29 2004")[1], "Y")
#         self.assertEqual(run("chkdate", [], "2 30 2000")[1], "N")
#         self.assertEqual(run("chkdate", [], "2 3 1900")[1], "Y")


if __name__ == "__main__":
    from docopt import docopt
    arguments = docopt(__doc__, version="Tufts Comp11 HW3 v2014s")
    # screenFilenames(arguments["<files>"], submission_filters)

    # build("max3.cpp", "max3")
    # build("3wordsort.cpp", "3wordsort")
    # build("chkdate.cpp", "chkdate")

    import doctest
    doctest.testmod()
