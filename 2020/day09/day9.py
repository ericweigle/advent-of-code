#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

def isOk(target, search):
  #print("Searching" + str(search) + " for " + str(target))
  for i in search:
    for j in search:
      if i==j:
        continue
      if (i+j)==target:
        return True

  return False

def get_target(preamble, data):
  for i in range(preamble,len(data)):
    if not isOk(data[i], data[i-preamble:i]):
      print("Target",data[i])
      return data[i]
  print("Target not found")
  sys.exit(1)


def get_target2(target, data):
  for start in range(len(data)-1):
    for end in range(start+1,len(data)):
      sliced = data[start:end] 
      if sum(sliced) == target:
        print("Target 2 found",min(sliced)+max(sliced))
        return 
  print("Target 2 not found")
  sys.exit(1)

for filename in sys.argv[1:]:
  data = [int(x.strip()) for x in open(filename, 'r').readlines()]
  preamble = 5 if len(data)==20 else 25

  target = get_target(preamble, data)
  get_target2(target, data)
