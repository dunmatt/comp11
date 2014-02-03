#!/usr/bin/evn python
"""A group of utility functions to facilitate grading scripts.
"""

import fnmatch
import sys

def screenFilenames(filenames, submission_filters):
    fs = set(filenames)
    rs = set(submission_filters["required"])
    missing = rs - fs
    if missing:
        print "Could not find the files: %s" % ", ".join(missing)
        sys.exit(1)

    def isPermitted(filename):
        for filt in submission_filters["permitted"]:
            if fnmatch.fnmatch(filename, filt):
                return True
        return False
    unaccounted_for = fs - rs
    not_permitted = [f for f in unaccounted_for if not isPermitted(f)]
    if not_permitted:
        print "Unrecognized filenames: %s" % ", ".join(not_permitted)
        sys.exit(2)




