#!/usr/bin/env python
"""HW3 Grading Script

Note: Do not run this directly, it is called by hw4.py.
"""

import re
from utilities import *

diagPromptsValidationRegex = r"(First string\?)\s*(Second string\?)\s*(Height\?)\s*(\S?.*)"

def diag(stdin):
    r"""Test diag.

    >>> diag('- X 7')[0]  # Does it print the correct prompts?
    'First string? \nSecond string? \nHeight? \n'
    >>> diag('- X 7')[1]  # Does it handle single characters?
    '------\nX-----\nXX----\nXXX---\nXXXX--\nXXXXX-\nXXXXXX'
    >>> diag('Batman NaNa 6')[1]  # Does it handle multi-character strings?
    'BatmanBatmanBatmanBatmanBatman\nNaNaBatmanBatmanBatmanBatman\nNaNaNaNaBatmanBatmanBatman\nNaNaNaNaNaNaBatmanBatman\nNaNaNaNaNaNaNaNaBatman\nNaNaNaNaNaNaNaNaNaNa'
    >>> diag('\\ / 5')[1]  # Does it handle backslashes?
    '\\\\\\\\\n/\\\\\\\n//\\\\\n///\\\n////'
    """
    out = testRun("./diag", [], stdin)[1].strip()
    match = re.match(diagPromptsValidationRegex, out)
    normalForm = "%s \n%s \n%s \n" % (match.group(1)
                                      , match.group(2)
                                      , match.group(3))
    return (normalForm, match.group(4)) if match else (out, out)
    # (first, second, height) = stdin.split()
    # height = int(height)
    # return 'First string? \nSecond string? \nHeight? \n' + "\n".join([second*i + first*(height-i-1) for i in range(height)])

mirrorPromptsValidationRegex = r"(Maximum value\?)\s*(\S?.*)"

def mirror(n):
    r"""Test mirror.

    >>> mirror(5)[0]  # Does it print the correct prompt?
    'Maximum value? \n'
    >>> mirror(5)[1]  # Does it handle reasonable numbers?
    '012345|543210\n012345|543210\n012345|543210\n012345|543210'
    >>> mirror(0)[1]  # Does it handle zero?
    '0|0\n0|0\n0|0\n0|0'
    >>> mirror(11)[1]  # Does it correctly not reverse the digits of numbers larger than 9?
    '01234567891011|11109876543210\n01234567891011|11109876543210\n01234567891011|11109876543210\n01234567891011|11109876543210'
    >>> mirror(100)[1]  # Does it handle less reasonable numbers?
    '0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100|1009998979695949392919089888786858483828180797877767574737271706968676665646362616059585756555453525150494847464544434241403938373635343332313029282726252423222120191817161514131211109876543210\n0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100|1009998979695949392919089888786858483828180797877767574737271706968676665646362616059585756555453525150494847464544434241403938373635343332313029282726252423222120191817161514131211109876543210\n0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100|1009998979695949392919089888786858483828180797877767574737271706968676665646362616059585756555453525150494847464544434241403938373635343332313029282726252423222120191817161514131211109876543210\n0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100|1009998979695949392919089888786858483828180797877767574737271706968676665646362616059585756555453525150494847464544434241403938373635343332313029282726252423222120191817161514131211109876543210'
    >>> mirror(-10)[1]  # Does it handle negative numbers?
    ''
    """
    out = testRun("./mirror", [], str(n))[1].strip()
    match = re.match(mirrorPromptsValidationRegex, out)
    return ("%s \n"%match.group(1), match.group(2)) if match else (out, out)
    # if n < 0:
    #     return ''
    # else:
    #     a = "".join(map(str, range(n+1)))
    #     z = "".join(map(str, range(n+1)[::-1]))
    #     # Somewhere Norman Ramsey is crying...
    #     return ('Maximum value? \n' + ("%s|%s\n" % (a, z)) * 4).strip()


if __name__ == "__main__":
    import doctest
    (failureCount, testCount) = doctest.testmod()
    correct = testCount - failureCount
    print "Assignment hw4 Total: %s / %s" % (correct, testCount)

