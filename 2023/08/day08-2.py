#!/usr/bin/python3

import math
import parse
import sys
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc


def parse_file(filename):
  with open(filename, 'r') as f:
    data = f.read()
  directions, nodes = data.split("\n\n")
  directions = directions.strip()
  output = dict()
  for line in nodes.splitlines():
    key, left, right = parse.parse("{} = ({}, {})", line)
    assert key not in output
    output[key] = (left, right)
  return directions, output

def get_period(dirs, nodes, node):
  steps = 0
  terminals = []
  while True:
    bound_step = steps % len(dirs)
    d = dirs[bound_step]
    if len(terminals) > 10:
      return terminals
    if node.endswith("Z"):
      terminals.append(steps)
    if d == 'L':
      node = nodes[node][0]
    elif d == 'R':
      node = nodes[node][1]
    else:
      raise ValueError("die")
    steps += 1
 
def part2(dirs, nodes):
  node = [x for x in nodes.keys() if x.endswith('A')]
  print(f"Found {len(node)} start nodes.")

  numbers = []
  for i in range(len(node)):
    p = get_period(dirs, nodes, node[i])
    #print(f"Period of start node {i} is {p}")
    deltas = [p[i+1]-p[i] for i in range(len(p)-1)]
    #print(f"Deltas: {deltas}")
    numbers.append(p[0])
  print(math.lcm(*numbers))


def mymain(filename):
  dirs, nodes = parse_file(filename)

  print("Part 2")
  part2(dirs, nodes)

aoc.run(mymain)

