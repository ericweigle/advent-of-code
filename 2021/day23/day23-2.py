#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc

#   #################
#   #01..2..3..4..56#
#   ###07#09#11#13###
#     #08#10#12#14#
#     #############
 
# Input puzzle
#   #############
#   #...........#
#   ###A#D#B#D###
#     #B#C#A#C#
#     #########

#...B.D.....
#  B . C D
#  A . C A



#   0 1 2  3 4  5 6  7 8 9 0 
#       11   12   13   14   
#       15   16   17   18 
#       19   20   21   22 
#       23   24   25   26 
NEIGHBORS = {
  0:  (1,),
  1:  (0,2),
  2:  (1,3,11),
  3:  (2,4),
  4:  (3,5,12),
  5:  (4,6),
  6:  (5,7,13),
  7:  (6,8),
  8:  (7,9,14),
  9:  (8,10),
  10:  (9,),
  11:  (2,15),
  12:  (4,16),
  13:  (6,17),
  14:  (8,18),

  15:  (11,19),
  16:  (12,20),
  17:  (13,21),
  18:  (14,22),
  
  19:  (15,23),
  20:  (16,24),
  21:  (17,25),
  22:  (18,26),

  23:  (19,),
  24:  (20,),
  25:  (21,),
  26:  (22,),
}

def parse_board(board):
  board = re.sub(" ", "", board)
  return tuple([x for x in board])

def serialize_board(board):
  return ''.join(board)

def is_first_row(pos):
  return pos<=10

def can_stay(pos):
  return pos not in (2, 4, 6, 8)

def is_room(pos):
  return pos > 10

def stay_at_home(amphipod, pos, board):
  if is_proper_room(amphipod, pos):
    return (pos>=23 or
            (pos>=19 and board[pos+4] == amphipod) or
            (pos>=15 and board[pos+4] == amphipod and board[pos+8] == amphipod) or
            (pos>=11 and board[pos+4] == amphipod and board[pos+8] == amphipod and board[pos+12] == amphipod))

  return False

def target_room(amphipod):
  if amphipod=='A':
    return (11,15,19,23)
  elif amphipod == 'B':
    return (12,16,20,24)
  elif amphipod == 'C':
    return (13,17,21,25)
  elif amphipod == 'D':
    return (14,18,22,26)

def forbidden_rooms(amphipod):
  return set(range(11,27)) - set(target_room(amphipod))

def is_proper_room(amphipod, pos):
  return pos in target_room(amphipod)

def amphipod_positions(board):
  for pos, amphipod in enumerate(board):
    if amphipod in ('A','B','C','D'):
      yield pos

def reachable_squares(board, start_pos):
  global NEIGHBORS
  reachable = set()
  to_visit = list(NEIGHBORS[start_pos])
  while to_visit:
    pos = to_visit.pop(0)
    if board[pos] == '.' and pos not in reachable:
      reachable.add(pos)
      to_visit.extend(NEIGHBORS[pos])
  return reachable


def legal_amphipod_moves(board, pos):
  #print(f"Checking legal moves for pos {pos} {len(board)}")
  amphipod = board[pos]
  #print(f"Found amphipod {board[pos]} at {pos}")

  # Find reachable squares
  reachable = reachable_squares(board,pos)
  if is_room(pos):
    if stay_at_home(amphipod, pos, board):
      # Already in optimal position
      return set()

    # Moving FROM room TO hallway
    # Can't stop in first square outside room
    reachable -= set((2,4,6,8))
    # For simplicity, break trip up into two moves
    # by subtracting out the rooms from the reach list
    reachable -= set(range(11,27))
    return reachable
  else:
    # Moving FROM hallway TO target room
    t1, t2, t3, t4 = target_room(amphipod)
    if t4 in reachable:
      return set([t4,])
    if t3 in reachable and board[t4] == amphipod:
      return set([t3,])
    if t2 in reachable and board[t3] == amphipod and board[t4]==amphipod:
      return set([t2,])
    if t1 in reachable and board[t2] == amphipod and board[t3] == amphipod and board[t4]==amphipod:
      return set([t1,])
  return set()

