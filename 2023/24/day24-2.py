#!/usr/bin/python3

import collections

import copy
import code
import math
import pprint
import re
import sys
import itertools
import z3
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc

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

def part2(data):
  # We're going to construct equations of the form:
  #   our rock  = the hailstone
  #   x + dx*t1 = C1 + C4*t1
  #   y + dy*t1 = C2 + C5*t1
  #   z + dz*t1 = C3 + C6*t1
  # or equivalently
  #    x = C1 - (dx-C4)*t1 
  #    y = C2 - (dy-C5)*t1 
  #    z = C3 - (dz-C6)*t1 
  # So the first data point produces a set of 7 unknowns and 3 equations;
  # the next 8 unknowns (new time) and 6 equations, and the third data point
  # 9 unknowns (new time) and 9 equations. So we can solve with only 3 input
  # records.
  x = z3.Int('x')
  y = z3.Int('y')
  z = z3.Int('z')
  dx = z3.Int('d')
  dy = z3.Int('e')
  dz = z3.Int('f')
  t1 = z3.Real('t1')
  t2 = z3.Real('t2')
  t3 = z3.Real('t3')

  s = z3.Solver()
  s.add(t1 >= 0)
  s.add(t2 >= 0)
  s.add(t3 >= 0)
  s.add(z >= 0)
  s.add(x + dx*t1 == data[0][0][0] + data[0][1][0]*t1)
  s.add(y + dy*t1 == data[0][0][1] + data[0][1][1]*t1)
  s.add(z + dz*t1 == data[0][0][2] + data[0][1][2]*t1)
  s.add(x + dx*t2 == data[1][0][0] + data[1][1][0]*t2)
  s.add(y + dy*t2 == data[1][0][1] + data[1][1][1]*t2)
  s.add(z + dz*t2 == data[1][0][2] + data[1][1][2]*t2)
  s.add(x + dx*t3 == data[2][0][0] + data[2][1][0]*t3)
  s.add(y + dy*t3 == data[2][0][1] + data[2][1][1]*t3)
  s.add(z + dz*t3 == data[2][0][2] + data[2][1][2]*t3)

  print("Solving")
  print(s.check())
  if str(s.check())=='sat':
    print(s.model())
    m = s.model()
    result = int(str(m[x])) + int(str(m[y])) + int(str(m[z]))
    print("Result: ", result)
  else:
    print(f"Unsatisfiable :( {s.check()}")

def mymain(filename):
  data = parseit(aoc.lines(filename))

  print("Part 2")
  part2(data)

aoc.run(mymain)
