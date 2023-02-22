#!/usr/bin/python3

import pprint

#INPUT = "example.txt"
INPUT = "input.txt"

data = [x.strip() for x in open(INPUT).readlines()]
print(data)

def contains(a, b):
  return a[0]>=b[0] and a[1]<=b[1]

def overlaps(a,b):
  return ((a[0]>=b[0] and a[0]<=b[1]) or 
          (a[1]>=b[0] and a[1]<=b[1]))

def score(a,b):
  if overlaps(a,b) or overlaps(b,a):
    return 1
  return 0

total = 0
for line in data:
  a, b = line.split(",")
  a = [int(x) for x in a.split('-')]
  b = [int(x) for x in b.split('-')]
  print(a,b,contains(a,b),contains(b,a))
  total += score(a,b)
print(total)
  
