#!/usr/bin/python3

import collections

import heapq
import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc


def neighbors(row, col, data):
  """From day 9"""
  val = []
  if row > 0:
    val.append((row-1,col))
  if row < (len(data)-1):
    val.append((row+1,col))
  if col > 0:
    val.append((row,col-1))
  if col < (len(data[0])-1):
    val.append((row,col+1))
  return val
 
def popit(myqueue):
  best = min([x[0] for x in myqueue])
  for i in range(len(myqueue)):
    if myqueue[i][0] == best:
      return myqueue.pop(i)

def bfs(board):
  myqueue = []
  path = [(0,0),]
  #heapq.heappush(myqueue, (0, path))
  myqueue.append((0, path,))
  bests = dict()
  bests[(0,0)] = 0
  while myqueue:
    #cost, path = heapq.heappop(myqueue)
    cost, path = popit(myqueue)
    for x,y in neighbors(path[-1][0], path[-1][1], board):
      if x==len(board)-1 and y == len(board)-1:
        return cost+board[x][y]
      if (x,y) not in path: 
        newcost = cost+board[x][y]
        if (x,y) in bests and bests[(x,y)] <= newcost:
          # prune inefficient paths
          continue
        bests[(x,y)] = newcost
        newpath = copy.deepcopy(path)
        newpath.append((x,y))
        #print("New path",newpath)
        #heapq.heappush(myqueue, (cost+board[x][y], newpath))
        #print('  cost',cost)
        #print('  board',board[x][y])
        myqueue.append((cost+board[x][y], newpath,))


def mymain(filename):
  data = aoc.lines(filename)
  board = [[int(x) for x in line] for line in data]
  #pprint.pprint(board)

  print("Part 1")
  print(bfs(board))

aoc.run(mymain)

