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


def get_board(data):
  result = []
  for line in data:
    result.append([x for x in line])
  return result

def roll_slice_north(row, low, high):
  #print(f"    Rolling piece: {row[low:high]}")
  # known to not have a #, roll everything all the way down.
  rocks = sum([1 for x in row[low:high] if x=='O'])
  empties = sum([1 for x in row[low:high] if x=='.'])
  assert rocks + empties == (high-low)
  for i in range(high-low):
    if i < rocks:
      row[low+i] = 'O'
    else:
      row[low+i] = '.'
  #print(f"    Result {row}")

def roll_left(row):
  rocks = [i for i in range(len(row)) if row[i] == '#']
  if not rocks:
    #print(f"Only piece case")
    roll_slice_north(row, 0, len(row))
    return
  #print(f"Rolling piece 0: {rocks[0]}")
  roll_slice_north(row, 0,rocks[0])
  for i in range(0, len(rocks)-1):
    #print(f"Rolling piece {i}: {rocks[i]}")
    roll_slice_north(row, rocks[i]+1, rocks[i+1])
  #print(f"Rolling piece {-1}: {rocks[-1]}")
  roll_slice_north(row, rocks[-1]+1, len(row))
  #print(f"Final result: {row}")

def roll_north(board):
  for c in range(len(board[0])):
    col = []
    for r in range(len(board)):
      col.append(board[r][c])
    #print(f"Col {c} is {col}")
    roll_left(col)
    for r in range(len(board)):
      board[r][c] = col[r]

def roll_south(board):
  for c in range(len(board[0])):
    col = []
    for r in range(len(board)-1,-1,-1):
      col.append(board[r][c])
    roll_left(col)
    for r in range(len(col)):
      board[len(board)-r-1][c] = col[r]

def roll_west(board):
  for r in range(len(board)):
    roll_left(board[r])

def roll_east(board):
  for r in range(len(board)):
    row = list(reversed(board[r]))
    roll_left(row)
    row = list(reversed(row))
    for c in range(len(row)):
      board[r][c] = row[c]

def dump(board):
  for row in board:
    print("".join(row))
  print("\n")

def spin_cycle(board):
  roll_north(board)
  #dump(board)
  roll_west(board)
  #dump(board)
  roll_south(board)
  #dump(board)
  roll_east(board)
  #dump(board)

def load(board):
  total = 0
  for row in range(len(board)):
    weight = len(board)-row
    for rock in board[row]:
      if rock == 'O':
        total += weight
  return total

def part1(data):
  roll_north(data)
  print(f"load = {load(data)}")

def cache_key(board):
  return '\n'.join([''.join(row) for row in board])

def part2(data):
  load_cache = dict()
  board_cache = dict()
  number_mapper = dict()
  offset = None
  mapped_offset = None
  cycle = None
  for i in range(300):
    spin_cycle(data)
    load_cache[i+1] = load(data)

    key = cache_key(data)

    if key in board_cache:
      #print(f"Cache hit {i} -> {board_cache[key]}")
      if offset is None:
        offset = i
        mapped_offset = board_cache[key]
        #print(f"Found offset {offset} mapped to {mapped_offset}")
      elif board_cache[key] == mapped_offset and cycle is None:
        cycle = i-offset
        #print(f"Found cycle {cycle}")
    else:
      number_mapper[i] = key
      board_cache[key] = i
    #print(len(board_cache))

  # Validation run
  for i in range(149,299):
    target = (i-offset)%cycle+mapped_offset
    if load_cache[i] != load_cache[target]:
      print(f"Mismatch at {i} != {target}")
  # Final result
  i = 1000000000
  target = (i-offset)%cycle+mapped_offset
  print(f"Mapping {i} to {target} load {load_cache[target]}")

def mymain(filename):
  data = aoc.lines(filename)
  data = get_board(data)

  print("Part 1")
  part1(data)

  print("Part 2")
  part2(data)

aoc.run(mymain)

