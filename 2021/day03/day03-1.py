#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)


# part 1
for filename in sys.argv[1:]:
  data = [x.strip() for x in open(filename, 'r').readlines()]

  gamma = 0
  epsilon = 0
  for bit in range(0,len(data[0])):
    total = 0
    for line in data:
      total += int(line[bit])
    if total > (len(data)/2):
      gamma = gamma *2+1
      epsilon = epsilon * 2+0
    else:
      gamma = gamma *2+0
      epsilon = epsilon * 2+1
print(gamma*epsilon)

# part 2
def collect(data, bit):
  total = 0
  for line in data:
    total += int(line[bit])
  if total >= (len(data)/2):
    return 1
  return 0

def select(data, bit, value):
  return [x for x in data if int(x[bit]) == value]

for filename in sys.argv[1:]:
  data = [x.strip() for x in open(filename, 'r').readlines()]
  # ox scrubber
  for bit in range(len(data[0])):
    v = collect(data, bit)
    data = select(data, bit, v)
    if len(data) == 1:
      ox = int(data[0],2)
  # co2 scrubber
  data = [x.strip() for x in open(filename, 'r').readlines()]
  for bit in range(len(data[0])):
    v = collect(data, bit)
    data = select(data, bit, 0 if v else 1)
    if len(data) == 1:
      co = int(data[0],2)
  print(ox * co)
