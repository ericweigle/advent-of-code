#!/usr/bin/python3

import re
import sys
import copy
import numpy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)

def parse(filename):
  return [x.strip() for x in open(filename, 'r').readlines()]

openers = ['(', '{', '[', '<']
closers = [')', '}', ']', '>']
def pair_for(closer):
  return openers[closers.index(closer)]

def first_corrupt(line):
  mystack =[]
  for char in line:
    if char in openers:
      mystack.append(char)
    elif char in closers:
      if mystack[-1] == pair_for(char):
        mystack.pop(-1)
      else:
        return char,mystack
  return None,mystack

for filename in sys.argv[1:]:
  print(f"For file '{filename}'")
  data = parse(filename)

  pt1_score = 0
  pt2_scores = []
  for line in data:
    c, mystack = first_corrupt(line)
    if c:
      pt1_score += {')': 3, ']': 57, '}': 1197, '>': 25137}[c]
    else:
      foo = ''.join(reversed(mystack))
      foo = re.sub(r'\(', '1', foo)
      foo = re.sub(r'\[', '2', foo)
      foo = re.sub(r'{', '3', foo)
      foo = re.sub(r'<', '4', foo)
      pt2_scores.append(int(foo, 5))

  print('pt1',pt1_score)
  print('pt2',int(numpy.median(pt2_scores)))

