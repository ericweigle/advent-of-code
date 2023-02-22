#!/usr/bin/python3

import os
import re
import sys
import math
import pprint
import copy

def check_timestamp(buses, t):
  for bus, offset in buses:
    #print("Bus: %03d\toffset:%d\ttime: %d\trel_time: %d\tmodulo: %d" % (bus, offset, t, t+offset, (t+offset)% bus))
    if ((t+offset)% bus) != 0:
      return False
  return True

def parse(buses):
  parsed = []
  buses = buses.split(",")
  count = 0
  for count in range(len(buses)):
    bus = buses[count]
    if bus != 'x':
      parsed.append((int(bus), count))
  parsed = list(reversed(sorted(parsed)))
  print(parsed)
  return parsed

#  buses = parse(data[1])
# part 1
#   start_time=int(data[0])
#   buses = data[1].split(",")
#   buses = [int(x) for x in buses if x!='x']
#   print(buses)
#   print(sorted([(x-(start_time % x), x) for x in buses]))

#
#base = 70147
#counter = 7*13*59*31
#parsed = parse("7,13") # 77
#parsed = parse("7,13,x,x,59") # 350
#parsed = parse("7,13,x,x,59,x,31") # 70147
#parsed = parse("7,13,x,x,59,x,31,19") # 2755467792 
#for i in range(base,100000000000000,counter):
#  if check_timestamp(parsed,i):
#    print(i)
#    break

def multiply_out(parsed):
  total = 1
  for bus, offset in parsed:
    total *= bus
  return total

def solve(buses):
  base = 0
  counter = 1
  step = 0
  while step < len(buses):
    print("Working on step %d: %s --> base %d counter %d" % (step, buses[:(step+1)], base, counter))
    for i in range(base,100000000000000000,counter):
      if check_timestamp(buses[:(step+1)],i):
        solution = i
        print("Solution for step %d: %d" % (step, solution))
        break
    base = solution
    counter = multiply_out(buses[:(step+1)])
    step+=1
  return solution


#print([17*x for x in range(20)])
#print([13*x-2 for x in range(20)])
#print(check_timestamp(parse("7,13"), 77))
#print(check_timestamp(parse("7,x,13"), 102))

#for i in range(1000):
#  if (i%17==0 and (i+2)%13==0):
#    print(i)
#    os.system('factor %s'% i)
#
#  print(check_timestamp(parse("7,13,x,x,59,x,31,19"), 1068781))
#  print(check_timestamp(parse("17,x,13,19"), 3417))
#  print(check_timestamp(parse("67,7,59,61"), 754018))
#  print(check_timestamp(parse("67,x,7,59,61"), 779210))
#  print(check_timestamp(parse("67,7,x,59,61"), 1261476))
#  print(check_timestamp(parse("1789,37,47,1889"), 1202161486))
#  print(check_timestamp(parse(data[1]), 487905974205117))

assert solve(parse("7,13,x,x,59,x,31,19")) ==1068781
assert solve(parse("17,x,13,19"))      ==   3417
assert solve(parse("67,7,59,61"))      ==   754018
assert solve(parse("67,x,7,59,61"))    ==  779210
assert solve(parse("67,7,x,59,61"))    ==  1261476
assert solve(parse("1789,37,47,1889")) ==  1202161486
assert solve(parse("13,x,x,41,x,x,x,x,x,x,x,x,x,569,x,29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,x,x,937,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17"))
