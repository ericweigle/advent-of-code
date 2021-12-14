#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc

def parse(data):
  polymer = data.pop(0)
  data.pop(0)
  rules = [tuple(x.split(' -> ')) for x in data]
  pairs = [x[0] for x in rules]
  assert len(pairs) == len(set(pairs))
  rules = dict(rules)
  #print(polymer)
  #print(rules)
  return polymer, rules

def expand(polymer, rules):
  two_tuples = [polymer[i:i+2] for i in range(len(polymer)-1)]
  result = []
  for mypair in two_tuples:
    if mypair in rules:
      result.append(mypair[0] + rules[mypair] + mypair[1])
    else:
      result.append(mypair)
  return result[0][0] + ''.join(x[1:] for x in result)


def elements(polymer):
  counter = collections.defaultdict(int)
  for c in polymer:
    counter[c] += 1
  return counter

def part1(polymer, rules):
  #print(polymer)
  for i in range(10):
    polymer = expand(polymer,rules)
    #pprint.pprint(elements(polymer))
  e = elements(polymer)
  print(max(e.values()) - min(e.values()))

def mymain(filename):
  data = aoc.lines(filename)
  polymer, rules = parse(data)

  print("Part 1")
  part1(polymer, rules)

aoc.run(mymain)

