#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc

class Interval(object):
  def __init____(self, lo, hi):
    assert hi < 200000
    assert lo > 0
    self.lo = lo
    self.hi = hi

  def overlaps(other):
    return ((self.lo <= other.lo and other.lo <= self.hi) or
            (self.lo <= other.hi and other.hi <= self.hi) or
            (other.lo <= self.lo and self.lo <= other.hi) or
            (other.lo <= self.hi and self.hi <= other.hi))

def parse(data):
  """Returns list of ((on/off, xrange, yrange,zrange), ...)"""
  result = []
  for line in data:
    onoff, points = line.split(" ")
    points = re.sub('[xyz]=','',points)
    x, y, z = points.split(',')
    x = [int(v) for v in x.split('..')]
    y = [int(v) for v in y.split('..')]
    z = [int(v) for v in z.split('..')]
    if onoff == 'on':
      onoff = True
    else:
      onoff = False
    result.append([onoff, x, y, z])
  pprint.pprint(result)
  return result

def is_small_range(v_range):
  return (v_range[0] >= -50 and
          v_range[1] >= -50 and
          v_range[0] <= 50 and
          v_range[1] <= 50)

def is_small_cube(x, y, z):
  return is_small_range(x) and is_small_range(y) and is_small_range(z)

def part1(data):
  rules = parse(data)
  result = dict() 
  for onoff, x_range, y_range, z_range in rules:
    print(f"Processing {x_range} {y_range} {z_range}")
    if not is_small_cube(x_range, y_range, z_range):
      continue
    for x in range(x_range[0], x_range[1]+1):
      for y in range(y_range[0], y_range[1]+1):
        for z in range(z_range[0], z_range[1]+1):
          if onoff:
            result[(x,y,z)]=True
          elif (x,y,z) in result:
            result.pop((x,y,z))
  print("Part 1:",len(result))

def mymain(filename):
  data = aoc.lines(filename)

  print("Part 1")
  part1(data)

aoc.run(mymain)

