#!/usr/bin/python3

import pprint

#INPUT = "example.txt"
INPUT = "input.txt"

def score(c):
  if c == c.lower():
    return ord(c) - ord('a') + 1
  elif c == c.upper():
    return ord(c) - ord('A') + 27
  else:
    assert False


total = 0
for sack in [x.strip() for x in open(INPUT).readlines()]:
  l = len(sack)//2
  a = sack[0:l]
  b = sack[l:]
  assert len(a)==len(b)

  
  matching = list(set(a).intersection(set(b)))
  assert len(matching) == 1
  total += score(matching[0])
print(total)
