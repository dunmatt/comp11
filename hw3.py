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

    print build(["max3.cpp"], "max3")[2]
    print build(["3wordsort.cpp"], "3wordsort")[2]
    print build(["chkdate.cpp"], "chkdate")[2]

    (return_code, stdout, stderr) = run("../../tests/hw3/hw3_test.py")
    print stdout
    with getScorecard(arguments["<dir>"]) as f:
        f.write(stdout)
