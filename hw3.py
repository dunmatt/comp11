#!/usr/bin/env python
"""HW3 Grading Script

Usage:
    ./hw3.py <dir> <files>...
"""
#TODO: double check the args to this script

import re
import sys
import unittest
from utilities import *

submission_filters = {
    "required": ["max3.cpp", "max3.data"
                 , "3wordsort.cpp", "3wordsort.data"
                 , "chkdate.cpp", "chkdate.data"]
    , "permitted": []
}

def testDataFile(tester, filename, regex):
    with open(filename) as f:
        tester.assertTrue(re.search(regex, f.read()))

def testAgainstFile(tester, filename, progname, lineRegex):
    with open(filename) as f:
        for line in f:
            match = re.match(lineRegex, line)
            self.assertEqual(run(progname, [], match.group(1))[1]
                             , match.group(2))
    

class TestMax3(unittest.TestCase):
    def test_data_file(self):
        testDataFile(self, "max3.data"
                     , r"(((?:-?\d*\.?\d+\s*){3}):\s*(-?\d*\.?\d+)\s+){4}")

    def test_against_data_in_file(self):
        testAgainstFile(self, "max3.data", "max3"
                        , r"^((?:-?\d*\.?\d+\s*){3}):\s*(-?\d*\.?\d+)\s+$")

    def test_corner_cases(self):
        self.assertEqual(run("max3", [], "4 2 3"[1]), "4")
        self.assertEqual(run("max3", [], "-5 -5 -5"[1]), "-5")
        self.assertEqual(run("max3", [], "-5.5 -5 -.5")[1], "-.5")
        self.assertEqual(run("max3", [], "-.000000001 0 -.000000001"[1]), "0")


class Test3WordSort(unittest.TestCase):
    def test_data_file(self):
        testDataFile(self, "3wordsort.data"
                     , r"(\S+\s+\S+\s+\S+\s*:\s*\S+\s+\S+\s+\S+\s*){4}")  # YES!

    def test_against_data_in_file(self):
        testAgainstFile(self, "3wordsort.data", "3wordsort"
                        , r"^(\S+\s+\S+\s+\S+)\s*:\s*(\S+\s+\S+\s+\S+)\s*$")

    def test_corner_cases(self):
        self.assertEqual(run("3wordsort", [], "aaa a aa")[1], "a aa aaa")
        self.assertEqual(run("3wordsort", [], "as is oz")[1], "as is oz")
        self.assertEqual(run("3wordsort", [], "4s 1s 0z")[1], "0z 1s 4s")
        self.assertEqual(run("3wordsort", [], "1 5 1000")[1], "1 1000 5")
        self.assertEqual(run("3wordsort", [], "0! a! !!")[1], "!! 0! a!")


class TestChkDate(unittest.TestCase):
    def test_data_file(self):
        testDataFile(self, "chkdate.data"
                     , r"(\d+\s+\d+\s+\d+\s*:\s*[YN]\s+){4}")

    def test_against_data_in_file(self):
        testAgainstFile(self, "chkdate.data", "chkdate"
                        , r"^(\d+\s+\d+\s+\d+)\s*:\s*([YN])\s*$")

    def test_corner_cases(self):
        self.assertEqual(run("chkdate", [], "12 13 1415")[1], "Y")
        self.assertEqual(run("chkdate", [], "1 1 1")[1], "Y")
        self.assertEqual(run("chkdate", [], "1 1 0")[1], "N")
        self.assertEqual(run("chkdate", [], "1 0 1")[1], "N")
        self.assertEqual(run("chkdate", [], "0 1 1")[1], "N")
        self.assertEqual(run("chkdate", [], "12 -1 9999")[1], "N")
        self.assertEqual(run("chkdate", [], "12 31 9999")[1], "Y")
        self.assertEqual(run("chkdate", [], "02 29 1900")[1], "N")
        self.assertEqual(run("chkdate", [], "02 29 2000")[1], "Y")
        self.assertEqual(run("chkdate", [], "02 29 2001")[1], "N")
        self.assertEqual(run("chkdate", [], "02 29 2004")[1], "Y")
        self.assertEqual(run("chkdate", [], "2 30 2000")[1], "N")
        self.assertEqual(run("chkdate", [], "2 3 1900")[1], "Y")


if __name__ == "__main__":
    from docopt import docopt
    arguments = docopt(__doc__, version="Tufts Comp11 HW3 v2014s")
    screenFilenames(arguments["<files>"], submission_filters)

    build("max3.cpp", "max3")
    build("3wordsort.cpp", "3wordsort")
    build("chkdate.cpp", "chkdate")

    unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__]).run()
