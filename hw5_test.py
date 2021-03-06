#!/usr/bin/env python
"""HW5 Grading Script

Note: Do not run this directly, it is called by hw4.py.
"""

import re
from utilities import *

grabAverageRegex = r""".*?avg\s=\s(-?\d*\.?\d+)"""

def read_years(stdin):
    r"""Test read_years.

    >>> read_years('4 5 6 -1')[0]  # Does it normally return success?
    0
    >>> read_years('4 5 6 -1')[1]  # Does it correctly compute integer averages?
    5.0
    >>> read_years('-100 6 100 -1')[1]  # Does it correctly handle negative numbers?
    2.0
    >>> read_years('5 10 -1')[1]  # Does it correctly compute floating point averages?
    7.5
    >>> read_years(' '.join(map(str, range(999)+[-1])))[1]  # Does it correctly handle large inputs?
    499.0
    >>> read_years(' '.join(map(str, range(1000)+[-1])))[0]  # Does it use the proper return code when too much input is supplied?
    1
    >>> read_years(' '.join(map(str, range(1000)+[-1])))[2]  # Does it print the right error message when too much input is supplied?
    'too much input'
    """
    (code, out, err) = testRun("./read_years", [], stdin)
    match = re.match(grabAverageRegex, out, flags=re.S)
    return (code, float(match.group(1)) if match else out + "\n" + err, err.strip())

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
    0
    >>> over_avg('5 ' * 30001 + '0')[0]  # Does it use the proper return code when the input is too big?
    1
    >>> over_avg('5 ' * 30001 + '0')[2]  # Does it print the right error message when too much input is supplied?
    'too much input'
    """
    (code, out, err) = testRun("./over_avg", [], stdin)
    return (code, int(out.strip()) if re.match(r"\d+$", out.strip()) else out, err.strip())

allData = readFile('../../tests/hw5/all')
grabAvgAgeParts = r"""(Enter a name:\s|\D{0,14})\n?(average age = \d*\.?\d+|name not found|.*)\s*"""
def avg_age(stdin):
    r"""Test avg_age.

    >>> avg_age('1992 Ann\n1993 Bob\n1994 Ann\n1991 Bob\n-1 DONE\nAnn')[0]  # Does it normally return success?
    0
    >>> avg_age('1992 Ann\n1993 Bob\n1994 Ann\n1991 Bob\n-1 DONE\nAnn')[1][0]  # Does it print the correct prompt?
    'Enter a name: '
    >>> avg_age('1992 Ann\n1993 Bob\n1994 Ann\n1991 Bob\n-1 DONE\nAnn')[1][1][:16]  # Does it work on a simple case?
    'average age = 21'
    >>> avg_age(allData + 'Xayrined\n')[1][1][:16]  # Does it work on singleton names in all?
    'average age = 26'
    >>> avg_age(allData + 'Mary\n')[1][1][:19]  # Does it work on popular names in all?
    'average age = 61.48'
    >>> avg_age(allData + 'Zaphod\n')[1][1]  # Does it have the right error messages for people that don't appear?
    'name not found'
    >>> avg_age(allData + 'DONE\n')[1][1]  # Does it correctly not report an age for the sentinel?
    'name not found'
    >>> avg_age('1970 Unix\n' * 50001 + '-1 DONE')[0]  # Does it use the proper return code when the input is too big?
    1
    >>> avg_age('1970 Unix\n' * 50001 + '-1 DONE')[2]  # Does it print the right error message when too much input is supplied?
    'too much data'
    """
    (code, out, err) = testRun("./avg_age", [], stdin)
    match = re.match(grabAvgAgeParts, out, flags=re.S)
    parts = (match.group(1), match.group(2).strip()) if match else (out, out)
    return (code, parts, err.strip())
    # from collections import defaultdict
    # d = defaultdict(list)
    # lines = stdin.strip().split("\n")
    # for line in lines[:-1]:
    #     [year, name] = line.split()
    #     d[name].append(2014 - float(year))
    # query = lines[-1]
    # if d.has_key(query):
    #     return (0, 'average age = %s' % (sum(d[query])/len(d[query])), None)
    # else:
    #     return (0, 'name not found', None)

if __name__ == "__main__":
    import doctest
    (failureCount, testCount) = doctest.testmod()
    correctCount = testCount - failureCount
    print "Assignment 5 Total: %s / %s" % (correctCount, testCount)

