#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc

def hits_target(xv, yv, target):
  x = 0
  y = 0
  max_y = -1000000
  for i in range(2000):
    x += xv
    y += yv
    xv = max(0,xv-1)
    yv -= 1
    max_y = max(y,max_y)

    if (x >= target[0][0] and
        x <= target[0][1] and
        y >= target[1][0] and
        y <= target[1][1]):
      # This is a hit
      return max_y
    if ((x < target[0][0] and xv <= 0) or
       (y < target[1][0] and yv <= 0) or
       x > target[0][1]):
      return None
  else:
    return "FAILED"

def part1(target):
  best = 0
  count = 0
  for x_vel in range(-1000, 1000):
    for y_vel in range(-1000, 1000):
      max_y = hits_target(x_vel, y_vel, target)
      if max_y == "FAILED":
        print("FAILED:",x_vel,y_vel,max_y)
      elif max_y is not None:
        count += 1
        if max_y > best:
          best = max_y
  print("pt1, best:",best)
  print("pt2, count:",count)

#example = ((20,30),(-10,-5))
#part1(example)
actual = ((155,182),(-117,-67))
part1(actual)
