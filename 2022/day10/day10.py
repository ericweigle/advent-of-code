#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc


def solve(data):
  cycle = [None,1]
  for line in data:
    if line.startswith('noop'):
      cycle.append(cycle[-1])
    elif line.startswith("addx"):
      amount = int(line.split(" ")[-1])
      cycle.append(cycle[-1])
      cycle.append(cycle[-1] + amount)
    else:
      assert False

  # Part 1
  total = 0
  for x in range(20,221,40):
    #print(x,len(cycle))
    if x >= len(cycle):
      break
    #print(x,cycle[x]*x)
    total += cycle[x]*x
  print("  Part 1: ", total)

  # Part 2
  for row in range(6):
    line = []
    for column in range(40):
      timer = row*40+column+1
      if cycle[timer] in (column-1,column,column+1):
        line.append("#")
      else:
        line.append(' ')
    print(''.join(line))
    


def mymain(filename):
  data = aoc.lines(filename)
  solve(data)

aoc.run(mymain)

