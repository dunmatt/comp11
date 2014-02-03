#!/usr/bin/env python
"""HW3 Grading Script

Usage:
    ./hw3.py <dir> <assignment> <files>...
"""
#TODO: double check the args to this script

from utilities import *

submission_filters = {
    "required": ["max3.cpp", "max3.data"
                 , "3wordsort.cpp", "3wordsort.data"
                 , "chkdate.cpp", "chkdate.data"]
    , "permitted": []
}

if __name__ == "__main__":
    from docopt import docopt
    arguments = docopt(__doc__, version="Tufts Comp11 HW3 grading script v2014s")

    screenFilenames(arguments["<files>"], submission_filters)


