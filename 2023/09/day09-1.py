#!/usr/bin/python3

import sys
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc

def all_zeros(l):
  for x in l:
    if x != 0:
      return False
  return True

def make_history(seq):
  result = []
  result.append(seq)
  while not all_zeros(result[-1]):
    x = result[-1]
    result.append(list([x[i+1]-x[i] for i in range(len(x)-1)]))
  return result

def unchain_r(history):
  history[-1].append(0)
  for i in range(len(history)-1, 0, -1):
    history[i-1].append(history[i][-1] + history[i-1][-1])
  return history

def unchain_l(history):
  history[-1].insert(0,0)
  for i in range(len(history)-1, 0, -1):
    history[i-1].insert(0, history[i-1][0] - history[i][0])
  return history

def part1(data):
  total = 0
  for seq in data:
    result = make_history(seq)
    result = unchain_r(result)
    total += result[0][-1]
  print("Part 1 Total",total)

def part2(data):
  total = 0
  for seq in data:
    result = make_history(seq)
    result = unchain_l(result)
    total += result[0][0]
  print("Part 2 Total", total)

def mymain(filename):
  data = aoc.lines(filename)
  data = [x.split() for x in data]
  result = []
  for line in data:
    result.append([int(x) for x in line])
  data = result

  part1(data)
  part2(data)

aoc.run(mymain)

