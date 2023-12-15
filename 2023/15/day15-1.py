#!/usr/bin/python3

import collections

import copy
import math
import parse
import pprint
import re
import sys
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc

def dohash(data):
  value = 0
  for c in data:
    value += ord(c)
    value = 17*value
    value = value % 256
  return value

def part1(data):
  assert dohash("HASH") == 52
  total = 0
  for s in data.split(','):
    total += dohash(s)
    #print(dohash(s))
  print(total)

def part2(data):
  hashmap = dict()
  for s in data.split(','):
    if s.endswith('-'):
      key = s[:-1]
      h = dohash(key)
      if h in hashmap and key in hashmap[h]:
        hashmap[h].pop(key)
    else:
      assert '=' in s
      key,value = s.split('=')
      value = int(value)
      h = dohash(key)
      if h not in hashmap:
        hashmap[h] = dict()
      hashmap[h][key] = value
  # print(hashmap)

  total = 0
  for box in range(256):
    values = hashmap.get(box,{})
    for slot, key in enumerate(values):
      total += (box+1)*(slot+1)*values[key]
  print(total)     

def mymain(filename):
  data = aoc.lines(filename)

  print("Part 1")
  part1(data[0])

  print("Part 2")
  part2(data[0])

aoc.run(mymain)

