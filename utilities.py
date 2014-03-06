#!/usr/bin/evn python
"""A group of utility functions to facilitate grading scripts.
"""

import fnmatch
import os
import re
from subprocess import Popen, PIPE
import sys
from threading import Timer

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
        print "You cannot submit from this machine, try again from one of: %s" % ", ".join(permitted_hosts)
        sys.exit(3)

def screenUname(versionSubstring):
    if versionSubstring not in run("uname", ["-a"])[1]:
        print "The version of linux you are submitting from is too old, try logging into homework.cs.tufts.edu to provide!"
        sys.exit(4)

def screenGxx(minimumVersion):
    versionRaw = run("g++", ["--version"])[0]
    match = re.search(r"g\++\D+(\d+)\.(\d+)\.(\d+).*", versionRaw, flags=re.S)
    version = (int(match.group(1)), int(match.group(2)), int(match.group(3)))
    if version < minimumVersion:
        print "The version of G++ on your machine is too old, try logging into homework.cs.tufts.edu to provide!"
        sys.exit(5)

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

def testRun(program, args=[], stdin="", timeout=3):
    if programCompiled(program):
        return run(program, args, stdin, timeout)
    else:
        raise Exception("Cannot run %s since it did not compile..." % program)

def run(program, args=[], stdin="", timeout=60):
    p = Popen([program] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    p.stdin.write(stdin)
    def killProcess():
        if p.poll() == None:
            try:
                p.kill()
                print "Killing %s because it took longer than %ss on input %s" % (program, timeout, stdin)
            except:
                pass
    timer = Timer(timeout, killProcess)
    timer.start()
    p.wait()
    timer.cancel()
    return (int(p.returncode), p.stdout.read(), p.stderr.read())

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
    os.makedirs("grading", 02770)  # magic 02770 here is file permissions
    run("chgrp", ["grade11", "grading"])
