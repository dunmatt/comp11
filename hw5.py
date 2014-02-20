#!/usr/bin/env python
"""HW5 Grading Script

Usage:
    ./hw5.py <dir> <files>...
"""

from utilities import *

submission_filters = {
    "required": ["read_years.cpp", "over_avg.cpp", "5-3.txt", "avg_age.cpp"]
    , "permitted": []
}

submission_host_filters = ["dell24"]

if __name__ == "__main__":
    from docopt import docopt
    arguments = docopt(__doc__, version="Tufts Comp11 HW5 v2014s")
    screenHost(submission_host_filters)
    screenFilenames(arguments["<files>"], submission_filters)

    (code0, _, err0) = build(["read_years.cpp"], "read_years")
    (code1, _, err1) = build(["over_avg.cpp"], "over_avg")
    (code2, _, err2) = build(["avg_age.cpp"], "avg_age")

    with getScorecard(arguments["<dir>"], "hw5") as f:
        (return_code, stdout, stderr) = run("../../tests/hw5/hw5_test.py")
        f.write(stdout)
        print stdout

        if code0 or code1 or code2:
            print "Here are the errors generated by the compiler:"
            print err0
            print err1
            print err2
            print "Your code did not build!"
            f.write("Here are the errors generated by the compiler:")
            f.write(err0)
            f.write(err1)
            f.write(err2)
            f.write("Your code did not build!")

