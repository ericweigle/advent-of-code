#!/usr/bin/python3

import sys

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)

def fuel_pt1(data, pos):
  return sum(abs(pos-crab) for crab in data)

def fuel_pt2(data, pos):
  return sum(abs(pos-crab)*(abs(pos-crab)+1)/2
      for crab in data)

def part1(data):
  solutions = []
  for i in range(min(data),max(data)+1): 
    solutions.append((fuel_pt1(data,i), i))
  print("part 1:",min(solutions)[0])

def part2(data):
  solutions = []
  for i in range(min(data),max(data)+1): 
    solutions.append((fuel_pt2(data,i), i))
  print("part 2:",min(solutions)[0])

for filename in sys.argv[1:]:
  print(f"For file '{filename}'")
  lines = [x.strip() for x in open(filename, 'r').readlines()]
  data = [int(x) for x in lines[0].split(',')]

  part1(data)
  part2(data)
