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

def get_board(data):
  result =[]
  for line in data:
    result.append([x for x in line])
  return result


def dump_board(board, beams):
  dump = copy.deepcopy(board)
  for r in range(len(board)):
    for c in range(len(board[r])):
      if (r,c) in beams:
        if len(beams[(r,c)]) == 1:
          dump[r][c] = {'l':'<','r':'>','u':'^','d':'v'}[beams[(r,c)][0]]
        else:
          dump[r][c] = str(len(beams[(r,c)]))
  for line in dump:
    print("".join(line))


def run_beams(board, to_visit):
  beams = dict()
  while to_visit:
    #dump_board(board, beams)
    #print("\n\n")
    r,c,d = to_visit.pop()
    if r<0 or r>=len(board) or c<0 or c>=len(board[0]):
      continue

    if (r,c) in beams:
      if d in beams[(r,c)]:
        continue
      else:
        beams[(r,c)].append(d)
    else:
      beams[(r,c)] = [d]

    if board[r][c] == '.':
      if d == 'u':
        to_visit.append((r-1,c,d))
      elif d == 'd':
        to_visit.append((r+1,c,d))
      elif d == 'l':
        to_visit.append((r,c-1,d))
      elif d == 'r':
        to_visit.append((r,c+1,d))
    elif board[r][c] == '-':
      if d == 'u' or d == 'd':
        to_visit.append((r,c-1,'l'))
        to_visit.append((r,c+1,'r'))
      elif d == 'l':
        to_visit.append((r,c-1,'l'))
      elif d == 'r':
        to_visit.append((r,c+1,'r'))
    elif board[r][c] == '|':
      if d == 'u':
        to_visit.append((r-1,c,'u'))
      elif d == 'd':
        to_visit.append((r+1,c,'d'))
      elif d == 'l' or d == 'r':
        to_visit.append((r-1,c,'u'))
        to_visit.append((r+1,c,'d'))
    elif board[r][c] == '/':
      if d == 'u':
        to_visit.append((r,c+1,'r'))
      elif d == 'd':
        to_visit.append((r,c-1,'l'))
      elif d == 'l':
        to_visit.append((r+1,c,'d'))
      elif d == 'r':
        to_visit.append((r-1,c,'u'))
    elif board[r][c] == '\\':
      if d == 'u':
        to_visit.append((r,c-1,'l'))
      elif d == 'd':
        to_visit.append((r,c+1,'r'))
      elif d == 'l':
        to_visit.append((r-1,c,'u'))
      elif d == 'r':
        to_visit.append((r+1,c,'d'))
  return beams


def part1(board):
  beams = dict()
  #dump_board(board, beams)
  beams = run_beams(board, [(0,0,'r')])
  energized = sum([1 for key in beams if beams[key]])
  print("Energized",energized)
  #dump_board(board, beams)


def part2(board):
  beams = dict()
  energized = []
  for row in range(len(board)):
    beams = run_beams(board, [(row,0,'r')])
    energized.append(sum([1 for key in beams if beams[key]]))
    beams = run_beams(board, [(row,len(board[0])-1,'l')])
    energized.append(sum([1 for key in beams if beams[key]]))
  for col in range(len(board[0])):
    beams = run_beams(board, [(0,col,'d')])
    energized.append(sum([1 for key in beams if beams[key]]))
    beams = run_beams(board, [(len(board)-1,col,'u')])
    energized.append(sum([1 for key in beams if beams[key]]))
  print("Energized",max(energized))


def mymain(filename):
  board = get_board(aoc.lines(filename))

  print("Part 1")
  part1(board)

  print("Part 2")
  part2(board)

aoc.run(mymain)

