#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc

def parse_line(line):
  xys = line.split(" -> ")
  result = []
  for point in xys:
    result.append([int(x) for x in point.split(",")])
  return result

def draw_line(start, end, board):
  if start[0] == end[0]:
    # vertical
    x = start[0]
    for y in range(min(start[1],end[1]), max(start[1],end[1])+1):
      board[(x,y)] = '#'
  elif start[1] == end[1]:
    # horiz
    y = start[1]
    for x in range(min(start[0],end[0]), max(start[0],end[0])+1):
      board[(x,y)] = '#'
  else:
    raise ValueError("Not horiz or vert")

def draw_board(board):
  min_x = min(x[0] for x in board.keys())
  max_x = max(x[0] for x in board.keys())
  min_y = min(x[1] for x in board.keys())
  max_y = max(x[1] for x in board.keys())
  for y in range(min_y, max_y+1):
    line = []
    for x in range(min_x, max_x+1):
      line.append(board.get((x,y), '.'))
    print("".join(line))

def make_board(lines):
  board = dict()
  for line in lines:
    for i in range(0,len(line)-1):
      start = line[i]
      end = line[i+1]
      draw_line(start, end, board)
  #pprint.pprint(board.keys())
  return board

def parse_input(filename):
  lines = [parse_line(x) for x in aoc.lines(filename)]
  #pprint.pprint(lines)
  board = make_board(lines)
  #draw_board(board)
  return board

def drop_sand(board,max_y):
  x = 500
  y = 0
  if (x,y) in board:
    return
  
  for loop in range(9999999):
    # move down one
    if (x,y+1) not in board:
      y = y+1
    elif (x-1,y+1) not in board:
      x = x-1
      y = y+1
    elif (x+1,y+1) not in board:
      x = x+1
      y = y+1
    else:
      # at rest
      board[(x,y)] = 'o'
      return True

    if y > max_y:
      print("Fell off the edge")
      return False


def part1(filename):
  board = parse_input(filename)
  max_y = max(xy[1] for xy in board.keys())
  for drop in range(1,99999):
    if not drop_sand(board,99999999):
      print(f"Terminated at {drop-1}")
      #draw_board(board)
      #print("")
      return


def part2(filename):
  board = parse_input(filename)
  max_y = max(xy[1] for xy in board.keys())
  floor = max_y + 2
  for x in range(-2000,2000):
    board[(x,floor)] = 'X'

  for drop in range(1,99999):
    if not drop_sand(board,floor+1):
      print(f"Terminated at {drop-1}")
      #draw_board(board)
      #print("")
      return



def mymain(filename):
  print("Part 1")
  part1(filename)
  print("Part 2")
  part2(filename)

aoc.run(mymain)
