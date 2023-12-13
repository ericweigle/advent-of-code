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

def reflection(rc, i):
  for j in range(99999):
    a = i-j
    b = i+j+1
    if a < 0 or a >= len(rc) or b<0 or b>=len(rc):
      return True
    if rc[a]!=rc[b]:
      #print(f"Mismatch at {a},{b}")
      #print(f"  {rc[a]}")
      #print(f"  {rc[b]}")
      return False
    else:
      pass
      #print(f"  Match at {a},{b}")

def get_reflection(board_str):


def part1(data):
  total = 0
  for boardnum, board in enumerate(data):
    print(f"Board {boardnum}")
    print("--------------------------------------------------------------------------------")
    rows = board.split("\n")
    if not rows[-1]:
      rows = rows[:-1]
    columns = len(rows[0])
    board = "".join(rows) 
    cols = [board[i::columns] for i in range(columns)]
    for foo in rows:
      print(f"'{foo}'")
    for foo in cols:
      print(f"'{foo}'")

    print("Rows --------------------------------------------------------------------------------")
    for r in range(len(rows)-1):
      if reflection(rows, r):
        print(f"Board {boardnum} Reflection at row {r+1}")
        total += 100*(r+1)
    print("Cols --------------------------------------------------------------------------------")
    for c in range(len(cols)-1):
      if reflection(cols, c):
        print(f"Board {boardnum} Reflection at col {c+1}")
        total += (c+1)

  print(total)
    #print(rows)
    #print(cols)

def part2(data):
  pass

def mymain(filename):
  data = open(filename).read().split("\n\n")

  print("Part 1")
  part1(data)

  print("Part 2")
  part2(data)

aoc.run(mymain)

