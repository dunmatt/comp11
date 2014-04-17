#!/usr/bin/env python
"""
"""

import re
from utilities import *

def buildTable(version="1"):
  run("rm", ["-f", "FrequencyTable.h", "FrequencyTable.o"])
  run("ln", ["-s", "FrequencyTable%s.h" % version, "FrequencyTable.h"])
  return build(["wordfreq.cpp"
                , "FrequencyTable%s.cpp" % version
                , "WordFreqList.cpp"
               ], "wordfreq%s" % version)

def makeFishString(fish):
  return "fish %s %s %s %s %s %s %s\n%s\n" % (fishImages[fish[4]][0]
                                              , fishImages[fish[4]][1]
                                              , fish[0]
                                              , fish[1]
                                              , fish[2]
                                              , fish[3]
                                              , fish[4]
                                              , fishImages[fish[4]][2])

def makeInputString(tankSize, fish):
  tank = "tank %s %s\n" % tankSize
  return tank + "\n".join(map(makeFishString, fish))

def goFishing(tankSize=(40, 80),
              fish=[(10,12, 0,0, "minnow")],
              frames=[0]):
  """Test project 3.

  """
  stdin = makeInputString(tankSize, fish)
  (_, stdout, _) = run("./SimFishy", [], stdin, 2, False)
  frameList = listifyFrames(stdout, tankSize[0])
  # print frameList
  for fNum in frames:
    print frameList[fNum][:-1]

def listifyFrames(stdout, lineCount):
  return re.findall("(?:[%s]+\n){%s}" % (expectedChars, lineCount), stdout)

def makeEmptyTank(size):
  return (size, [[" " for _ in range(size[1])] for _ in range(size[0])])

def drawFishAtTime(tank, fish, fishImg, t):
  for r, line in enumerate(fishImg[2].split("\n")):
    for c, char in enumerate(line):
      if char != " ":
        row = int(r + fish[0] + t * fish[2]) % tank[0][0]
        col = int(c + fish[1] + t * fish[3]) % tank[0][1]
        tank[1][row][col] = char

def referenceSolution(tankSize, fish, frame=0):
  tank = makeEmptyTank(tankSize)
  for f in fish:
    drawFishAtTime(tank, f, fishImages[f[4]], frame)
  print "\n".join(["".join(line) for line in tank[1]])




if __name__ == "__main__":
  import doctest
  print "These tests take 34 seconds to run, be patient"
  print "When something goes wrong, the way to read the test case is"
  print "goFishing((1, 10), [(0,3, 0,-1, 'minnow')], range(4))   ===>"
  print "the first 4 frames of SimFishy given the input:"
  print "tank 1 10\nfish 1 3 0 3 0 -1 minnow\n><>\nEOF"
  print ""
  (failureCount, testCount) = doctest.testmod()
  correctCount = testCount - failureCount
  print "Project 3 Total: %s / %s" % (correctCount, testCount)


