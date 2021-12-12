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
    if node in small_visited and node != 'start':
      visited['consumed'] = True
    else:
      visited[node] = True
  else:
    visited = small_visited

  count = 0
  for neighbor in mymap[node]:
    if neighbor == 'end':
      print('->'.join(cur_path + ['end']))
      count += 1
    elif neighbor.lower() == neighbor:
      if (neighbor not in visited) or (neighbor in visited and not visited['consumed'] and neighbor != 'start'):
        count += visit(mymap, visited, neighbor, cur_path + [neighbor])
      else:
        pass # previously visit
    else:
      count += visit(mymap, visited, neighbor, cur_path + [neighbor])
  return count


def part2(mymap):
  count = visit(mymap, {'start':10, 'consumed':False}, 'start', ['start'])
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

  print("Part 2")
  part2(mymap)

aoc.run(mymain)
