#!/usr/bin/python3

import pprint

#INPUT = "example.txt"
INPUT = "input.txt"

def parse_crates(crates):
  stacks = {}
  for c in range(1,100,4):
    for r in range(len(crates)-2, -1, -1):
      if c < len(crates[r]):
        box = crates[r][c]
        if box == ' ':
          continue

        col = (c // 4) + 1
        if col not in stacks:
          stacks[col] = []
        stacks[col].append(box)
  return stacks

def parse_moves(moves):
  moves = [x.split() for x in moves if x]
  #print(moves)
  return [(int(x[1]), int(x[3]), int(x[5])) for x in moves]
  return moves  

data = open(INPUT).read()
crates, moves = data.split("\n\n")
crates = parse_crates(crates.split("\n"))
#print(crates)
moves = parse_moves(moves.split("\n"))
#print(moves)
for num_boxes, source, dest in moves:
  temp = []
  for boxid in range(num_boxes):
    temp.append(crates[source].pop(-1))
  while temp:
    crates[dest].append(temp.pop(-1))

for i in range(1,100):
  if i in crates:
    if crates[i]:
      print(crates[i][-1])
