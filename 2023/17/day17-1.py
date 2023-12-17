#!/usr/bin/python3

import collections

import code
import copy
import math
import parse
import pprint
import heapq
import re
import sys
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc

def mk_board(data):
  result = []
  for line in data:
    result.append([int(x) for x in line])
  return result

def neighbors(r, c, cost, last_dirs):
  if last_dirs != ('u', 'u', 'u') and last_dirs[-1]!='d':
    yield (cost, (r-1,c), (r,c), [last_dirs[-2], last_dirs[-1], 'u'])
  if last_dirs != ('d', 'd', 'd') and last_dirs[-1]!='u':
    yield (cost, (r+1,c), (r,c), [last_dirs[-2], last_dirs[-1], 'd'])
  if last_dirs != ('l', 'l', 'l') and last_dirs[-1]!='r':
    yield (cost, (r,c-1), (r,c), [last_dirs[-2], last_dirs[-1], 'l'])
  if last_dirs != ('r', 'r', 'r') and last_dirs[-1]!='l':
    yield (cost, (r,c+1), (r,c), [last_dirs[-2], last_dirs[-1], 'r'])

#def dump_costs(min_cost):
#  pprint.pprint(min_cost)

def part1(board):
  min_cost = []
  for r in board:
    min_cost.append([])
    for c in board:
      min_cost[-1].append({})
  last_dirs = ('x', 'x', 'x')
  min_cost[0][0] = {last_dirs: 0}

  to_visit = []
  for neighbor in neighbors(0,0,0,last_dirs):
    heapq.heappush(to_visit, neighbor)
  while to_visit:
    cost, cur, last, last_dirs = heapq.heappop(to_visit)
    #print(f"Visiting {cur} from {last} dirs {last_dirs} costs old {cost}")
    r, c = cur
    if r<0 or r>=len(board) or c<0 or c>=len(board[0]):
      #print("...bounded.")
      continue

    # ensure we're improving the state
    new_cost = cost + board[r][c]
    #print(f"... new {new_cost}")
    last_dirs = tuple(last_dirs)
    if new_cost >= min_cost[r][c].get(last_dirs, 99999999999):
      continue
    min_cost[r][c][last_dirs] = new_cost
    #if r==1 and c==3:
    #  print(min_cost[r][c])


    for neighbor in neighbors(r, c, new_cost, last_dirs):
      heapq.heappush(to_visit, neighbor)

    #print("First 5 neighbors:")
    #pprint.pprint(to_visit[:5])

  print(f"\n\nCost {min(min_cost[-1][-1].values())}\n")
  #code.interact(local=locals())
  #print(f"Cost {min_cost[0][0]}")
  #print(f"Cost {min_cost[0][1]}")
  #print(f"Cost {min_cost[0][2]}")
  #print(f"Cost {min_cost[1][2]}")
  #print(f"Cost {min_cost[1][3]}")
  #print(f"Cost {min_cost[1][4]}")
  #print(f"Cost {min_cost[1][5]}")
  #print(f"Cost {min_cost[0][6]}")
  #print(f"Cost {min_cost[0][7]}")
  #print(f"Cost {min_cost[0][8]}")
  #print(f"Cost {min_cost[0][9]}")

def part2(board):
  pass

def mymain(filename):
  board = mk_board(aoc.lines(filename))

  print("Part 1")
  part1(board)

  print("Part 2")
  part2(board)

aoc.run(mymain)

