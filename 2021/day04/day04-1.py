#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)

def parse_board(b):
  board = re.sub('  ', ' ', b.strip())
  board = board.split('\n')
  board = [x.split(' ') for x in board]
  for row in range(len(board)):
    for col in range(len(board[row])):
      board[row][col] = int(board[row][col])
  return board

def mark(number, board):
  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] == number:
        board[row][col] = None

def is_winner(board):
  for row in board:
    marked = sum([1 for x in row if x is None])
    if marked == len(row):
      return True
  
  for col in range(len(board[0])):
    effective = [x[col] for x in board]
    marked = sum([1 for x in effective if x is None])
    if marked == len(effective):
      return True

def score_pt1(board, last_num):
  total = 0
  for row in board:
    for col in row:
      if col is not None:
        total += col
  return total * last_num


for filename in sys.argv[1:]:
  data = [x.strip() for x in open(filename, 'r').readlines()]

  picks = [int(x) for x in data[0].split(',')]
  data = data[2:]

  boards = '\n'.join(data).split('\n\n')
  boards = [parse_board(x) for x in boards]

  already_won = set()
  for pick in picks:
    for boardnum,board in enumerate(boards):
      mark(pick, board)
      if is_winner(board):
        if boardnum not in already_won:
          print("board",boardnum,"wins with score", score_pt1(board, pick))
          already_won.add(boardnum)
