#!/usr/bin/python3

import collections

import copy
import math
import parse
import pprint
import re
import sys
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc

def read_pt1(data):
  for line in data:
    d, m, c = parse.parse("{} {} (#{})", line)
    yield (d,int(m),c)

def read_pt2(data):
  for d,m,c in data:
    d = {'0':'R', '1':'D', '2':'L', '3':'U'}[c[-1]]
    m = int(c[:-1],16)
    yield (d, m, None)

def build_trench(data):
  trench_locs = list()
  loc = (0,0)
  for direction, length, color in data:
    if direction == 'U':
      loc = (loc[0]-length, loc[1])
    elif direction == 'D':
      loc = (loc[0]+length, loc[1])
    elif direction == 'L':
      loc = (loc[0], loc[1]-length)
    elif direction == 'R':
      loc = (loc[0], loc[1]+length)
    else:
      raise ValueError(f"Bad direction {direction}")
    trench_locs.append(loc)
  return trench_locs

def shoelace(points):
  total = 0
  m = len(points)
  for i in range(0,len(points)):
    total += points[i][0] * (points[(i+1)%m][1]-points[(m+i-1)%m][1])
  return abs(total) // 2

def trench_border_volume(data):
	return sum([x[1] for x in data])

def part2(data):
  trench_locs = build_trench(data)
  area = shoelace(trench_locs) + trench_border_volume(data)//2 + 1
  print(f"total: {area}")
  
def mymain(filename):
  pt1_data = list(read_pt1(aoc.lines(filename)))
  pt2_data = list(read_pt2(pt1_data))

  print("Part 1")
  part2(pt1_data)
  print("Part 2")
  part2(pt2_data)

aoc.run(mymain)

