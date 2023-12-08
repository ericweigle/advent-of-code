#!/usr/bin/python3

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


def part1(dirs, nodes):
  node = "AAA"
  steps = 0
  while node != "ZZZ":
    d = dirs[steps % len(dirs)]
    if d == 'L':
      next_node = nodes[node][0]
    elif d == 'R':
      next_node = nodes[node][1]
    else:
      raise ValueError("die")
    node = next_node
    steps += 1
  print(f"Reached ZZZ in {steps}")

def mymain(filename):
  dirs, nodes = parse_file(filename)

  print("Part 1")
  part1(dirs, nodes)

aoc.run(mymain)
