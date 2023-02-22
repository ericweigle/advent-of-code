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


sacks = [x.strip() for x in open(INPUT).readlines()]
assert(len(sacks)%3==0)

total = 0
for group in range(0,1000,3):
  if group < len(sacks):
    a,b,c = sacks[group:(group+3)]
    matching = list(set(a).intersection(set(b)).intersection(set(c)))
    assert len(matching) == 1
    print(matching,score(matching[0]))
    total += score(matching[0])
print(total)

#total = 0
#for sack in scaks:
#  l = len(sack)//2
#  a = sack[0:l]
#  b = sack[l:]
#  assert len(a)==len(b)
#
#  
#  matching = list(set(a).intersection(set(b)))
#  total += score(matching[0])
#print(total)
