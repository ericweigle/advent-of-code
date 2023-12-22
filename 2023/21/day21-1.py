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


def mkboard(data):
  board = []
  for row in data:
    board.append([x for x in row])
  for row in range(len(board)):
    for column in range(len(board[row])):
      if board[row][column] == 'S':
        start = (row,column)
  return start, board

def step(board, positions):
  result = set()
  for row,column in positions:
    for rd, cd in ((-1,0), (1,0), (0,-1), (0,1)):
      nr = row + rd
      nc = column + cd
      if nr < 0 or nr >= len(board) or nc < 0 or nc >= len(board[nr]) or board[nr][nc] == '#':
        continue
      result.add((nr,nc))
  return result

def part1(start, board):
  positions = set([start,])
  for i in range(64):
    positions = step(board, positions)
    print(f"step {i} options {len(positions)}")
  print("Final", len(positions))

def part2(start, board):
  pass

def mymain(filename):
  start, board = mkboard(aoc.lines(filename))

  print("Part 1")
  part1(start, board)

  print("Part 2")
  part2(start, board)

aoc.run(mymain)

