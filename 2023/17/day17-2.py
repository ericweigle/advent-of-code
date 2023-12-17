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

def neighbors(r, c, board, cost, last_dirs):
  if can_move(r, c, board, last_dirs, 'u'):
    yield (cost, (r-1,c), (r,c), last_dirs[1:] + 'u')
  if can_move(r, c, board, last_dirs, 'd'):
    yield (cost, (r+1,c), (r,c), last_dirs[1:] + 'd')
  if can_move(r, c, board, last_dirs, 'l'):
    yield (cost, (r,c-1), (r,c), last_dirs[1:] + 'l')
  if can_move(r, c, board, last_dirs, 'r'):
    yield (cost, (r,c+1), (r,c), last_dirs[1:] + 'r')


#def can_move_print(moves, to_add):
#  result = can_move(moves, to_add)
#  print(f"can_move({moves}, {to_add}) -> {result}")
#  return result

def can_move(r, c, board, moves, to_add):
  assert len(moves) == 10

  if to_add != moves[-1]:
    # Turning. Make sure we have space for 4 moves
    # without running off the board.
    if to_add == 'u':
      if r < 4:
        return False
    elif to_add == 'd':
      if r >= (len(board)-4):
        return False
    elif to_add == 'l':
      if c < 4:
        return False
    elif to_add == 'r':
      if c >= (len(board[0])-4):
        return False
    else:
      raise ValueError(f"illegal turn {to_add}")

  if to_add == moves[-1]:
    # Maximum of 10 moves in one direction
    if to_add=='u' and moves=='uuuuuuuuuu':
      return False
    if to_add=='d' and moves=='dddddddddd':
      return False
    if to_add=='l' and moves=='llllllllll':
      return False
    if to_add=='r' and moves=='rrrrrrrrrr':
      return False
    return True
    #return (len(set(moves)) > 1)

  # if this is a turn, ensure we've moved the 4 minimum blocks in prior direction
  count = 0
  for x in reversed(moves):
    if x==moves[-1]:
      count+=1
    else:
      break
  return count>=4

#def dump_costs(min_cost):
#  pprint.pprint(min_cost)

def part2(board):
  min_cost = []
  for r in board:
    min_cost.append([])
    for c in board:
      min_cost[-1].append({})
  last_dirs = ('xxxxxxxxxx')
  min_cost[0][0] = {last_dirs: 0}

  to_visit = []
  for neighbor in neighbors(0,0,board,0,last_dirs):
    heapq.heappush(to_visit, neighbor)
  #print("to visit:")
  #pprint.pprint(to_visit)
  while to_visit:
    cost, cur, last, last_dirs = heapq.heappop(to_visit)
    #print(f"Visiting {cur} from {last} dirs {last_dirs} costs old {cost}")
    r, c = cur
    if r<0 or r>=len(board) or c<0 or c>=len(board[0]):
      #print("...board bounded.")
      continue

    # ensure we're improving the state
    new_cost = cost + board[r][c]
    #print(f"... new {new_cost}")
    if new_cost >= min_cost[r][c].get(last_dirs, 99999999999):
      #print("...cost bounded.")
      continue
    min_cost[r][c][last_dirs] = new_cost
    #if r==1 and c==3:
    #  print(min_cost[r][c])

    for neighbor in neighbors(r, c, board,new_cost, last_dirs):
      #print(f"New neighbor {neighbor} with {last_dirs}")
      heapq.heappush(to_visit, neighbor)
    #print("to visit:")
    #pprint.pprint(to_visit)

    #print("First 5 neighbors:")
    #pprint.pprint(to_visit[:5])

  pprint.pprint(min_cost[-1][-1])
  print(f"\n\nCost {min(min_cost[-1][-1].values())}\n")


# TODO: 993 is too low << what this code generates
# TODO: 996 is too low
# TODO: 997 << right answer, from binary search :(
# TODO: 999 is too high
def mymain(filename):
  board = mk_board(aoc.lines(filename))

  print("Part 2")
  part2(board)

aoc.run(mymain)
