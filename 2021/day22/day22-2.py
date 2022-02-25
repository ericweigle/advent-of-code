#!/usr/bin/python3

"""This was an attempt to do a multi-resolution map to encode the cuboids into a uniform set of ranges,
from which we could add and subtract with total overlaps. Got lost in the math and gave up in favor
of day22-3.py partial-overlapping solution."""

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc


class Interval(object):
  def __init__(self, lo, hi, offset=0):
    self.lo = lo
    self.hi = hi
    self.offset = offset

  def __repr__(self):
    return f'{self.lo}..{self.hi}'

  def equals(self, other):
    return self.lo == other.lo and self.hi == other.hi

  def intersection(self, other):
    return Interval(max(self.lo,other.lo),min(self.hi,other.hi))

  def shifted(self, amount):
    return Interval(self.lo+amount,self.hi+amount)

  def overlaps(self, other):
    return ((self.lo <= other.lo and other.lo <= self.hi) or
            (self.lo <= other.hi and other.hi <= self.hi) or
            (other.lo <= self.lo and self.lo <= other.hi) or
            (other.lo <= self.hi and self.hi <= other.hi))

  def is_small(self):
    return (self.lo >= -50 and
            self.hi >= -50 and
            self.lo <= 50 and
            self.hi <= 50)

  def make_positive(self):
    self.lo += 100000
    self.hi += 100000


class Cuboid(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def is_small(self):
    return self.x.is_small() and self.y.is_small() and self.z.is_small()
  
  def make_positive(self):
    return self.x.make_positive() and self.y.make_positive() and self.z.make_positive()

  def __repr__(self):
    return f'x={self.x},y={self.y},z={self.z}'


def parse(data):
  """Returns list of ((on/off, xrange, yrange,zrange), ...)"""
  def parse_ival(points):
    points = [int(v) for v in points.split('..')]
    return Interval(points[0],points[1])

  def parse_cube(ranges):
    ranges = re.sub('[xyz]=','',ranges)
    x, y, z = ranges.split(',')
    return Cuboid(parse_ival(x), parse_ival(y), parse_ival(z))

  result = []
  for line in data:
    onoff, points = line.split(" ")
    if onoff == 'on':
      onoff = True
    else:
      onoff = False
    result.append([onoff, parse_cube(points)])
  pprint.pprint(result)
  return result


def part1(rules):
  result = dict() 
  for onoff, cube in rules:
    print(f"Processing {cube}")
    if not cube.is_small():
      continue
    for x in range(cube.x.lo, cube.x.hi+1):
      for y in range(cube.y.lo, cube.y.hi+1):
        for z in range(cube.z.lo, cube.z.hi+1):
          if onoff:
            result[(x,y,z)]=True
          elif (x,y,z) in result:
            result.pop((x,y,z))
  print("Part 1:",len(result))


#def Pow2Interval(object):

def partition(interval, offset, maximum):
  #print(f"Partitioning {interval} offset {offset} max {maximum}")
  if interval.equals(Interval(0,maximum-1)):
    effective = Interval(interval.lo+offset,interval.hi+offset)
    print(f"power-of-2 interval f{interval} at {offset} --> {effective}")
    return

  assert interval.lo>=0 and interval.hi < maximum and 2*(maximum//2)==maximum

  splitpoint = maximum // 2
  left = Interval(0,splitpoint-1)
  right = Interval(splitpoint, maximum)
  if left.overlaps(interval):
    #print("Recurse left.")
    partition(interval.intersection(left), offset, splitpoint)
  if right.overlaps(interval):
    #print("Recurse right.")
    partition(interval.intersection(right).shifted(-splitpoint),offset+splitpoint, splitpoint)


#def partition(interval:Interval, splitpoint:int):
#  if splitpoint >= interval.lo and splitpoint<interval.hi:
#    left = Interval(interval.lo, splitpoint)
#    right = Interval(splitpoint+1, interval.hi)
#    return (left, right)

#def power_of_two_interval(order: int, offset: int):
#  """Get an interval that's a power-of-two given minimum value and order.
#
#  order == 18:  [0 ... 2^18)
#  order == 17:  [0 ... 2^17)[2^17 ... 2^18)
#  order == 16:  [0 ... 2^16)[2^16 ... 2^17)...
#  ...
#  order = 1: [0,2)[2,4)[4,6)
#  order = 0: [0,1)[1,2)[2,3)
#  """
#  return Interval(offset, offset + (2**order)-1)

def part2(rules):
  """Returns list of ((on/off, xrange, yrange,zrange), ...)"""
  # Makes everything in [0,...] quadrant.
  for _, cube in rules:
    cube.make_positive()


partition(Interval(100,200),0,1024)
#def mymain(filename):
#  data = aoc.lines(filename)
#  rules = parse(data)
#
#  print("Part 1")
#  part1(rules)
#
#  print("Part 2")
#  part2(rules)
#
#aoc.run(mymain)
#
