#!/usr/bin/env python
"""
"""

from collections import defaultdict
from utilities import *

mobyDick = readFile("../../tests/proj3/mobydick.txt")
# mobyDick = readFile("mobydick.txt")

def lnp(s):
  for result in s.split("\n"):
    print result

def wordfreq(version, stdin):
  """Test project 3.

  >>> lnp(wordfreq(1, "Does it sort sorted words?"))
  1 does
  1 it
  1 sort
  1 sorted
  1 words?
  >>> lnp(wordfreq(1, "Does it sort unsorted words correctly?"))
  1 correctly?
  1 does
  1 it
  1 sort
  1 unsorted
  1 words
  >>> lnp(wordfreq(1, "da da da da"))
  4 da
  >>> wordfreq(1, mobyDick)  # does it take too long using the slow way?
  aborting, algorithm too slow
  >>> wordfreq(2, mobyDick) == referenceSolution(mobyDick)  # does it handle huge texts using the fast way?
  True
  """
  # stdout = referenceSolution(stdin)
  # TODO: the hard coded 2 here may take some tuning
  (error, stdout, _) = run("./wordfreq%s" % version, [], stdin, 2, False)
  if error:
    print "aborting, algorithm too slow"
  return stdout

def referenceSolution(stdin):
  words = stdin.split()
  counters = defaultdict(lambda: 0)
  for word in words:
    counters[word.lower()] += 1
  results = ["%s %s" % (i[1], i[0]) for i in sorted(counters.items())]
  return "\n".join(results)

if __name__ == "__main__":
  import doctest
  (failureCount, testCount) = doctest.testmod()
  correctCount = testCount - failureCount
  print "Project 3 Total: %s / %s" % (correctCount, testCount)


