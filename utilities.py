#!/usr/bin/evn python
"""A group of utility functions to facilitate grading scripts.
"""

import fnmatch
import re
import subprocess
import sys
from tempfile import TemporaryFile

def screenFilenames(filenames, submission_filters):
    fs = set(filenames)
    rs = set(submission_filters["required"])
    missing = rs - fs
    if missing:
        print "Could not find the files: %s" % ", ".join(missing)
        sys.exit(1)

    def isPermitted(filename):
        for filtr in submission_filters["permitted"]:
            if fnmatch.fnmatch(filename, filtr):
                return True
        return False
    unaccounted_for = fs - rs
    not_permitted = [f for f in unaccounted_for if not isPermitted(f)]
    if not_permitted:
        print "Unrecognized filenames: %s" % ", ".join(not_permitted)
        sys.exit(2)

def grep(filename, regex):
    with open(filename) as f:
        return re.search(regex, f.read())

def lineMatchesIn(filename, regex):
    with open(filename) as f:
        for line in f:
            match = re.match(regex, line)
            if match:
                yield match

def build(sources, binary):
    return run("g++", ["-Wall", "-Wextra"] + sources + ["-o", binary])

def run(program, args=[], stdin=None):
    tempIn = TemporaryFile(mode="w+")
    if stdin:
        tempIn.write(stdin)
        tempIn.seek(0)
    tempOut = TemporaryFile(mode="w+")
    tempErr = TemporaryFile(mode="w+")
    cmd = [program] + args
    return_code = subprocess.call(cmd
                                  , stdin=tempIn
                                  , stdout=tempOut
                                  , stderr=tempErr)
    tempOut.seek(0)
    tempErr.seek(0)
    return (return_code, tempOut.read(), tempErr.read())

def getScorecard(directory, assignment):
    me = run("whoami")[1].strip()
    return open("%s/scorecards/%s/%s" % (directory, assignment, me), mode="w+")
