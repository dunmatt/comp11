#!/usr/bin/env python
"""HW4 Grading Script

Usage:
    ./hw4.py <dir> <files>...
"""

from utilities import *

submission_filters = {
    "required": ["diag.cpp", "mirror.cpp"]
    , "permitted": []
}

if __name__ == "__main__":
    from docopt import docopt
    arguments = docopt(__doc__, version="Tufts Comp11 HW4 v2014s")
    screenFilenames(arguments["<files>"], submission_filters)

    (code0, o, err0) = build(["diag.cpp"], "diag")
    (code1, o, err1) = build(["mirror.cpp"], "mirror")

    if code0 or code1:
        print err0
        print err1
        print "Your code did not build!"
        print "Assignment hw4 Total: 0 / 10" 
        with getScorecard(arguments["<dir>"], "hw4") as f:
            f.write(err0)
            f.write(err1)
            f.write("Your code did not build!")
            f.write("Assignment hw4 Total: 0 / 10")
    else:
        (return_code, stdout, stderr) = run("../../tests/hw4/hw3_test.py")
        print stdout
        with getScorecard(arguments["<dir>"], "hw4") as f:
            f.write(stdout)

