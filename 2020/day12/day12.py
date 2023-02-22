#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

def part1():
  direction = 'E'
  # north, east
  north = 0
  east = 0 
  for action, amount in data:
    # print(action, amount)
    if action == 'F': # means to move forward by the given value in the direction facing
      action = direction

    if action == 'N': # means to move north by the given value.
      north += amount
    if action == 'S': # means to move south by the given value.
      north -= amount
    if action == 'E': # means to move east by the given value.
      east += amount
    if action == 'W': # means to move west by the given value.
      east -= amount
    if action == 'R': # means to turn right the given number of degrees.
      action = 'L'
      amount = 360-amount
    if action == 'L': # means to turn left the given number of degrees.
      while amount > 0:
        if direction == 'N':
          direction = 'W'
        elif direction == 'W':
          direction = 'S'
        elif direction == 'S':
          direction = 'E'
        elif direction == 'E':
          direction = 'N'
        amount -= 90
  print("part1",abs(north)+abs(east))
  
def part2():
  print('\n')
  waypoint_north = 1
  waypoint_east = 10

  # north, east
  ship_north = 0
  ship_east = 0 
  # print('start ship', ship_east,ship_north)
  # print('start wp', waypoint_east,waypoint_north)
  for action, amount in data:
    # print("executing", action, amount)
    if action == 'F':
      ship_north += waypoint_north * amount
      ship_east += waypoint_east * amount
    if action == 'N':
      waypoint_north += amount
    if action == 'S':
      waypoint_north -= amount
    if action == 'E':
      waypoint_east += amount
    if action == 'W':
      waypoint_east -= amount
    if action == 'L':
      action = 'R'
      amount = 360-amount
    if action == 'R':
      while amount > 0:
        tmp = waypoint_north
        waypoint_north = -1*waypoint_east
        waypoint_east = tmp
        amount -= 90
    #print('ship', ship_east,ship_north)
    #print('wp', waypoint_east,waypoint_north)
    #print("--")

  print("part2",abs(ship_north)+abs(ship_east))

for filename in sys.argv[1:]:
  data = [x.strip() for x in open(filename, 'r').readlines()]
  data = [(x[0], int(x[1:])) for x in data]
  #print(data)
 
  part1()
  part2()
