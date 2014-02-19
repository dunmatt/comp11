#!/usr/bin/env python
"""HW5 Grading Script

Note: Do not run this directly, it is called by hw4.py.
"""

import re
from utilities import *


def read_years(stdin):
    r"""Test read_years.

    >>> read_years('4 5 6 -1')[0]  # Does it normally return success?
    0
    >>> read_years('4 5 6 -1')[1]  # Does it correctly compute integer averages?
    5
    >>> read_years('-100 5 100 -1')[1]  # Does it correctly handle negative numbers?
    5
    >>> read_years('5 10 -1')[1]  # Does it correctly compute floating point averages?
    7.5
    >>> read_years(' '.join(range(999)+[-1]))[1]  # Does it correctly handle large inputs?
    499
    >>> read_years(' '.join(range(1000)+[-1]))[0]  # Does it use the proper return code when too much input is supplied?
    1
    >>> read_years(' '.join(range(1000)+[-1]))[2]  # Does it print the right error when too much input is supplied?
    'too much input'
    """
    (code, out, err) = testRun("./read_years", [], stdin)
    return (int(code), float(out.strip()), err.strip())

def over_avg(stdin):
    r"""Test over_avg.

    >>> over_avg('0')[0]  # Does it normally return success?
    0
    >>> over_avg('0')[1]  # Does it correctly do nothing on sentinel?
    0
    >>> over_avg('1 1 -1 1 1000 0')[1]  # Does it seem to work?
    1
    >>> over_avg('1000 1000 -1000 1000 4 0')[1]  # Does it seem to work?
    3
    >>> over_avg('5 ' * 30000 + '0')[1]  # Does it handle huge inputs?
    5
    >>> over_avg('5 ' * 30001 + '0')[0]  # Does it use the proper return code when the input is too big
    1
    >>> over_avg('5 ' * 30001 + '0')[2]  # Does it print the right error when too much input is supplied?
    'too much input'
    """
    (code, out, err) = testRun("./over_avg", [], stdin)
    return (int(code), float(out.strip()), err.strip())

if __name__ == "__main__":
    import doctest
    (failureCount, testCount) = doctest.testmod()
    correctCount = testCount - failureCount
    print "Assignment hw5 Total: %s / %s" % (correctCount, testCount)

