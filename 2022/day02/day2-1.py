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
    if me == rps[0]:
      # rock
      return 1 + 3
    elif me == rps[1]:
      # paper
      return 2 + 6
    elif me == rps[2]:
      # scissors
      return 3 + 0

  elif opp == "B":
    # paper
    if me == rps[0]:
      # rock
      return 1 + 0
    elif me == rps[1]:
      # paper
      return 2 + 3
    elif me == rps[2]:
      # scissors
      return 3 + 6

  elif opp == "C":
    # scissors
    if me == rps[0]:
      # rock
      return 1 + 6
    elif me == rps[1]:
      # paper
      return 2 + 0
    elif me == rps[2]:
      # scissors
      return 3 + 3

total = 0
for guide in open(INPUT).readlines():
  total += score(guide.strip())
  #print(score(guide.strip()))
print(total)
