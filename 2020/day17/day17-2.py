#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)


def neighborcount(active, z, row, col, w):
  count = 0
  for zd in (-1, 0, 1):
    for rd in (-1, 0, 1):
      for cd in (-1, 0, 1):
        for wd in (-1, 0, 1):
          if zd != 0 or rd !=0 or cd != 0 or wd != 0:
            if (z+zd,row+rd,col+cd, w + wd) in active:
              count+=1
              if count > 3:
                return count
  return count


for filename in sys.argv[1:]:
  data = [x.strip() for x in open(filename, 'r').readlines()]
  
  rows = len(data)
  cols = len(data[0])

  active = set()
  active_range = [0, rows, cols, 0]
  for row in range(rows):
    for col in range(cols):
      if data[row][col] == '#': # active
        active.add((0,row,col, 0))

  for iteration in range(6):
    active_range = [x+1 for x in active_range]
    new_active = set()
    for z in range(-1*active_range[0], active_range[0]+1):
      for row in range(-1*active_range[1], active_range[1]+1):
        for col in range(-1*active_range[2], active_range[2]+1):
          for w in range(-1*active_range[3], active_range[3]+1):
            if (z,row,col,w) in active:
              if neighborcount(active, z, row, col,w)in (2,3):
                # If a cube is active and exactly 2 or 3 of its neighbors are also active,
                # the cube remains active. Otherwise, the cube becomes inactive.
                new_active.add((z,row,col,w))
            elif neighborcount(active, z, row, col,w) == 3:
              #  If a cube is inactive but exactly 3 of its neighbors are active,
              #  the cube becomes active. Otherwise, the cube remains inactive.
              new_active.add((z,row,col,w))
    active = new_active
  print(len(active))
