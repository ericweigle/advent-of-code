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

def find_and_replace_letter(board, letter, replace):
  for row in range(len(board)):
    for column in range(len(board[row])):
      if board[row][column] == letter:
        board[row][column] = replace
        return (row,column)

def part1(board, start, end):
  visited = dict()
  queue = [(0, start[0], start[1])]
  while queue:
    cost, row, col = queue.pop(0)

    #print(f"Visiting ({row},{col})")
    if (row, col) == end:
      continue
    neighbors = (
      (row-1,col),
      (row+1,col),
      (row,col-1),
      (row,col+1)
    )

    for next_row, next_col in neighbors:
      if (next_row >= 0 and next_row < len(board) and 
          next_col >= 0 and next_col < len(board[row]) and
          ord(board[next_row][next_col]) <= (ord(board[row][col])+1)):
        # can move to that square
        if (((next_row, next_col) not in visited) or 
            visited[(next_row, next_col)] > (cost+1)):
          visited[(next_row, next_col)] = (cost+1)
          queue.append((cost+1, next_row, next_col))
  return visited.get(end, 999999999999)

def part2(board, start, end):
  best = 999999999999999
  for r in range(len(board)):
    for c in range(len(board[r])):
      if board[r][c] == 'a':
        steps = part1(board, (r,c), end)
        if steps < best:
          best = steps
  return best


def parse_board(filename):
  data = aoc.lines(filename)
  board = []
  for line in data:
    board.append(list(x for x in line.strip()))

  #pprint.pprint(board)
  start = find_and_replace_letter(board, 'S', 'a')
  end = find_and_replace_letter(board, 'E', 'z')

  return start, end, board


def mymain(filename):
  start, end, board = parse_board(filename)

  #print("Start",start)

  print("Part 1", part1(board, start, end))

  print("Part 2", part2(board, start, end))

aoc.run(mymain)

