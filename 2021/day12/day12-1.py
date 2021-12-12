#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc


def visit(mymap, small_visited, node, cur_path):
  if node.lower() == node:
    visited = copy.copy(small_visited)
    visited.add(node)
  else:
    visited = small_visited

  count = 0
  for neighbor in mymap[node]:
    if neighbor == 'end':
      print('->'.join(cur_path + ['end']))
      count += 1
    elif neighbor.lower() == neighbor:
      if neighbor not in visited:
        count += visit(mymap, visited, neighbor, cur_path + [neighbor])
      else:
        pass # previously visit
    else:
      count += visit(mymap, visited, neighbor, cur_path + [neighbor])
  return count


def part1(mymap):
  count = visit(mymap, set(['start']), 'start', ['start'])
  print("Total:",count)

def mymain(filename):
  data = aoc.lines(filename)
  data = [x.split('-') for x in data]
  mymap = dict()
  for start, end in data:
    if start in mymap:
      mymap[start].append(end)
    else:
      mymap[start] = [end]
    if end in mymap:
      mymap[end].append(start)
    else:
      mymap[end] = [start]

  pprint.pprint(mymap)

  print("Part 1")
  part1(mymap)

aoc.run(mymain)
