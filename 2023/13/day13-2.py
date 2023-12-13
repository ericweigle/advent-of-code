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

def get_reflection(board):
  #print(f"Board {boardnum}")
  #print("--------------------------------------------------------------------------------")
  rows = board.split("\n")
  if not rows[-1]:
    rows = rows[:-1]
  columns = len(rows[0])
  board = "".join(rows) 
  cols = [board[i::columns] for i in range(columns)]
  #for foo in rows:
  #  print(f"'{foo}'")
  #for foo in cols:
  #  print(f"'{foo}'")

  #print("Rows --------------------------------------------------------------------------------")
  for r in range(len(rows)-1):
    if reflection(rows, r):
      yield ('r', r+1)
  #print("Cols --------------------------------------------------------------------------------")
  for c in range(len(cols)-1):
    if reflection(cols, c):
      yield ('c', c+1)


# 21896 - fail
def part2(data):
  dedup = dict()
  total = 0
  for boardnum, board in enumerate(data):
    dedup[boardnum] = list(get_reflection(board))
    assert dedup[boardnum] and len(dedup[boardnum])==1
    for i in range(len(board)):
      #print(f"Trying {boardnum} {i}")
      trials = []
      if board[i] == '.':
        #print(f"Orig {i} .:\n{board}")
        fixed = board[:i]+'#'+board[i+1:] +'\n'
        #print(f"Fixed {i}:\n{fixed}\n")
        trials = list(get_reflection(fixed))
      elif board[i] == '#':
        #print(f"Orig {i} #:\n{board}")
        fixed = board[:i]+'.'+board[i+1:] +'\n'
        #print(f"Fixed {i}:\n{fixed}\n")
        trials = list(get_reflection(fixed))
      elif board[i] == '\n':
        continue
      else:
        print("Fail")
        sys.exit(1)

      for trial in trials:
        if trial not in dedup[boardnum]:
          assert len(dedup[boardnum]) == 1
          #  print(f"Found twice, board {boardnum}, {trial}")
          #  assert trial in dedup[boardnum]
          #  continue
          if trial[0] == 'r':
            total += 100*trial[1]
          else:
            total += trial[1]
          dedup[boardnum].append(trial)
    if len(dedup[boardnum])==1:
      print(f"Found never, board {boardnum}")
      sys.exit(1)
    else:
      print(f"OK {boardnum}")
          
  print(total)

def mymain(filename):
  data = open(filename).read().split("\n\n")

  print("Part 2")
  part2(data)

aoc.run(mymain)

