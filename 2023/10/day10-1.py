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

def make_board(data):
  for i in range(len(data)):
    data[i] = [x for x in data[i]]
  return data

def find_start(data):
  for r in range(len(data)):
    for c in range(len(data[r])):
      if data[r][c] == 'S':
        return (r,c)
  raise ValueError("No start")

def bounded(board, r,c):
  return r >=0 and r < len(board) and c>=0 and c < len(board[0])

def visit(to_visit, r, c, count):
  if count not in to_visit:
    to_visit[count] = []
  to_visit[count].append((r,c))

def bfs(board, to_visit):
  while to_visit:
    count = min(to_visit.keys())
    if not to_visit[count]:
      del to_visit[count]
      if not to_visit:
        return count
      continue

    start = to_visit[count].pop()
    r, c = start
    if board[r][c] in ('|', '-', 'L', 'J', '7', 'F', '.', 'S'):
      board[r][c] = count
    else:
      # already visited
      continue

    # up
    r,c   = (start[0]-1, start[1])
    if bounded(board, r, c) and board[r][c] in ('|', '7', 'F'):
      visit(to_visit, r, c, count+1)

      # | is a vertical pipe connecting north and south.
      # 7 is a 90-degree bend connecting south and west.
      # F is a 90-degree bend connecting south and east.

    # down  = (start[0]+1, start[1])
    r, c  = (start[0]+1, start[1])
    if bounded(board, r, c) and board[r][c] in ('|', 'L', 'J'):
      visit(to_visit, r, c, count+1)
      # | is a vertical pipe connecting north and south.
      # L is a 90-degree bend connecting north and east.
      # J is a 90-degree bend connecting north and west.

    # left
    r, c  = (start[0], start[1]-1)
    if bounded(board, r, c) and board[r][c] in ('-', 'L', 'F'):
      visit(to_visit, r, c, count+1)
      # - is a horizontal pipe connecting east and west.
      # L is a 90-degree bend connecting north and east.
      # F is a 90-degree bend connecting south and east.

    # right
    r, c = (start[0], start[1]+1)
    if bounded(board, r, c) and board[r][c] in ('-', 'J', '7'):
      visit(to_visit, r, c, count+1)
      # - is a horizontal pipe connecting east and west.
      # J is a 90-degree bend connecting north and west.
      # 7 is a 90-degree bend connecting south and west.


def part1(board, start):
  print("Start",start)
  copied = copy.deepcopy(board)
  best = bfs(board, {0: [start]})
  print(f"Best: {best}")


def mymain(filename):
  data = aoc.lines(filename)
  board = make_board(data)
  start = find_start(board)

  print("Part 1")
  part1(board, start)

aoc.run(mymain)

