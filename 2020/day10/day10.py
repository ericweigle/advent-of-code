#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

# part 1
for filename in sys.argv[1:]:
  data = [int(x.strip()) for x in open(filename, 'r').readlines()]

  curr = 0
  diff = [0, 0, 0, 1]
  for i in sorted(data):
    diff[i-curr]+=1
    curr = i
  print(diff)
  print(diff[1]*diff[3])

# example1: 8
# example2: 19208


def get_count_to(start, target, mytree, memoized):
  if (start, target) in memoized:
    return memoized[(start, target)]

  print('count_to %d %d' % (start, target))
  if target < start:
    return 0
  elif target == start:
    return 1
  elif target > start:
    total = 0
    children = mytree[start]
    for child in children:
      if child == target:
        total += 1
      elif child < target:
        total += get_count_to(child, target, mytree, memoized)
      # if child > target, do nothing.
    memoized[(start, target)] = total
    return total


for filename in sys.argv[1:]:
  data = [int(x.strip()) for x in open(filename, 'r').readlines()]
  data.append(0)

  print(sorted(data))
  mytree = {}
  for i in sorted(data):
    reachable = list(sorted(x for x in data if i < x <= i + 3))
    mytree[i] = reachable
  pprint.pprint(mytree)
  #  reach_count = [0]*len(data)
  print(get_count_to(start=0, target=max(data), mytree=mytree, memoized={}))
