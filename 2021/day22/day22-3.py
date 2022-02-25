#!/usr/bin/python3

import collections

import re
import sys
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc


class Interval(object):
  def __init__(self, lo, hi, offset=0):
    assert lo <= hi
    self.lo = lo
    self.hi = hi
    self.offset = offset

  def __repr__(self):
    return f'{self.lo}..{self.hi}'

  def intersection(self, other):
    return Interval(max(self.lo,other.lo),min(self.hi,other.hi))

  def overlaps(self, other):
    return ((self.lo <= other.lo and other.lo <= self.hi) or
            (self.lo <= other.hi and other.hi <= self.hi) or
            (other.lo <= self.lo and self.lo <= other.hi) or
            (other.lo <= self.hi and self.hi <= other.hi))

  def size(self):
    return self.hi-self.lo+1

  def is_small(self):
    return (self.lo >= -50 and
            self.hi >= -50 and
            self.lo <= 50 and
            self.hi <= 50)


class Cuboid(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def is_small(self):
    return self.x.is_small() and self.y.is_small() and self.z.is_small()
  
  def overlap(self, other):
    if self.x.overlaps(other.x) and self.y.overlaps(other.y) and self.z.overlaps(other.z):
      return Cuboid(self.x.intersection(other.x), self.y.intersection(other.y), self.z.intersection(other.z))

  def size(self):
    return self.x.size()*self.y.size()*self.z.size()

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
  return result


def handle_new_on(new_cube, working_set):
  result = [(new_cube.size(), new_cube)]
  for old_size, old_cube in working_set:
    overlap = new_cube.overlap(old_cube)
    if overlap is None:
      continue
    if old_size>0:
      # both 'on'; avoid double counting.
      result.append((-1*overlap.size(), overlap))
    else:
      result.append((overlap.size(), overlap))
  return result


def handle_new_off(new_cube, working_set):
  result = []
  for old_size, old_cube in working_set:
    overlap = new_cube.overlap(old_cube)
    if overlap is None:
      continue
    if old_size>0:
      # prior was 'on', now off.
      result.append((-1*overlap.size(), overlap))
    else:
      # we've turned these off already.
      result.append((overlap.size(), overlap))

  return result

def part2(rules, is_eligible):
  working_set = []
  for new_onoff, new_cube in rules:
    if not is_eligible(new_cube):
      continue
    to_update = []
    if new_onoff:
      working_set.extend(handle_new_on(new_cube, working_set))
    else:
      working_set.extend(handle_new_off(new_cube, working_set))

  total_size = 0
  for size, cube in working_set:
    total_size += size
  return total_size

def mymain(filename):
  data = aoc.lines(filename)
  rules = parse(data)

  print("Part 1", part2(rules, lambda x : x.is_small()))
  print("Part 2", part2(rules, lambda x: True))

aoc.run(mymain)

