#!/usr/bin/env python
"""Project 1 Grading Script

Usage:
    ./proj1.py <dir> <files>...
"""

from utilities import *

submission_filters = {
    "required": ["ddr.cpp"]
    , "permitted": ["ddrlib.cpp", "ddrlib.h"]
}

# submission_host_filters = ["dell24"]

if __name__ == "__main__":
    from docopt import docopt
    arguments = docopt(__doc__, version="Tufts Comp11 Project1 v2014s")
    # screenHost(submission_host_filters)
    screenUname(".el6")
    screenGxx((4, 8, 0))  # this means g++ >= 4.8.0
    screenFilenames(arguments["<files>"], submission_filters)
    run("cp", ["../../tests/proj1/ddrlib.h", "."])
    run("cp", ["../../tests/proj1/ddrlib.cpp", "."])
    (code0, _, err0) = build(["ddr.cpp", "ddrlib.cpp"], "ddr")

    # create thing called testhw5 so that t will work
    with getReport() as f:
        (return_code, stdout, stderr) = run("python", ["../../tests/proj1/proj1_test.py"])
        f.write(stdout)
        print stdout

        if code0:
            print "Here are the errors generated by the compiler:"
            print err0
            print "Your code did not build!"
            f.write("Here are the errors generated by the compiler:\n")
            f.write(err0)
            f.write("Your code did not build!\n")


