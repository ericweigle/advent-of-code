#!/usr/bin/python3

import sys
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc


def find_start(data, num_chars):
  for i in range(0,len(data)):
    if len(set(x for x in data[i:i+num_chars])) == num_chars:
      print("    ",i+num_chars)
      return
  print("    No start of message")


def mymain(filename):
  data = aoc.lines(filename)

  print("  Part 1:", end="")
  find_start(data[0],num_chars=4)

  print("  Part 2", end="")
  find_start(data[0],num_chars=14)

aoc.run(mymain)

