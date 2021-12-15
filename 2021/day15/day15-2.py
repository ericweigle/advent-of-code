#!/usr/bin/python3

import collections

import heapq
import sys
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc

def neighbors(row, col, data):
  """From day 9"""
  if row > 0:
    yield (row-1,col)
  if row < (len(data)-1):
    yield (row+1,col)
  if col > 0:
    yield (row,col-1)
  if col < (len(data[0])-1):
    yield (row,col+1)


def bfs(board):
  myqueue = []
  path = [(0,0),]
  entries = collections.defaultdict(list)
  heapq.heappush(myqueue, 0)
  entries[0] = [path]

  bests = dict()
  bests[(0,0)] = 0
  while myqueue:
    cost = heapq.heappop(myqueue)
    path = entries[cost].pop(0)
    #print("path",path)
    for x,y in neighbors(path[-1][0], path[-1][1], board):
      if x==len(board)-1 and y == len(board)-1:
        return cost+board[x][y]
      if (x,y) not in path: 
        newcost = cost+board[x][y]
        if (x,y) in bests and bests[(x,y)] <= newcost:
          # prune inefficient paths
          continue
        bests[(x,y)] = newcost
        newpath = [(x,y)]
        heapq.heappush(myqueue, newcost)
        entries[newcost].append(newpath)


def expand(board):
  dim = len(board)
  newboard = []
  for x in range(5*dim):
    newboard.append([0]*5*dim)
    for y in range(5*dim):
      if x < dim and y < dim:
        newboard[x][y] = board[x][y]
      else:
        v = (board[x % dim][y % dim]+
             x//dim + y//dim ) # tile
        while v > 9:
          v -= 9
        newboard[x][y] = v
  return newboard


def mymain(filename):
  data = aoc.lines(filename)
  board = [[int(x) for x in line] for line in data]

  print("Part 1")
  print(bfs(board))

  print("Part 2")
  print(bfs(expand(board)))

aoc.run(mymain)

