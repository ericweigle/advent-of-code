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
  start = (0,1)
  return board, start

def valid(pt, board):
  return pt[0] >= 0 and pt[0] < len(board) and pt[1] >= 0 and pt[1] < len(board[pt[0]]) and board[pt[0]][pt[1]] != '#'

def neighbors_pt1(row, col, board):
  up    = (row-1, col)
  down  = (row+1, col)
  left  = (row, col-1)
  right = (row, col+1)

  # mandatory moves
  if board[row][col] == 'v':
    if valid(down, board):
      yield down
      return
  elif board[row][col] == '>':
    if valid(right, board):
      yield right
      return
  elif board[row][col] == '<':
    if valid(left, board):
      yield left
      return

  if valid(up, board):
    yield up
  if valid(down, board):
    yield down
  if valid(left, board):
    yield left
  if valid(right, board):
    yield right

def neighbors_pt2(row, col, board):
  up    = (row-1, col)
  down  = (row+1, col)
  left  = (row, col-1)
  right = (row, col+1)

  if valid(up, board):
    yield up
  if valid(down, board):
    yield down
  if valid(left, board):
    yield left
  if valid(right, board):
    yield right


def part1(data):
  board, start = mkboard(data)

  visited_set = set()
  to_visit = [(start[0], start[1], set())]

  deepest = 0
  while to_visit:
    row, column, visited = to_visit.pop(0)
    visited.add((row, column))
    deepest = max(deepest, len(visited))

    for neighbor in neighbors_pt2(row, column, board):
      if neighbor in visited:
        continue
      to_visit.append((neighbor[0], neighbor[1], copy.copy(visited)))
  print(f"Deepest {deepest-1}")


def part2(data):
  pass

def mymain(filename):
  data = aoc.lines(filename)

  print("Part 1")
  part1(data)

  print("Part 2")
  part2(data)

aoc.run(mymain)

