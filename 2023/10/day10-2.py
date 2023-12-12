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
import png

import render


def make_board(data):
  for i in range(len(data)):
    data[i] = [x for x in data[i]]
  return data

# This only works for my particular input,
# where start == 'L'
def replace_start(data):
  for r in range(len(data)):
    for c in range(len(data[r])):
      if data[r][c] == 'S':
        data[r][c] = 'L'
        return (r,c)
  raise ValueError("No start")

def bounded(board, r,c):
  return r >=0 and r < len(board) and c >= 0 and c < len(board[0])

def visit(to_visit, r, c, count):
  if count not in to_visit:
    to_visit[count] = []
  to_visit[count].append((r,c))

def identify_dirt(board, to_visit, drawable):
  while to_visit:
    r, c = to_visit.pop()
    if board[r][c] == '#':
      # already visited
      continue

    # up
    nr,nc   = (r-1, c)
    if bounded(board, nr, nc):
      if board[nr][nc] in ('|', '7', 'F') and board[r][c] in ('S', '|', 'L', 'J'):
        to_visit.add((nr,nc))

    # down
    nr, nc  = (r+1, c)
    if bounded(board, nr, nc):
      if board[nr][nc] in ('|', 'L', 'J') and board[r][c] in ('S', '|', '7', 'F'):
        to_visit.add((nr,nc))


    # left
    nr, nc  = (r, c-1)
    if bounded(board, nr, nc):
      if board[nr][nc] in ('-', 'L', 'F') and board[r][c] in ('S', '-', 'J', '7'):
        to_visit.add((nr,nc))

    # right
    nr, nc = (r, c+1)
    if bounded(board, nr, nc):
      if board[nr][nc] in ('-', 'J', '7') and board[r][c] in ('S', '-', 'L', 'F'):
        to_visit.add((nr,nc))

    drawable.render_char(r, c, board[r][c], color=(255,0,0))
    drawable.save()
    board[r][c] = '#'

  for r in range(len(board)):
    for c in range(len(board[r])):
      if board[r][c] != '#':
        board[r][c] = "."
  #for row in board:
  #  print("".join(row))
  return board


def dfs(board, visited, to_visit):
  while to_visit:
    start, orientation = to_visit.pop()
    if start in visited:
      # already visited
      continue
    else:
      visited[start] = True
     
    #if board[r][c] in ('|', '-', 'L', 'J', '7', 'F', '.', 'S'):
    #  board[r][c] = count
    #else:
    #  continue

    # up
    r,c = (start[0]-1, start[1])
    if bounded(board, r, c):
      if board[r][c] == '|':
        to_visit.add(((r, c), 0))
      if board[r][c] == '7':
        to_visit.add(((r, c), 0))
      if board[r][c] == 'F':
        to_visit.add(((r, c), 0))

    # down  = (start[0]+1, start[1])
    r, c = (start[0]+1, start[1])
    if bounded(board, r, c) and board[r][c] in ('|', 'L', 'J'):
      to_visit.add(((r, c), 0))

    # left
    r, c  = (start[0], start[1]-1)
    if bounded(board, r, c) and board[r][c] in ('-', 'L', 'F'):
      to_visit.add(((r, c), 0))

    # right
    r, c = (start[0], start[1]+1)
    if bounded(board, r, c) and board[r][c] in ('-', 'J', '7'):
      to_visit.add(((r, c), 0))


#  012
#  3#4
#  567

def stretch_vert(board):
  expanded = [board[0]]
  for r in range(1,len(board)):
    created = []
    for c in range(len(board[r])):
      above = board[r-1][c]
      below = board[r][c]
      if above == '|' or below == '|':
        created.append('|')
      elif below == 'L' or below == 'J':
        created.append('|')
      elif above == '7' or above == 'F':
        created.append('|')
      else:
        created.append('.')
    expanded.append(created)
    expanded.append(board[r])
  return expanded

def stretch_horiz(board):
  expanded = []
  for r in range(len(board)):
    expanded.append([board[r][0],])

  for c in range(1,len(board[0])):
    for r in range(len(board)):
      left = board[r][c-1]
      right = board[r][c]

      if left == '-' or right == '-':
        expanded[r].append('-')
      elif left == 'L' or left == 'F':
        expanded[r].append('-')
      elif right == 'J' or right == '7':
        expanded[r].append('-')
      else:
        expanded[r].append('.')
      expanded[r].append(right)
  return expanded

def flood(board, outside, to_visit, drawable):
  while to_visit:
    r, c = to_visit.pop()
    if (r,c) in outside:
      continue
    outside.add((r,c))
    drawable.render_char(r//2,c//2, "#", (0,0,255))
    drawable.save()

    for delta in ((-1,0), (1, 0), (0, -1), (0,1)):
      nr = r+delta[0]
      nc = c+delta[1]
      if bounded(board, nr, nc) and board[nr][nc] == '.':
        to_visit.add((nr,nc))

def part2(board, start, drawable):
  # Clean up board by separating extraneous pipe from actual loop
  dirt = identify_dirt(copy.deepcopy(board), set([start]), drawable)
  for r in range(len(dirt)):
    for c in range(len(dirt[r])):
      if dirt[r][c] == "." and board[r][c] != '.':
        board[r][c] = '.'
        drawable.render_char(r, c, '.') # ground always white
        drawable.save()

  board = stretch_vert(board)
  board = stretch_horiz(board)

  # Initialize 'outside' to known outside points
  to_visit = set()
  for r in (0, len(board)-1):
    for c in range(len(board[r])):
      if board[r][c] == '.':
        to_visit.add((r,c))
        drawable.render_char(r//2, c//2, '#', (0,0,255))
        drawable.save()
  for c in (0, len(board[0])-1):
    for r in range(len(board)):
      if board[r][c] == '.':
        to_visit.add((r,c))
        drawable.render_char(r//2, c//2, '#', (0,0,255))
        drawable.save()

  # Flood fill from outside to mark all outside points.
  outside = set()
  flood(board, outside, to_visit, drawable)
  for r,c in outside:
    board[r][c] = 'O'
  #for row in board:
  #  print("".join(row))

  # Count up all remaining background points - these must be inside.
  inside = 0
  for r in range(0, len(board), 2):
    for c in range(0, len(board[0]), 2):
      if board[r][c] == '.':
        drawable.render_char(r//2, c//2, '#', (0,255,0))
        drawable.save()
        inside += 1
  print("Inside:",inside)

def mymain(filename):
  data = aoc.lines(filename)
  board = make_board(data)
  drawable = render.DrawableBoard(
      len(board), len(board[0]),
      "/mnt/sda1/space/viz/board",
      sampling_interval=10)
  drawable.render_board(board)
  drawable.save()

  start = replace_start(board)

  part2(board, start, drawable)


aoc.run(mymain)

