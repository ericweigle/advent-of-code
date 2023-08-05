#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
# sudo apt-get install python3-intervaltree
from intervaltree import IntervalTree
from intervaltree import Interval

sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc

def parse_line(line):
  m = re.match("^Sensor at x=([0-9-]*), y=([0-9-]*): closest beacon is at x=([0-9-]*), y=([0-9-]*)$", line.strip())
  if not m:
    print(f"failed to match {line}")
    sys.exit(1)
  sensor = (int(m.group(1)), int(m.group(2)))
  beacon = (int(m.group(3)), int(m.group(4)))
  #print(sensor,beacon)
  return (sensor,beacon)

def parse_input(filename):
  lines = [parse_line(x) for x in aoc.lines(filename)]
  #pprint.pprint(lines)
  return lines

def manhattan_distance(a, b):
  return abs(a[0]-b[0]) + abs(a[1]-b[1])

def get_overlap(sensor, beacon, y):
  """Find the overlap window for a fixed line. Returns [x0, x1] inclusive."""
  d1 = manhattan_distance(sensor, beacon)
  d2 = manhattan_distance(sensor, (sensor[0],y))
  if d2 > d1:
    #print(f"NOT Candidate {sensor},{beacon},{d}")
    return None

  width = d1 - abs(y - sensor[1])
  #print(f"Candidate sensor {sensor}, beacon {beacon}, d1 {d1}, d2 {d2} width {width}")
  return sensor[0] - width, sensor[0] + width

#for y in range(-3, 18):
#  print(f"y: {y} overlap:", get_overlap((8,7),(2,10),y))
#
#assert get_overlap((8,7),(2,10),y=-2) == (8,8)
#assert get_overlap((8,7),(2,10),y=-1) == (7,9)
#assert get_overlap((8,7),(2,10),y=0) == (6,10)
#assert get_overlap((8,7),(2,10),y=1) == (5,11)
#assert get_overlap((8,7),(2,10),y=6) == (0,16)
#assert get_overlap((8,7),(2,10),y=7) == (-1,17)
#assert get_overlap((8,7),(2,10),y=8) == (0,16)


def build_tree(sensors_and_beacons, y):
  tree = IntervalTree()
  for sensor,beacon in sensors_and_beacons:
    overlap = get_overlap(sensor, beacon, y)
    if overlap is not None:
      # Intervals here are [closed,open)
      tree.add(Interval(overlap[0],overlap[1]+1))
  tree.merge_overlaps(strict=False)
  return tree

def part1(filename, y):
  tree = build_tree(parse_input(filename), y)
  #print(tree)
  print("Part1",filename, sum([abs((x[1]-1)-x[0]) for x in tree]))


def tuning_freq(x, y):
  return x*4000000 + y

def part2(filename, start, end):
  sensors_and_beacons = parse_input(filename)
  for y in range(start, end):
    #if y % 1000 == 0:
    #  print("up to",y)
    tree = build_tree(sensors_and_beacons, y)
    if len(tree) != 1:
      assert(len(tree) == 2)
      #print(tree)
      a, b = list([(x[0],x[1]) for x in tree])
      if a[0] > b[0]:
        c = a
        a = b
        b = c
      #print(a,b)
      print("Part 2:", tuning_freq(a[1], y))
      return

print("--Part 1---")
part1("example", y=10)
part1("input", y=2000000)
print("--Part 2--")
part2("example", 0, 20)
#part2("input", 0, 4000000)
part2("input", 2703000, 2704000)

