#!/usr/bin/env python
"""HW3 Grading Script

Note: Do not run this directly, it is called by hw3.py.
"""

from utilities import *

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
    # return max(map(float, stdin.split()))
    return float(run("./max3", [], stdin)[1])

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
    # return " ".join(sorted(stdin.split()))
    return run("./3wordsort", [], stdin)[1]

chkdateDataValidationRegex = r"(\d+\s+\d+\s+\d+\s*:\s*[YN]\s+){4}"
chkdateLineRegex = r"^(\d+\s+\d+\s+\d+)\s*:\s*([YN])\s*$"
def dateCheck(str):
    (month, day, year) = map(int, str.split())
    if day < 1 or 31 < day or month < 1 or 12 < month or year < 1 or 9999 < year:
        return False
    if month == 2 and day == 29 and year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        return True
    if month == 2 and day >= 29:
        return False
    if day == 31 and month in [1, 3, 5, 7, 8, 10, 12]:
        return True
    if day == 31:
        return False
    return True

def chkDate(stdin):
    r"""Test chkdate.

    >>> grep("chkdate.data", chkdateDataValidationRegex) is not None  # Is the data file in the correct and long enough?
    True
    >>> all([chkDate(m.group(1)) == m.group(2) for m in lineMatchesIn("chkdate.data", chkdateLineRegex)])  # Do all of the examples in the data file work?
    True
    >>> chkDate("12 13 1415")  # Dec 13 1415?
    'Y'
    >>> chkDate("1 1 1")  # Jan 1 0001?
    'Y'
    >>> chkDate("1 1 0")  # Year zero?
    'N'
    >>> chkDate("1 0 1")  # Jan 0th?
    'N'
    >>> chkDate("0 1 1")  # Prebruary?
    'N'
    >>> chkDate("12 -1 9999")  # Dec negative 1?
    'N'
    >>> chkDate("12 31 9999")  # Dec 31 9999?
    'Y'
    >>> chkDate("11 31 9999")  # Nov 31 9999?
    'N'
    >>> chkDate("02 29 1900")  # Handles the 100 year leap year exception?
    'N'
    >>> chkDate("02 29 2000")  # Handles the 400 year exception to the 100 year exception?
    'Y'
    >>> chkDate("02 29 2001")  # Handles non-leap years?
    'N'
    >>> chkDate("02 29 2004")  # Handles normal leap years?
    'Y'
    >>> chkDate("2 30 2000")   # Works without padding?  And also there is no Feb 30th...
    'N'
    """
    # return "Y" if dateCheck(stdin) else "N"
    return run("./chkdate", [], stdin)[1].strip()

if __name__ == "__main__":
    import doctest
    (failureCount, testCount) = doctest.testmod()
    print "You got %s / %s" % (testCount - failureCount, testCount)
