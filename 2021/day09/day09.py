#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)

def parse(filename):
  lines = [x.strip() for x in open(filename, 'r').readlines()]
  lines = [[int(x) for x in line] for line in lines]
  return lines

def neighbors(row, col, data):
  val = []
  if row > 0:
    val.append((row-1,col))
  if row < (len(data)-1):
    val.append((row+1,col))
  if col > 0:
    val.append((row,col-1))
  if col < (len(data[0])-1):
    val.append((row,col+1))
  return val

def is_low(row, col, data):
  for r, c in neighbors(row,col,data):
    if data[r][c] <= data[row][col]:
      return False
  return True

def get_low_points(data):
  for row in range(len(data)):
    for col in range(len(data[row])):
      if is_low(row, col, data):
        yield (row,col)

def part1(data):
  risk = sum(data[row][col]+1 for row,col in get_low_points(data))
  print("pt1",risk)

def fill_basin(row,col,data):
  data[row][col] = 9
  size = 0
  for r, c in neighbors(row,col,data):
    if data[r][c] != 9:
      size += fill_basin(r, c, data)
  return 1 + size

def part2(data):
  basin_sizes = []
  for row, col in get_low_points(data):
    basin_sizes.append(fill_basin(row,col,data))
  it = reversed(sorted(basin_sizes))
  print("pt2",next(it)*next(it)*next(it))

for filename in sys.argv[1:]:
  print(f"For file '{filename}'")
  data = parse(filename)

  part1(copy.deepcopy(data))
  part2(data)
