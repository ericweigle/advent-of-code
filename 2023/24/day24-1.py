#!/usr/bin/python3

import collections

import copy
import math
import pprint
import re
import sys
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc

def to_xy_formula(pt, slope):
  """Convert point, slope formula to slope-intercept y=mx+b formula. Return (m, b)"""
  x1, y1, _ = pt
  dx1, dy1, _ = slope

  #x = x1 + dx1*t  --> t = (x-x1)/dx1
  #y = y1 + dy1*t  --> t = (y-y1)/dy1
  # (x-x1)/dx1 = (y-y1)/dy1
  # (y-y1) = (dy1/dx1)(x-x1)
  # y = (dy1/dx1)(x) - (dy1/dx)*x1 + y1
  m = (dy1 / dx1)
  b = y1-m*x1
  return (m,b)

def intersect_slope_intercept(m1, b1, m2, b2):
  if m1 == m2:
    return (None, None)  # parallel
  # y = m1*x + b1
  # y = m2*x + b2
  # m1*x + b1 == m2*x + b2
  # (m1-m2)*x = (b2-b1)
  # x = (b2-b1)/(m1-m2)
  # y = m1*x + b1
  x = (b2-b1)/(m1-m2)
  y = m1*x + b1
  return (x,y)

def get_time(x, y, pt, slope):
  # x = pt[0] + slope[0]*t
  # t = (x-pt[0]) / slope[0]
  t1 = (x-pt[0]) / slope[0]
  t2 = (y-pt[1]) / slope[1]
  if not math.isclose(t1, t2, rel_tol=1e-10):
    print(f"Time mismatch {t1}")
    print(f"Time mismatch {t2}")
    assert t1 == t2
  return t1


#def intersect(coord, first, second, bounds):
#  #  (19, 13, 30), (-2,  1, -2)
#  #  (18, 19, 22), (-1, -1, -2)
#  # A*t + B == C*t + D
#  # t == (D-B)/(A-C)
#  A = first[1][coord]
#  B = first[0][coord]
#  C = second[1][coord]
#  D = second[0][coord]
#  if A==C:
#    #parallel lines
#    if B == D:
#      return (True, None)
#    else:
#      return (False, None)
#  t = (D-B)/(A-C)

def parseit(data):
  result = []
  for line in data:
    pos, vel = line.split('@')
    pos = pos.strip()
    vel = vel.strip()
    pos = tuple([int(x) for x in pos.split(",")])
    vel = tuple([int(x) for x in vel.split(",")])
    result.append((pos,vel))
  return result

def hailstone(tuples):
  return f"{tuples[0][0]}, {tuples[0][1]}, {tuples[0][2]} @ {tuples[1][0]}, {tuples[1][1]}, {tuples[1][2]}"

def find_intersections(data, bbox, verbose=False):
  count = 0
  for a in range(len(data)):
    for b in range(a+1,len(data)):
      if verbose:
        print(f"Hailstone A: {hailstone(data[a])}")
        print(f"Hailstone B: {hailstone(data[b])}")
      m1,b1 = to_xy_formula(*data[a])
      m2,b2 = to_xy_formula(*data[b])
      x,y = intersect_slope_intercept(m1, b1, m2, b2)
      if x is None or y is None:
        if verbose:
          print(f"Hailstones' paths are parallel, they never intersect.\n")
        continue
      t_a = get_time(x,y,data[a][0],data[a][1])
      t_b = get_time(x,y,data[b][0],data[b][1])
      if t_a < 0 and t_b < 0:
        if verbose:
          print("Hailstones' paths crossed in the past for both hailstones.\n")
        continue
      if t_a < 0:
        if verbose:
          print("Hailstones' paths crossed in the past for hailstone A.\n")
        continue
      if t_b < 0:
        if verbose:
          print("Hailstones' paths crossed in the past for hailstone B.\n")
        continue

      if x >= bbox[0] and x <= bbox[1] and y >= bbox[0] and y <= bbox[1]:
        if verbose:
          print(f"Hailstones' paths will cross inside the test area (at {x},{y})\n")
        count += 1
      else:
        if verbose:
          print(f"Hailstones' paths will cross outside the test area (at {x},{y})\n")
  return count

def part1(data):
  #pprint.pprint(data)
  #count = find_intersections(data, (7,27))
  count = find_intersections(data, (200000000000000, 400000000000000))
  print(f"Count is {count}")



def part2(data):
  pass

def mymain(filename):
  data = parseit(aoc.lines(filename))

  print("Part 1")
  part1(data)

  print("Part 2")
  part2(data)

aoc.run(mymain)

