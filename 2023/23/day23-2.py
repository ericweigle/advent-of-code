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
    cols = []
    for col in row:
      cols.append('#' if col == '#' else '.')
    board.append(cols)
  start = (0,1)

  end_row = len(board)-1
  end_col = len(board[end_row])-2
  return board, start, (end_row, end_col)

def valid(pt, board):
  return pt[0] >= 0 and pt[0] < len(board) and pt[1] >= 0 and pt[1] < len(board[pt[0]]) and board[pt[0]][pt[1]] != '#'

def neighbors(row, col, board):
  up    = (row-1, col)
  down  = (row+1, col)
  left  = (row, col-1)
  right = (row, col+1)

  result = []
  if valid(up, board):
    result.append(up)
  if valid(down, board):
    result.append(down)
  if valid(left, board):
    result.append(left)
  if valid(right, board):
    result.append(right)
  return result

def dump(board, visited):
  for row in range(len(board)):
    output = []
    for col in range(len(board[row])):
      if (row, col) in visited:
        output.append("O")
      else:
        output.append(board[row][col])
    print("".join(output))

def preprocess_to_nodes(board, start, nodes):
  if start not in nodes:
    nodes[start] = []
  row, column = start
  length = 0
  while True:
    board[row][column] = '#'
    to_visit = neighbors(row, column, board)

    if not to_visit:
      # Dead end!
      nodes[start].append([length+1, (row,column)])
      print(f"Dead end at {(row,column)}")
      return
    if len(to_visit) == 1:
      # walking a chain
      print(f"Walking chain length {length} from {start} now at {to_visit}")
      length += 1
      row, column = to_visit[0]
    else:
      print(f"Node at {(row, column)}, {length}, {to_visit}")
      # hit a new node
      board[row][column] = '#'
      for neighbor in to_visit:
        nodes[start].append([length+1, neighbor])
        preprocess_to_nodes(board, neighbor, nodes)

def follow_edge(board, start, nodes):
  length = 1
  row, column = start

  marked = set()
  while True:
    board[row][column] = '#'
    marked.add((row,column))
    to_visit = neighbors(row, column, board)
    if len(to_visit) > 1:
      print(f"Hit unexpected node at {(row, column)}, with {to_visit} from {start}")
      assert len(to_visit) == 1
    row, column = to_visit[0]
    length += 1

    if (row, column) in nodes:
      for r,c in marked:
        board[r][c] = '.'
      return length, (row, column), marked

def dfs(nodes, visited, start, end):
  visited.add(start)
  longest = 0
  best = []
  for dist, neighbor in nodes[start]:
    if neighbor in visited:
      continue
    if neighbor == end:
      if dist > longest:
        longest = dist
        best = [start, end, dist]
    else:
      putative_longest, putative_best = dfs(nodes, visited, neighbor, end)
      if (dist + putative_longest) > longest and putative_best:
        longest = (dist + putative_longest)
        best = [(start, neighbor, dist)] + putative_best
  visited.remove(start)
  return longest, best

def part2(data):
  board, start, end = mkboard(data)
  #dump(board, set())

  nodes = dict()
  nodes[start] = []
  nodes[end] = []
  for row in range(len(board)):
    for col in range(len(board[row])):
      asdf = neighbors(row, col, board)
      if board[row][col] == '.' and len(asdf)>2:
        #print(f"Neighbors at {row},{col} == {asdf}")
        nodes[(row,col)] = []
  #print(f"Found {len(nodes)} nodes:")
  #pprint.pprint(nodes)
  dump(board, nodes)

  for node in nodes:
    row, column = node
    board[row][column] = '#'
    for neighbor in neighbors(row, column, board):
      length, next_node, points = follow_edge(board, neighbor, nodes)
      nodes[node].append([length, next_node]) # , points
    board[row][column] = '.'
  print("Final graph")
  pprint.pprint(nodes)

  print(f"Start is {start}, end is {end}")
  longest, route = dfs(nodes, visited=set(), start=start, end=end)
  print(f"Longest is {longest}, {route}")
  

#  preprocess_to_nodes(board, start, nodes)
#  pprint.pprint(nodes)

def mymain(filename):
  data = aoc.lines(filename)

  print("Part 1")
  part2(data)

aoc.run(mymain)

