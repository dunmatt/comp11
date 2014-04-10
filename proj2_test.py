#!/usr/bin/env python
"""
"""

from utilities import *

fishImages = {
  "minnow": (1, 3, "><>"),
  "aviators": (10, 52, """ _,a========Y88888888888888888888888888========a,_
dP                  `"b,    ,d"'                 Yb
8l                    8l____8l                    8l
8l                    8l----8l                    8l
8l                   d8      8b                   8l
8l                ,dP/        \Yb,                8l
8l             ,adP'/          \`Yba,             8l
 Yb       ,aadP'                    `Yaa,        dP
  `b==,aaP'                             `Ybaa,=dP'"""),
  "bigPhish": (30, 60, """7DNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7MNNNNNNNNNNNNNNNNNNDN87777NNNNNDI7$NNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNMNN777777NNNN$7777777MNNNNNNNNNNNNNNNNNNNNN
MMNNNNNNNNNNNNNNNINN7777IOIZN77777777777ZMNNNNNNNNNNNNNNNNNN
NZNNNNNNNNNNNO7II7NN77777N7I$IIIII7I77I77?NNNNNNNNNNNNNNNNNN
NMNNNNNNNNNNN?NIIIMNIIIIMMNNIIIIII8III7IIN?NNNNNNNNNNNNNNNNN
DNNNNNNNNNMN7I8IIIONIIIIN?IIIIIIDNNN8IIIDNI$NNNNNNNNNNNNDNNN
NMNNNNNNNNN???+???=N??IMM???+??ZNNNNN??+N+???=NNNNNNNNNNN7MN
M8NNNNNNO?++++++++=N+++N7+++=++NNNNND?+8N++++NMNNNNNNNNNN$+N
MND=~D=++++$N++=++=D=+IN====N++NNNN,MNNN$==+DNNN=MNNNNNNDM8N
ND====OD=======~==~N==NN====Z:=ONNN7NNNM====N==NNM~NNNNDNNNN
NM~===MN=======MN==N=+NN=====D==NNNNNNN~===~N===~NNNM=+NM~NN
N7NNNNNI++++++NNN++I+=NO+++++NM+=DNNNNN=++++N+++NNNNNNND:BNN
NMNNNNNMZ?+++$NNN+++++NI+++++DNN?=NNNNNN+++=N++?NNNNNNNN~NNN
NDNNNM8MN????NNNN????+N??????INNNIINNNNN????N??+NNNNNNNN8OMN
NNNNNNNONIIIDNNNNIINIINI?IIII?NNNN?IDNNNNIIIIII?NNNNNNNND+NN
NNNNNNNNNIIINNNNNIIN77N$IIIII7NNNNNIIINNNI77Z7IINNNNNNNN78NN
NNINNNNNN777NNNNO77N77N8777777NNNNNN777NN777D777NNNNNNNDD7?N
NNNMNNNNNI77NNNN777N7INN777777NNNNNN877$N777N777NNNN7NNINNMM
NNNNONND7777NNNN77IN7INN7777I7NNNNNNN777N$77N7777NDNNNNNDNNN
NNNNNM7?7I7INNNN777N7IDN777I77MNNNNNNI7IN877IO77N$NNNNNNMNIN
NNNNNNNNNNNNNNNOIION7I7NI7III7NNNZDNNI77ND777DNMNNNNNNNNN8ZN
NNNNNNNNNNNNDNNIIIDNIIIN$IIIIINNND7NNIIINDIII?DNNNNNNNNNN7N8
NNNNNNNNNNNNNZZIIINNIIINNIIIIINNNI?N7II?N8IIO?NNNNNNNNNNNNNN
NNNNNNNNNNNNNIIIIINNI??NN?II??INII?????NNOINNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNII??NN???IN????7$N??I????MN7NNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNN7??IN?I??NN???N?N?I????NNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNII????IN+??NOMI?II?INNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNDNZI??D?Z?N?NNM?7NNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNMNNNDNNNNNNNNNNNNNNNNNNNNNNNNNNNNN""")
}

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
              fish=[(10,12, 0,0, "minnow")]):
  """Test project 2.

  # TODO: test one line fish drawn correctly
  # TODO: test one multiline fish drawn correctly
  # TODO: test multiple fish drawn correctly
  # TODO: test transparency
  # TODO: test horizontal integer motion
  # TODO: test vertical integer motion
  # TODO: test diagonal integer motion
  # TODO: test horizontal floating point motion
  # TODO: test vertical floating point motion
  # TODO: test diagonal floating point motion
  # TODO: test horizontal motion wrapping
  # TODO: test vertical motion wrapping
  # TODO: test diagonal motion wrapping
  # TODO: test horizontal render wrapping
  # TODO: test vertical render wrapping
  # TODO: test max tank size
  # TODO: test tiny tank
  # TODO: test max fish size
  # TODO: test tiny fish (plankton?)
  # TODO: 
  # TODO: 
  """
  stdin = makeInputString(tankSize, fish)
  (_, stdout, _) = run("./SimFishy", [], stdin, 2)
  pass

def listifyFrames(stdout):
  pass

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
  return "\n".join(["".join(line) for line in tank[1]])




if __name__ == "__main__":
  import doctest
  (failureCount, testCount) = doctest.testmod()
  correctCount = testCount - failureCount
  print "Project 1 Total: %s / %s" % (correctCount, testCount)


