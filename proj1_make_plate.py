#!/usr/bin/env python
"""Proj1 Plate Generator

Usage:
    ./proj1_make_plate.py [options] <specification>...

Options:
    --help                      Show this screen.
    --version                   Show version.
    -h=<h>, --height=<h>        Height of the generated plate.  [default: 16]
    -w=<w>, --width=<w>         Width of the generated plate.   [default: 76]
    --dig_height=<dh>           Height of a single digit.       [default: 7]
    --dig_width=<dw>            Width of a single digit.        [default: 5]
    --digits_file=<digits>      What file contains the digits?  [default: digits.dat]
"""

import re
import sys

def parseSpec(rawSpec):
    # returns a list of triples: (digit, row, col)
    withStrings = re.findall(r"\s*(\w+)\s*@\s*(\d+)\s*,\s*(\d+)", rawSpec)
    return [(c[0], int(c[1]), int(c[2])) for c in withStrings]

def readDatFile(filename):
    contents = ""
    with open(filename) as f:
        contents = f.read()
    hits = re.findall(r"(\w+)\s+\d+\s+\d+([\s.#]+)", contents)
    results = {}
    for hit in hits:
        results[hit[0]] = hit[1].replace(" ", "").replace("\t", "").split()
    return results

def between(x, lower, upper):
    return lower <= x and x <= upper

def isOverlap(a, b, dh, dw):
    return (between(a[1], b[1], b[1] + dh) and between(a[2], b[2], b[2] + dw)
         or between(b[1], a[1], a[1] + dh) and between(b[2], a[2], a[2] + dw))

def isConflict(a, b, dh, dw):
    return a != b and isOverlap(a, b, dh, dw)

def getConflicts(a, spec, dh, dw):
    return [(a, b) for b in spec if isConflict(a, b, dh, dw)]

def isOnBoard(a, h, w, dh, dw):
    return a[1] + dh < h and a[2] + dw < w

def getValidCharacters(spec, h, w, dh, dw):
    return [c for c in spec if isOnBoard(c, h, w, dh, dw)
                                and not getConflicts(c, spec, dh, dw)]

def getEmptyBoard(h, w):
    return ["." * w for _ in range(h)]

def getBoard(h, w, digits, spec):
    board = getEmptyBoard(h, w)
    for s in spec:
        d = digits[s[0]]
        for i in range(len(d)):
            bi = s[1] + i
            board[bi] = board[bi][:s[2]] + d[i] + board[bi][s[2] + len(d[i]):]
    return board

if __name__ == "__main__":
    from docopt import docopt
    args = docopt(__doc__, version="Project 1 Plate Generator v2014s")

    h = int(args["--height"])
    w = int(args["--width"])
    dh = int(args["--dig_height"])
    dw = int(args["--dig_width"])
    spec = parseSpec(" ".join(args["<specification>"]))
    valid = getValidCharacters(spec, h, w, dh, dw)
    digits = readDatFile(args["--digits_file"])
    if len(spec) == len(valid):
        board = getBoard(h, w, digits, valid)
        for row in board:
            print row
        print ""
    else:
        for err in set(spec) - set(valid):
            print "%s @ %s,%s is invalid." % (err[0], err[1], err[2])
