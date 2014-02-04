#!/usr/bin/env python
"""HW3 Grading Script

Usage:
    ./hw3.py <dir> <files>...
"""

from utilities import *

submission_filters = {
    "required": ["max3.cpp", "max3.data"
                 , "3wordsort.cpp", "3wordsort.data"
                 , "chkdate.cpp", "chkdate.data"]
    , "permitted": []
}

if __name__ == "__main__":
    from docopt import docopt
    arguments = docopt(__doc__, version="Tufts Comp11 HW3 v2014s")
    screenFilenames(arguments["<files>"], submission_filters)

    (code0, o, err0) = build(["max3.cpp"], "max3")
    (code1, o, err1) = build(["3wordsort.cpp"], "3wordsort")
    (code2, o, err2) = build(["chkdate.cpp"], "chkdate")

    if code0 or code1 or code2:
        print err0
        print err1
        print err2
        with getScorecard(arguments["<dir>"]) as f:
            f.write(err0)
            f.write(err1)
            f.write(err2)
    else:
        (return_code, stdout, stderr) = run("../../tests/hw3/hw3_test.py")
        print stdout
        with getScorecard(arguments["<dir>"]) as f:
            f.write(stdout)
