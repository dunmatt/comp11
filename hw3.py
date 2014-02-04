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

def m3(str):
    return max(map(lambda s: float(s), str.split()))

def s3(str):
    return sorted(str.split())

max3DataValidationRegex = r"(((?:-?\d*\.?\d+\s*){3}):\s*(-?\d*\.?\d+)\s*){4}"
max3LineRegex = r"^((?:-?\d*\.?\d+\s*){3}):\s*(-?\d*\.?\d+)\s+$"
twsDataValidationRegex = r"(\S+\s+\S+\s+\S+\s*:\s*\S+\s+\S+\s+\S+\s*){4}"
twsLineRegex = r"^(\S+\s+\S+\s+\S+)\s*:\s*(\S+\s+\S+\s+\S+)\s*$"

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
    return float(run("max3", [], stdin)[1])

def threeWordSort(stdin):
    r"""Test 3wordsort.
    """
    pass
    # run("3wordsort", [], stdin)[1]

# class Test3WordSort(unittest.TestCase):
#     def test_data_file(self):
#         testDataFile(self, "3wordsort.data"
#                      , )  # YES!

#     def test_against_data_in_file(self):
#         testAgainstFile(self, "3wordsort.data", "3wordsort"
#                         , )

#     def test_corner_cases(self):
#         self.assertEqual(run("3wordsort", [], "aaa a aa")[1], "a aa aaa")
#         self.assertEqual(run("3wordsort", [], "as is oz")[1], "as is oz")
#         self.assertEqual(run("3wordsort", [], "4s 1s 0z")[1], "0z 1s 4s")
#         self.assertEqual(run("3wordsort", [], "1 5 1000")[1], "1 1000 5")
#         self.assertEqual(run("3wordsort", [], "0! a! !!")[1], "!! 0! a!")


# class TestChkDate(unittest.TestCase):
#     def test_data_file(self):
#         testDataFile(self, "chkdate.data"
#                      , r"(\d+\s+\d+\s+\d+\s*:\s*[YN]\s+){4}")

#     def test_against_data_in_file(self):
#         testAgainstFile(self, "chkdate.data", "chkdate"
#                         , r"^(\d+\s+\d+\s+\d+)\s*:\s*([YN])\s*$")

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
