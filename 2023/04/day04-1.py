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


def run(data):
  multiplier = collections.defaultdict(lambda:1)
  pt1_total = 0
  pt2_total = 0
  for line in data:
    card, winners, mine = parse.parse("Card {}: {} | {}", line)
    card = int(card)
    winners = [int(x) for x in winners.strip().split(" ") if x]
    mine = [int(x) for x in mine.strip().split(" ") if x]
    matches = set(winners).intersection(mine)
    # part 1 scoring
    if matches:
      value = 2**(len(matches)-1)
    else:
      value = 0
    pt1_total += value

    # part 2 scoring
    pt2_total += multiplier[card]
    if matches:
      for i in range(card+1, card+len(matches)+1):
        multiplier[i] += multiplier[card]

    #print(card, winners, mine, matches, value)
  print(f"Part 1: {pt1_total}")
  print(f"Part 2: {pt2_total}")


def mymain(filename):
  data = aoc.lines(filename)

  run(data)

aoc.run(mymain)

