#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc


def visit(mymap, quota, node, cur_path):
  cur_path.append(node)

  count = 0
  for neighbor in mymap[node]:
    if neighbor == 'end':
      #print('->'.join(cur_path + ['end']))
      count += 1
    elif quota[neighbor] > 0:
      quota[neighbor] -= 1
      count += visit(mymap, quota, neighbor, cur_path + [neighbor])
      quota[neighbor] += 1
    elif quota[neighbor] == 0 and quota['bonus'] > 0:
      quota['bonus'] -= 1
      count += visit(mymap, quota, neighbor, cur_path + [neighbor])
      quota['bonus'] += 1
  cur_path.pop(-1)
  return count

def part1(mymap):
  quota = dict([(x,99999999 if x.lower() != x else 1) for x in mymap.keys()])
  quota['start'] = -1
  quota['bonus'] = 0
  count = visit(mymap, quota, 'start', [])
  print("Total:",count)

def part2(mymap):
  quota = dict([(x,99999999 if x.lower() != x else 1) for x in mymap.keys()])
  quota['start'] = -1
  quota['bonus'] = 1
  count = visit(mymap, quota, 'start', [])
  print("Total:",count)


def build_map(filename):
  data = aoc.lines(filename)
  data = [x.split('-') for x in data]
  mymap = collections.defaultdict(list)
  for start, end in data:
    mymap[start].append(end)
    mymap[end].append(start)
  #pprint.pprint(mymap)
  return mymap

def mymain(filename):
  mymap = build_map(filename)

  print("Part 1")
  part1(mymap)

  print("Part 2")
  part2(mymap)

aoc.run(mymain)

