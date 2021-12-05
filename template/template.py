#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)

def parse(filename):
  return [x.strip() for x in open(filename, 'r').readlines()]

def part1(data):
  pass

def part2(data):
  pass

for filename in sys.argv[1:]:
  print(f"For file '{filename}'")
  data = parse(filename)

  part1(copy.deepcopy(data))
  part2(data)
