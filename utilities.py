#!/usr/bin/evn python
"""A group of utility functions to facilitate grading scripts.
"""

import fnmatch
import os
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

def screenHost(permitted_hosts):
    host = run("hostname")[1].strip()
    if host not in permitted_hosts:
        print "You cannot submit from this machine, try again from one of: %s" % ", ".join(host_filters)
        sys.exit(3)

def programCompiled(name):
    return os.path.exists(name)

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

def testRun(program, args=[], stdin=None):
    if programCompiled(program):
        return run(program, args, stdin)
    else:
        raise Exception("Cannot run %s since it did not compile..." % program)

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
    return (int(return_code), tempOut.read(), tempErr.read())

def readFile(filename):
    with open(filename) as f:
        return f.read()

def getScorecard(directory, assignment):
    me = run("whoami")[1].strip()
    return open("%s/scorecards/%s/%s" % (directory, assignment, me), mode="w+")

def getReport():
    if not os.path.exists("grading"):
        makeGrading()
    return open("grading/REPORT", mode="w+")

def makeGrading():
    os.makedirs("grading", "02770")  # magic 02770 here is file permissions
    run("chgrp", ["grade11", "grading"])
