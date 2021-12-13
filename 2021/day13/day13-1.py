#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc

def parse(data):
  dots = set()
  folds = []
  for line in data:
    if ',' in line:
      dots.add(tuple([int(x) for x in line.split(',')]))
    if 'fold' in line:
      folds.append(line.split(' ')[-1].split('='))
      folds[-1][-1] = int(folds[-1][-1])
  return dots, folds


def dump(dots):
  max_x = max([x for x, y in dots])+1
  max_y = max([y for x, y in dots])+1
  for y in range(0,max_y):
    for x in range(0,max_x):
      if (x,y) in dots:
        print('#', end='')
      else:
        print('.',end='')
    print()

def fold_y(dots, fold_point):
  result = set()
  for x, y in dots:
    if y < fold_point:
      result.add(tuple([x,y]))
    elif y > fold_point:
      new_y = 2*fold_point - y
      result.add(tuple([x, new_y]))
  return result

def fold_x(dots, fold_point):
  result = set()
  for x, y in dots:
    if x < fold_point:
      result.add(tuple([x,y]))
    elif x > fold_point:
      new_x = 2*fold_point - x
      result.add(tuple([new_x, y]))
  return result

def part1(dots, folds):
  for xy, fold_point in folds:
    if xy == 'x':
      dots = fold_x(dots, fold_point)
    elif xy == 'y':
      dots = fold_y(dots, fold_point)
    return len(dots)

def part2(dots, folds):
  for xy, fold_point in folds:
    if xy == 'x':
      dots = fold_x(dots, fold_point)
    elif xy == 'y':
      dots = fold_y(dots, fold_point)
    else:
      assert False
  dump(dots)

def mymain(filename):
  data = aoc.lines(filename)
  dots, folds = parse(data)

  print("Part 1")
  print(part1(copy.deepcopy(dots), copy.deepcopy(folds)))

  print("Part 2")
  part2(dots, folds)

aoc.run(mymain)

