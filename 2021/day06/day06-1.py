#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)

def ints(filename):
  lines = [x.strip() for x in open(filename, 'r').readlines()]
  result = []
  for line in lines:
    value = re.sub('[^0-9]', ' ', line)
    result.append(value.split())
  return result

def advance_one_day(fish):
  #print("advancing",fish)
  result = dict()
  #$for counter in range(10):
  #$  result[counter] = 0

  for counter in fish:
    if not fish[counter]:
      continue
    #print("foo",counter)
    if counter == 0:
      result[6] = result.get(6,0) + fish[counter]
      result[8] = fish[counter]
    else:
      result[counter-1] = result.get(counter-1,0) +fish[counter]
  return result

 
def tostring(fish):
  result = []
  for key in sorted(fish):
    result.append(f'{key},{fish[key]}')
  return ' '.join(result)

def part1(data):
  fish = dict()
  for counter in data:
    fish[counter] = fish.get(counter,0)+1
 
  print("before",fish)
  for day in range(256):
    fish = advance_one_day(fish)
    print("day",day,"fish",tostring(fish))
  print(sum(fish.values()))


def part2(data):
  pass

for filename in sys.argv[1:]:
  print(f"For file '{filename}'")
  data = ints(filename)
  data = [int(x) for x in data[0]]
  part1(copy.deepcopy(data))
  part2(data)
