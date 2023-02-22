#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

#cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
cups = [8, 5, 3, 1, 9, 2, 6, 4, 7]

for i in range(100):
  #print("Cups:",cups)
  picked = cups[1:4]
  #print(picked,"\n")
  cups = [cups[0]] + cups[4:]
  dest = cups[0]-1
  while dest not in cups:
    dest -= 1
    if dest < 1:
      dest = 9
  dest_idx = cups.index(dest)+1
  #print(dest,dest_idx)
  cups = cups[:dest_idx] + picked + cups[dest_idx:]
  cups.append(cups.pop(0))

while cups[0]!=1:
  cups.append(cups.pop(0))
print("".join([str(x) for x in cups[1:]]))
