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

def parse_rule(rule):
  m = re.match('^([xmas])([<>])([0-9]+):([a-zA-Z]+)$', rule)
  if m:
    return (m.group(1), m.group(2), int(m.group(3)), m.group(4))
  elif re.match('^[a-zA-Z]+$', rule):
    return (None, None, None, rule)
  raise ValueError(f"Could not parse rule {rule}")

def part2(rules, workflow, xmas_range, accepted_ranges):
  if workflow == 'A':
    accepted_ranges.append(xmas_range)
    return
  if workflow == 'R':
    return

  for xmas, lt_gt, num, next_workflow in rules[workflow]:
    if xmas is None:
      part2(rules, next_workflow, xmas_range, accepted_ranges)
      return

    if lt_gt == '<':
      copied_range = copy.deepcopy(xmas_range)
      copied_range[xmas][1] = min(copied_range[xmas][1], num-1)
      if copied_range[xmas][1] >= copied_range[xmas][0]:
        part2(rules, next_workflow, copied_range, accepted_ranges)

      xmas_range[xmas][0] = max(xmas_range[xmas][0], num)
      if xmas_range[xmas][1] < xmas_range[xmas][0]:
        return

    else: # lt_gt == '>'
      copied_range = copy.deepcopy(xmas_range)
      copied_range[xmas][0] = max(copied_range[xmas][0], num+1)
      if copied_range[xmas][1] >= copied_range[xmas][0]:
        part2(rules, next_workflow, copied_range, accepted_ranges)

      xmas_range[xmas][1] = min(xmas_range[xmas][1], num)
      if xmas_range[xmas][1] < xmas_range[xmas][0]:
        return


def doparse(filename):
  data = open(filename, 'r').read()
  rules, parts = data.split("\n\n")
  rules = [x.strip() for x in rules.splitlines()]
  workflows = dict()
  for rule in rules:
    #print(f"Parsing rule {rule}")
    name, pieces = rule.split('{')
    pieces = pieces.strip('}')
    pieces = pieces.split(',')
    workflows[name] = [parse_rule(x) for x in pieces]
  rules = workflows

  raw_parts = [x.strip() for x in parts.splitlines()]
  parts = []
  for part in raw_parts:
    part = part.strip('{')
    part = part.strip('}')
    x, m, a, s = parse.parse("x={},m={},a={},s={}", part)
    parts.append({'x':int(x),'m':int(m),'a':int(a),'s':int(s)})
  #pprint.pprint(rules)
  #pprint.pprint(parts)
  return rules, parts

def combinations(xmas):
  total = 1
  for c in ('x', 'm', 'a', 's'):
    lo, hi = xmas[c]
    total *= (hi-lo)+1
  return total

def mymain(filename):
  rules, parts = doparse(filename)

  print("Part 2")
  xmas={'x':[1,4000], 'm':[1,4000], 'a':[1,4000], 's':[1,4000]}
  accepted = []
  part2(rules, workflow='in', xmas_range=xmas, accepted_ranges=accepted)
  total = 0
  for xmas in accepted:
    print(xmas)
    total += combinations(xmas)
  print(f"Total: {total}")

aoc.run(mymain)