def move_amphipod(board, from_pos, to_pos):
  result = [x for x in board]
  result[to_pos] = result[from_pos]
  result[from_pos] = '.'
  return tuple(result)

def per_move_cost(amphipod):
  if amphipod=='A':
    return 1
  if amphipod=='B':
    return 10
  if amphipod=='C':
    return 100
  if amphipod=='D':
    return 1000

def num_steps(board, from_pos, to_pos):
  # Manhattan distance, again
  coordinate_transform = {
    0:  (0,0),
    1:  (0,1),
    2:  (0,2),
    3:  (0,3),
    4:  (0,4),
    5:  (0,5),
    6:  (0,6),
    7:  (0,7),
    8:  (0,8),
    9:  (0,9),
    10: (0,10),

    11: (1,2),
    12: (1,4),
    13: (1,6),
    14: (1,8),

    15: (2,2),
    16: (2,4),
    17: (2,6),
    18: (2,8),

    19: (3,2),
    20: (3,4),
    21: (3,6),
    22: (3,8),

    23: (4,2),
    24: (4,4),
    25: (4,6),
    26: (4,8),
  }
  r1, c1 = coordinate_transform[from_pos]
  r2, c2 = coordinate_transform[to_pos]
  return int(abs(r1-r2) + abs(c1-c2))


def all_legal_moves(board, baseline_cost):
  """Returns a list of (total cost, reachable board) for boards we can reach from here with one move and a given baseline cost."""
  result = []
  for pos in amphipod_positions(board):
    for new_pos in legal_amphipod_moves(board, pos):
      new_board = move_amphipod(board, pos, new_pos)
      new_cost = num_steps(board, pos, new_pos) * per_move_cost(board[pos])
      result.append((baseline_cost+new_cost, new_board))
  return result

class VisitList(object):
  def __init__(self):
    self.to_visit = dict()
    self.min_score = 0
    self.added = 0
    self.popped = 0

  def extend(self, score_board_pairs):
    self.added += len(score_board_pairs)
    for score, board in score_board_pairs:
      assert score >= self.min_score
      if score in self.to_visit:
        #print("Exists")
        self.to_visit[score].append(board)
      else:
        #print("New")
        self.to_visit[score] = [board]
    #print(f"To visit: {len(self.to_visit)} -- {len(score_board_pairs)}")

  def empty(self):
    empty = (len(self.to_visit) == 0)
    if empty:
      print(f"Empty! {self.added} == {self.popped}")
    return empty

  def pop(self):
    if self.empty():
      return None
    while True:
      if self.min_score in self.to_visit:
        to_return = self.to_visit[self.min_score].pop(0)
        if not self.to_visit[self.min_score]:
          self.to_visit.pop(self.min_score)
        self.popped += 1
        return self.min_score, to_return
      self.min_score+= 1
      #print("Min score ",self.min_score)

def part2(board):
  visited = dict()
  to_visit = VisitList()
  visited[board] = 0
  to_visit.extend(all_legal_moves(board, 0))
  goal_board =  parse_board("........... ABCD ABCD ABCD ABCD")

  counter = 0
  while not to_visit.empty():
    cost, next_board = to_visit.pop()
    if next_board == goal_board:
      print("Cheapest way to destination: ",cost)
      return

    if (next_board not in visited or
        cost < visited[next_board]):
      visited[next_board] = cost
      counter += 1
      if (counter % 100)==0:
        print(f"visited {cost} {next_board}")
      to_visit.extend(all_legal_moves(next_board, cost))

  print("Never reached goals.")


def mymain():
  #                         111111111
  #               0123456789012345678            
  #serial_board = "...........BCBDDCBADBACADCA" # example
  serial_board = "...........ADBDDCBADBACBCAC" # input

  print("Part 2")
  part2(parse_board(serial_board))

#print(legal_amphipod_moves(parse_board("...B.D..... B.CD A.CA"), 3))
mymain()
