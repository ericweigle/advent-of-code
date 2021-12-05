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
  data = [x.strip() for x in open(filename, 'r').readlines()] 
  #print(data)
  result = []
  for line in data:
    a, b = line.split(' -> ')
    a = [int(x) for x in a.split(',')]
    b = [int(x) for x in b.split(',')]
    result.append([a, b])
  return result

def part1(data):
  # make board
  size  = 0
  for line in data:
    for pt in line:
      for c in pt:
        size  = max(size , c)
  size += 1
  board = []
  for x in range(size):
    board.append([0]*size)

  for line in data:
    start = line[0]
    end = line[1]
    if start[0] == end[0]:
      # horizontal
      x = start[0]
      for y in range(min(start[1],end[1]),max(start[1],end[1])+1):
        board[x][y] += 1
    elif start[1] == end[1]:
      # vertical
      y = start[1]
      for x in range(min(start[0],end[0]),max(start[0],end[0])+1):
        board[x][y] += 1
    else:
      # Diagonals
      x = start[0]
      y = start[1]
      if x < end[0]:
        delta_x = 1
      else:
        delta_x = -1
      if y < end[1]:
        delta_y = 1
      else:
        delta_y = -1
      while (x, y) != tuple(end):
        board[x][y] += 1
        x += delta_x
        y += delta_y
      board[x][y] += 1

  #transposed = list(zip(*board))
  #pprint.pprint(transposed)
  
  doubles = 0
  for row in board:
    for val in row:
      if val > 1:
        doubles += 1
  print(doubles)


def part2(data):
  pass

for filename in sys.argv[1:]:
  print(f"For file '{filename}'")
  data = parse(filename)
  #print(data)

  part1(copy.deepcopy(data))
  part2(data)
