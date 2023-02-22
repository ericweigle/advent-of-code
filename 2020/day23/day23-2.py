#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

#cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]#  +list(range(10,1000001))
cups = [8, 5, 3, 1, 9, 2, 6, 4, 7] + list(range(10,1000001))
assert len(cups)==1000000

def to_llist(cups):
  result = dict()
  for index in range(len(cups)):
    value = cups[index]
    result[value] = cups[(index+1) % len(cups)]
  return result

def unchain(curr, values):
  start = curr
  result = []
  for i in range(len(values)):
    result.append(curr)
    curr = values[curr]
    if curr == start:
      break
  return result

current = cups[0]
max_val = max(cups)

#pprint.pprint(cups)
chained = to_llist(cups)
#pprint.pprint(chained)
assert unchain(current, chained) == cups
cups = chained
#pprint.pprint(cups) 

for i in range(10000000):
  if (i%100000 == 0):
    print("up to...",i)
  #print("Current cup:",current)
  #print("Chain",unchain(current, cups))
  picked = [cups[current]]
  picked.append(cups[picked[0]])
  picked.append(cups[picked[1]])
  ##print("picked",picked)
  cups[current] = cups[picked[2]]
  #print("excluded",unchain(current, cups))
  dest = current-1
  while dest in picked or dest<1:
    dest -= 1
    if dest < 1:
      dest = max_val

  #print("Dest",dest,"picked[2]",picked[2])
  old_next = cups[dest]
  cups[dest] = picked[0]
  cups[picked[2]] = old_next

  current = cups[current]
  #print("")


#print(unchain(current,cups))

print(cups[1]*cups[cups[1]])
