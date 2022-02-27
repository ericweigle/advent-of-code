#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc

def step_east(data):
  changed = False
  board = copy.deepcopy(data)
  for row in range(len(data)):
    for col in range(len(data[row])):
      if data[row][col] == '.' and data[row][col-1]=='>':
        changed = True
        board[row][col] = '>'
        board[row][col-1] = '.'
  return changed, board

def step_south(data):
  changed = False
  board = copy.deepcopy(data)
  for row in range(len(data)):
    for col in range(len(data[row])):
      if data[row][col] == '.' and data[row-1][col]=='v':
        changed = True
        board[row][col] = 'v'
        board[row-1][col] = '.'
  return changed, board


def part1(data):
  steps = 0
  while True:
    changed1, data = step_east(data)
    changed2, data = step_south(data)
    steps += 1
    if not changed1 and not changed2:
      break
  print(f"Stabilized at {steps}")

def part2(data):
  pass

def mymain(filename):
  data = aoc.lines(filename)
  parsed = []
  for line in data:
    parsed.append([x for x in line.strip()])
  data = parsed

  print("Part 1")
  part1(data)

  print("Part 2")
  part2(data)

aoc.run(mymain)


