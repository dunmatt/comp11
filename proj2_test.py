#!/usr/bin/env python
"""
"""

import re
from utilities import *

fishImages = {
  "minnow": (1, 3, "><>"),
  "corners": (2, 4, """UTCO
AZNM"""),
  "aviators": (9, 52, """ _,a========Y88888888888888888888888888========a,_  
dP                  `"b,    ,d"'                 Yb 
8l                    8l____8l                    8l
8l                    8l----8l                    8l
8l                   d8      8b                   8l
8l                ,dP/        \Yb,                8l
8l             ,adP'/          \`Yba,             8l
 Yb       ,aadP'                    `Yaa,        dP 
  `b==,aaP'                             `Ybaa,=dP'  """),
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

# "".join(list(set(list("".join([f[2] for f in fishImages.values()])))))  # to calculate next line's literal
expectedChars = '\n "$\'+\\-,/78:=<?>BDIMONPYZUTCOAZNM\\\\_a`bdl~'

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
  """Test project 2.

  >>> goFishing((5, 5), [(1,1, 0,0, "minnow")])  # one line fish drawn correctly
  <BLANKLINE>
   ><> 
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  >>> # referenceSolution((10, 52), [(0,0, 0,0, "aviators")])
  >>> goFishing((10, 52), [(0,0, 0,0, "aviators")])  # one multiline "fish" drawn correctly
   _,a========Y88888888888888888888888888========a,_  
  dP                  `"b,    ,d"'                 Yb 
  8l                    8l____8l                    8l
  8l                    8l----8l                    8l
  8l                   d8      8b                   8l
  8l                ,dP/        \Yb,                8l
  8l             ,adP'/          \`Yba,             8l
   Yb       ,aadP'                    `Yaa,        dP 
    `b==,aaP'                             `Ybaa,=dP'  
  <BLANKLINE>
  >>> goFishing((5, 10), [(1,1, 0,0, "minnow"), (3,6, 0,0, "minnow")])  # multiple fish drawn correctly
  <BLANKLINE>
   ><>      
  <BLANKLINE>
        ><> 
  <BLANKLINE>
  >>> goFishing((10, 52), [(2, 10, 0,0, "minnow"), (0,0, 0,0, "aviators")])  # transparency
   _,a========Y88888888888888888888888888========a,_  
  dP                  `"b,    ,d"'                 Yb 
  8l        ><>         8l____8l                    8l
  8l                    8l----8l                    8l
  8l                   d8      8b                   8l
  8l                ,dP/        \Yb,                8l
  8l             ,adP'/          \`Yba,             8l
   Yb       ,aadP'                    `Yaa,        dP 
    `b==,aaP'                             `Ybaa,=dP'  
  <BLANKLINE>
  >>> goFishing((10, 52), [(2, 20, 0,0, "minnow"), (0,0, 0,0, "aviators")])  # opacity
   _,a========Y88888888888888888888888888========a,_  
  dP                  `"b,    ,d"'                 Yb 
  8l                  ><8l____8l                    8l
  8l                    8l----8l                    8l
  8l                   d8      8b                   8l
  8l                ,dP/        \Yb,                8l
  8l             ,adP'/          \`Yba,             8l
   Yb       ,aadP'                    `Yaa,        dP 
    `b==,aaP'                             `Ybaa,=dP'  
  <BLANKLINE>
  >>> goFishing((1, 10), [(0,0, 0,1, "minnow")], range(4))  # horizontal integer motion
  ><>       
   ><>      
    ><>     
     ><>    
  >>> goFishing((1, 10), [(0,3, 0,-1, "minnow")], range(4))  # horizontal integer motion
     ><>    
    ><>     
   ><>      
  ><>       
  >>> goFishing((5, 3), [(0,0, 1,0, "minnow")], range(3))  # vertical integer motion
  ><>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  ><>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  ><>
  <BLANKLINE>
  <BLANKLINE>
  >>> goFishing((5, 3), [(4,0, -1,0, "minnow")], range(3)) # vertical integer motion
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  ><>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  ><>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  ><>
  <BLANKLINE>
  <BLANKLINE>
  >>> goFishing((5, 5), [(0,0, 1,1, "minnow")], range(3)) # diagonal integer motion
  ><>  
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
   ><> 
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
    ><>
  <BLANKLINE>
  <BLANKLINE>
  >>> goFishing((1, 10), [(0,0, 0,.5, "minnow")], range(8))  # TODO: horizontal floating point motion
  ><>       
  ><>       
   ><>      
   ><>      
    ><>     
    ><>     
     ><>    
     ><>    
  >>> goFishing((5, 3), [(0,0, 1.5,0, "minnow")], range(3)) # vertical floating point motion
  ><>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  ><>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  ><>
  <BLANKLINE>
  >>> goFishing((1, 10), [(0,0, 0,1, "minnow")], [0,11]) # horizontal motion wrapping
  ><>       
   ><>      
  >>> goFishing((3, 3), [(0,0, -1,0, "minnow")], range(2)) # vertical motion wrapping
  ><>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  ><>
  >>> goFishing((2,4), [(0,0, 1,1, "corners")], range(3))  # diagonal motion wrapping
  UTCO
  AZNM
  MAZN
  OUTC
  COUT
  NMAZ
  >>> goFishing((50, 200), [(49,198, 0,0, "corners")])  # max tank size
  NM                                                                                                                                                                                                    AZ
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  <BLANKLINE>
  CO                                                                                                                                                                                                    UT
  >>> goFishing((30, 60), [(0,0, 0,0, "bigPhish")])  # max phish size
  7DNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
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
  NNNNNNNNNNNNNNNNNNNNNNNNNNMNNNDNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
  """
  stdin = makeInputString(tankSize, fish)
  (_, stdout, _) = run("./SimFishy", [], stdin, 2, False)
  frameList = listifyFrames(stdout)
  for fNum in frames:
    print frameList[fNum][:-1]

def listifyFrames(stdout):
  return re.findall("[%s]+" % expectedChars, stdout)

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
  (failureCount, testCount) = doctest.testmod()
  correctCount = testCount - failureCount
  print "Project 1 Total: %s / %s" % (correctCount, testCount)


