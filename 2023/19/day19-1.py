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

def rating(part):
  return sum(part.values())


def parse_rule(rule):
  m = re.match('^([xmas])([<>])([0-9]+):([a-zA-Z]+)$', rule)
  if m:
    return (m.group(1), m.group(2), int(m.group(3)), m.group(4))
  elif re.match('^[a-zA-Z]+$', rule):
    return (None, None, None, rule)
  raise ValueError(f"Could not parse rule {rule}")


def organize(part, rules):
  workflow = "in"
  while workflow not in ('A', 'R'):
    for xmas, lt_gt, num, next_workflow in rules[workflow]:
      if xmas is None:
        workflow = next_workflow
        break
      elif lt_gt == '<':
        if part[xmas] < num:
          workflow = next_workflow
          break
      else:
        if part[xmas] > num:
          workflow = next_workflow
          break
  return workflow

def doparse(filename):
  data = open(filename, 'r').read()
  rules, parts = data.split("\n\n")
  rules = [x.strip() for x in rules.splitlines()]
  workflows = dict()
  for rule in rules:
    print(f"Parsing rule {rule}")
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
  pprint.pprint(rules)
  pprint.pprint(parts)
  return rules, parts

def part1(rules, parts):
  total = 0
  for part in parts:
    result = organize(part, rules)
    print(f"Terminal result: {result}")
    if result == 'A':
      total += rating(part)
  print(f"Total {total}")

def part2(rules, parts):
  pass

def mymain(filename):
  rules, parts = doparse(filename)

  print("Part 1")
  part1(rules, parts)

  print("Part 2")
  part2(rules, parts)

aoc.run(mymain)

