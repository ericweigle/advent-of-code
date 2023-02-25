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

def initialize(data):
  for r in range(len(data)):
    data[r] = [int(x) for x in data[r]]
  #print(data)

  output = dict()
  for r in range(len(data)):
    for c in range(len(data[r])):
      data[r][c] = int(data[r][c])
      output[(r,c)] = set()
  return output

def visible_upward(data, output):
  for c in range(len(data[0])):
    max_height = -1
    for r in range(len(data)):
      if data[r][c] > max_height:
        output[(r,c)].add('up')
        max_height = data[r][c]

def visible_downward(data, output):
  for c in range(len(data[0])):
    max_height = -1
    for r in range(len(data)-1,-1,-1):
      if data[r][c] > max_height:
        output[(r,c)].add('down')
        max_height = data[r][c]

def visible_leftward(data, output):
  for r in range(len(data)):
    max_height = -1
    for c in range(len(data[r])):
      if data[r][c] > max_height:
        output[(r,c)].add('left')
        max_height = data[r][c]

def visible_rightward(data, output):
  for r in range(len(data)):
    max_height = -1
    for c in range(len(data[r])-1,-1,-1):
      if data[r][c] > max_height:
        output[(r,c)].add('right')
        max_height = data[r][c]


def part1(data):
  output = initialize(data)
  visible_upward(data,output)
  visible_downward(data,output)
  visible_leftward(data,output)
  visible_rightward(data,output)

  count = 0
  for r in range(len(data)):
    for c in range(len(data[r])):
      if output[(r,c)]:
        count += 1
  return count


def scenic_score(data, row, col):
  # up
  up = 0
  for r in range(row-1,-1,-1):
    up += 1
    if data[r][col] >= data[row][col]:
      break

  # down
  down = 0
  for r in range(row+1,len(data)):
    down += 1
    if data[r][col] >= data[row][col]:
      break

  # left
  left = 0
  for c in range(col-1,-1,-1):
    left += 1
    if data[row][c] >= data[row][col]:
      break

  # right
  right = 0
  for c in range(col+1,len(data[0])):
    right += 1
    if data[row][c] >= data[row][col]:
      break

  return left*right*up*down


def part2(data):
  initialize(data)

  best = -1
  for r in range(len(data)):
    for c in range(len(data[r])):
      score = scenic_score(data,r,c)
      if score > best:
        best = score
  return best


def mymain(filename):
  data = aoc.lines(filename)
  
  print("Part 1",part1(data))

  print("Part 2",part2(data))

# 368,368
aoc.run(mymain)
