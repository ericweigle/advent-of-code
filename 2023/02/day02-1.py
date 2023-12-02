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


def parse_r(reveal):
  assert len(reveal.split(",")) <= 3
  result = []
  for color in ("red", "green", "blue"):
    c = re.search(f"([0-9]+) {color}", reveal)
    if c:
      result.append(int(c.group(1)))
    else:
      result.append(0)
  return result 


def possible(results):
  for r, g, b in results:
    if r>12 or g>13 or b>14:
      return False
  return True


def min_cubes(results):
  max_r, max_g, max_b = (0,0,0)
  for r, g, b in results:
      max_r = max(r,max_r)
      max_g = max(g,max_g)
      max_b = max(b,max_b)
  return max_r*max_g*max_b


def parse(data):
  total = 0
  power = 0
  for line in data:
    game = int(re.search("Game ([0-9]+)", line).group(1))
    revealed = [parse_r(x.strip()) for x in line.split(';')]
    #print(game)
    #print(revealed)
    if possible(revealed):
      #print("  possible")
      total += game
    else:
      #print("  not possible")
      pass

    power += min_cubes(revealed)

  print(f"Part 1 total {total}")
  print(f"Part 2 total {power}")


def mymain(filename):
  data = aoc.lines(filename)
  parse(data)


aoc.run(mymain)

