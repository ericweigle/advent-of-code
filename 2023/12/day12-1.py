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


def doparse(data):
  for line in data:
    dots, numbers = line.split()
    #dots = [x for x in dots.split(".") if x]
    dots = [x for x in dots]
    numbers = [int(x) for x in numbers.split(',')]
    yield (dots, numbers)


def consistent(dots, numbers):
  count = 0
  counts = []
  for i in range(len(dots)):
    if dots[i]== '.':
      if count > 0:
        counts.append(count)
      count = 0
    elif dots[i]== '#':
      count += 1
    else:
      raise ValueError("Undefined symbol")
  if count > 0:
    counts.append(count)
  if counts != numbers:
    #print(f"Inconsistent {dots} {counts} != {numbers}")
    return False

  #print(f"Consistent {dots} {numbers}")
  return True     


def expand(dots, numbers, i):
  total = 0
  if i == len(dots):
    if consistent(dots, numbers):
      return 1
    return 0
  elif dots[i] == '?':
    dots[i] = '.'
    total += expand(dots, numbers, i+1)
    dots[i] = '#'
    total += expand(dots, numbers, i+1)
    dots[i] = '?'
  else:
    total += expand(dots, numbers, i+1)
  return total

def part1(data):
  pprint.pprint(data)
  total = 0
  for dots, nums in data:
    count = expand(dots, nums, 0)
    #print(count)
    total += count
  print(total)

def part2(data):
  pass

def mymain(filename):
  data = aoc.lines(filename)
  data = list(doparse(data))

  print("Part 1")
  part1(data)

  print("Part 2")
  part2(data)

aoc.run(mymain)

