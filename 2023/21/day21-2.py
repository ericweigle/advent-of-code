#!/usr/bin/python3

import collections

import code
import itertools
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
    board.append([x for x in row])
  for row in range(len(board)):
    for column in range(len(board[row])):
      if board[row][column] == 'S':
        start = (row,column)
  return start, board

def get(board, r, c):
  rows = len(board)
  cols = len(board[0])
  r = (r + rows*(abs(r)//rows + 10)) % rows
  c = (c + cols*(abs(c)//cols + 10)) % cols
  return board[r][c]

def step_pt1(board, positions):
  result = set()
  for row,column in positions:
    for rd, cd in ((-1,0), (1,0), (0,-1), (0,1)):
      nr = row + rd
      nc = column + cd
      if get(board, nr,nc) != '#':
        result.add((nr,nc))
  return result

def pairwise_diff(mylist):
  return [x[1]-x[0] for x in itertools.pairwise(mylist)]

def part2(start, board):
  cache = dict()
  cache[1] = 1

  # Seed position cache
  pos_cache = dict()
  pos_cache[0] = set([start,])
  pos_cache[1] = step_pt1(board, pos_cache[0])

  size_cache = dict()
  size_cache[0] = 1
  size_cache[1] = len(pos_cache[1])

  # Observation: Every position reachable at step I is reachable at I+2.
  # So we don't need to repeatedly calculate that stuff.
  for i in range(2,500):
    pos_cache[i] = step_pt1(board, pos_cache[i-1]).difference(pos_cache[i-2])
    size_cache[i] = size_cache[i-2]+len(pos_cache[i])
    print(f"step {i} options {size_cache[i]} working set {len(pos_cache[i])}")
    del pos_cache[i-2]
    #del size_cache[i-2]

  sizes = [size_cache[x] for x in sorted(size_cache.keys())]

  # Validate that we have a constant 2nd derivative 
  # f(n) = A*x^2 + B*x + C
  # f'(n) = 2*A*X + B
  # f''(n) = 2*A   <<< calculating this by double diff
  #sliced = sizes[0::131]
  sliced = sizes[65::131]
  A = set(pairwise_diff(pairwise_diff(sliced)))
  assert len(A) == 1
  A = A.pop()
  assert A % 2 == 0

  def get_slice_index(index, sliced):
    """Synthetic function to simulate an infinite 'sliced' array"""
    if index <2:
      return sliced[index]
    total = sliced[1]
    delta = sliced[1]-sliced[0]
    delta_delta = (sliced[2]-sliced[1])-(sliced[1]-sliced[0])
    for i in range(1,index):
      delta += delta_delta
      total += delta
      #print(i,delta,total)
    return total

  # Target = 26501365
  #     26501300       + 65
  #     202300*131     + 65
  #     ^sliced[202300] ^==sliced[1]=65

  # 619407349431167
  print(get_slice_index(202300,sliced))

def mymain(filename):
  start, board = mkboard(aoc.lines(filename))

  print("Part 2")
  part2(start, board)

aoc.run(mymain)
