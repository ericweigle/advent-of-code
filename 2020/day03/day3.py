#!/usr/bin/python3

import re
import sys

for filename in sys.argv[1:]:
  data = [x.strip() for x in open(filename, 'r').readlines()]
  huge = [2000 * x for x in data]
  #assert len(huge[0])==31*35
 
  #for line in huge:
  #  print(line)

  final = 1
  for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    count = 0
    for i in range(1, len(huge)):
      row = i * down
      column = i * right
      if row > len(huge):
        break
      #print(row,column)
      if huge[row][column] == '#':
        count += 1
    print(count)
    final *= count
  print('=%d' % final)
