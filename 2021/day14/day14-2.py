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
  return polymer, rules

def expand(counted_tuples, rules):
  result = collections.defaultdict(int)
  for mypair in counted_tuples.keys():
    if mypair in rules:
      result[mypair[0] + rules[mypair]] += counted_tuples[mypair]
      result[rules[mypair]+ mypair[1]] += counted_tuples[mypair]
    else:
      result[mypair] += counted_tuples[mypair]
  return result

def elements(polymer,counted_tuples):
  counter = collections.defaultdict(int)
  for mypair in counted_tuples:
    counter[mypair[1]] += counted_tuples[mypair]
  counter[polymer[0]] += 1
  return counter

def parts(polymer, rules):
  counted_tuples = collections.defaultdict(int)
  for mypair in [polymer[i:i+2] for i in range(len(polymer)-1)]:
    counted_tuples[mypair] += 1
  for i in range(40):
    counted_tuples = expand(counted_tuples,rules)
    if i == 9:
      e = elements(polymer,counted_tuples)
      print("part 1", max(e.values()) - min(e.values()))

  e = elements(polymer,counted_tuples)
  print("part 2",max(e.values()) - min(e.values()))

def mymain(filename):
  data = aoc.lines(filename)
  polymer, rules = parse(data)
  parts(polymer, rules)

aoc.run(mymain)

