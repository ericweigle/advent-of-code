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
  return [[int(x) for x in line] for line in lines]

def flash_one(board, row, col):
  for x in (-1, 0, 1):
    for y in (-1, 0, 1):
      e_row = row+x
      e_col = col+y
      if (e_row >= 0 and e_row < len(board) and
          e_col >= 0 and e_col < len(board[0]) and
          (e_row != row or e_col != col)):
        board[e_row][e_col] += 1

def flash_all(board, flashed):
  before = len(flashed)
  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] >= 10 and (row,col) not in flashed:
        flash_one(board, row, col)
        flashed.add((row,col))
  return len(flashed) > before

def step(board):
  for row in range(len(board)):
    for col in range(len(board[row])):
      board[row][col] += 1

  flashed = set()
  while flash_all(board, flashed):
    pass

  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] >= 10:
        board[row][col] = 0
  return len(flashed)

def dump(board):
  for line in board:
    print(''.join([str(x) for x in line]))
  print()

def part1(board):
  total_flashed = 0
  for i in range(100):
    total_flashed += step(board)
  print("part 1:",total_flashed)

def part2(board):
  for i in range(1000000):
    if step(board) == 100:
      print("part 2",i+1)
      return

for filename in sys.argv[1:]:
  print(f"For file '{filename}'")
  board = parse(filename)
  part1(copy.deepcopy(board))
  part2(copy.deepcopy(board))

