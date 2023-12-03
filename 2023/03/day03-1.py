#!/usr/bin/python3

import collections

import re
import parse
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc


def isdigit(x):
  return x in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


def full_number(x, y, lines):
  # find start (moving left)
  left = x
  for i in range(99999):
    if (x-i) < 0 or not isdigit(lines[y][x-i]):
      break
    left = x-i

  # find end (moving right)
  for i in range(99999):
    if (x+i) >= len(lines[y]) or not isdigit(lines[y][x+i]):
      break
    right = x+i

  # We add the number location so we don't double count.
  return (int(''.join(lines[y][left:right+1])), y, left)


def find_adjacent_numbers(x, y, lines):
  for i in (-1,0,1):
    for j in (-1,0,1):
      xp = x+i
      yp = y+j
      if (yp >= 0 and yp < len(lines) and
          xp >= 0 and xp < len(lines[yp]) and 
          isdigit(lines[yp][xp])):
            yield full_number(xp, yp, lines)


def run(lines):
  part2 = 0
  for y in range(len(lines)):
    lines[y] = [c for c in lines[y]]
  all_adjacent = set()
  for y in range(len(lines)):
    line = lines[y]
    for x in range(len(lines[y])):
      c = line[x]
      if c != '.' and not isdigit(c):
        # symbol
        for a in find_adjacent_numbers(x, y, lines):
          all_adjacent.add(a)
      if c == '*':
        # gear?
        adj = set(find_adjacent_numbers(x, y, lines))
        if len(adj) == 2:
          adj = [x[0] for x in adj]
          part2 += adj[0]*adj[1]

  part_total = sum([x[0] for x in all_adjacent])
  print(f"Part 1: {part_total}")
  print(f"Part 2: {part2}")


def mymain(filename):
  data = aoc.lines(filename)

  run(data)

aoc.run(mymain)

