#!/usr/bin/python3

import pprint

#INPUT = "example.txt"
INPUT = "input.txt"

def score(guide, rps=("X","Y","Z")):
  #print(guide)
  assert len(guide) == 3
  opp = guide[0]
  me = guide[2]
  assert opp in ("A", "B", "C")
  assert me in ("X", "Y", "Z")

  if opp == "A":
    # rock
    if me == rps[0]: # lose
      return 3 + 0
    elif me == rps[1]: # draw
      return 1 + 3
    elif me == rps[2]: # win
      return 2 + 6

  elif opp == "B":
    # paper
    if me == rps[0]:
      return 1 + 0
    elif me == rps[1]:
      return 2 + 3
    elif me == rps[2]:
      return 3 + 6

  elif opp == "C":
    # scissors
    if me == rps[0]:
      return 2 + 0
    elif me == rps[1]:
      return 3 + 3
    elif me == rps[2]:
      return 1 + 6

total = 0
for guide in open(INPUT).readlines():
  total += score(guide.strip())
  #print(score(guide.strip()))
print(total)

# 9974 is too low
