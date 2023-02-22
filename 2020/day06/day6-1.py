#!/usr/bin/python3

import re
import sys
import math

def yield_groups(data):
  result = []
  for line in data:
    if line:
      result.append(line)
    else:
      if result:
        yield result
      result = []
  if result:
    yield result

def setify(group):
 # print("group"+str(group))
  allof = set()
  first = True
  for line in group:
    if first:
      print("First: " + line)
      allof = set(line)
      first = False
    else:
      print("line" + line +  "set " + str(set(line)))
      allof =allof.intersection(set(line))
  print("final: " +str(allof))
  return len(allof)

for filename in sys.argv[1:]:
  print("For %s" % filename)
  #data = [x.strip() for x in open(filename, 'r').readlines()]
  #print(sum(setify(group) for group in yield_groups(data)))

  data = [x.splitlines() for x in (open(filename, 'r').read() + "\n").split("\n\n")]
  print 
  #print(data)
  print(sum(setify(group) for group in data))

