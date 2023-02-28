#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc

EXAMPLE_DIVISOR = 23*19*13*17
EXAMPLE = [
#Monkey 0:
  {
  "items": [ 79, 98],
  "operation": lambda old: old * 19,
  "test": lambda x: 2 if x % 23 == 0 else 3
  },{
#Monkey 1:
  "items": [ 54, 65, 75, 74],
  "operation": lambda old: old + 6,
  "test": lambda x: 2 if x % 19 == 0 else 0
  },{
#Monkey 2:
  "items": [ 79, 60, 97],
  "operation": lambda old: old*old,
  "test": lambda x: 1 if x % 13 == 0 else 3
  },{
#Monkey 3:
  "items": [ 74],
  "operation": lambda old: old + 3,
  "test": lambda x: 0 if x % 17 == 0 else 1
  },
]

PUZZLE_DIVISOR = 2*7*13*5*3*19*11*17
PUZZLE = [
  {
#Monkey 0:
  "items": [ 85, 79, 63, 72],
  "operation": lambda old: old * 17,
  "test": lambda x: 2 if x % 2 == 0 else 6
  },{
#Monkey 1:
  "items": [ 53, 94, 65, 81, 93, 73, 57, 92],
  "operation": lambda old: old * old,
  "test": lambda x: 0 if x % 7 == 0 else 2
  },{
#Monkey 2:
  "items": [ 62, 63],
  "operation": lambda old: old + 7,
  "test": lambda x: 7 if x % 13 == 0 else 6
  },{
#Monkey 3:
  "items": [ 57, 92, 56],
  "operation": lambda old: old + 4,
  "test": lambda x: 4 if x % 5 == 0 else 5
  },{
#Monkey 4:
  "items": [ 67],
  "operation": lambda old: old + 5,
  "test": lambda x: 1 if x % 3 == 0 else 5
  },{
#Monkey 5:
  "items": [ 85, 56, 66, 72, 57, 99],
  "operation": lambda old: old + 6,
  "test": lambda x: 1 if x % 19 == 0 else 0
  },{
#Monkey 6:
  "items": [ 86, 65, 98, 97, 69],
  "operation": lambda old: old * 13,
  "test": lambda x: 3 if x % 11 == 0 else 7
  },{
#Monkey 7:
  "items": [ 87, 68, 92, 66, 91, 50, 68],
  "operation": lambda old: old + 2,
  "test": lambda x: 4 if x % 17 == 0 else 3
  },
]

def dump_monkey_items(monkies):
  for i in range(len(monkies)):
    print(f"Monkey {i}: {monkies[i]['items']}")

def dump_monkey_inspections(monkies):
  for i in range(len(monkies)):
    print(f"Monkey {i} inspected items {monkies[i]['inspections']} times.")

def monkey_business(monkies):
  inspections = list(sorted([x['inspections'] for x in monkies]))
  return inspections[-1]*inspections[-2]

def run_round_pt1(monkies,divisor):
  for monkey in monkies:
    monkey["inspections"] = monkey.get("inspections", 0) + len(monkey['items'])
    for item in monkey['items']:
      item = monkey['operation'](item) // divisor
      next_monkey = monkey['test'](item)
      monkies[next_monkey]['items'].append(item)
      monkey['items'] = []

def run_round_pt2(monkies,divisor):
  for monkey in monkies:
    monkey["inspections"] = monkey.get("inspections", 0) + len(monkey['items'])
    for item in monkey['items']:
      item = monkey['operation'](item) % divisor
      next_monkey = monkey['test'](item)
      monkies[next_monkey]['items'].append(item)
      monkey['items'] = []


def part1(monkies, rounds,divisor):
  #print("Part 1")
  for myround in range(rounds):
    run_round_pt1(monkies,divisor)

  #dump_monkey_items(monkies)
  #dump_monkey_inspections(monkies)
  return monkey_business(monkies)

def part2(monkies, rounds, divisor):
  for myround in range(rounds):
    run_round_pt2(monkies,divisor)
    #if myround in (0,19,999,1999):
    #  print(f"After round {myround+1}")
    #  dump_monkey_inspections(monkies)

  #dump_monkey_items(monkies)
  return monkey_business(monkies)


def mymain(monkies, divisor):
  print(part1(copy.deepcopy(monkies),rounds=20,divisor=3))
  print(part2(monkies, rounds=10000, divisor=divisor))

#mymain(EXAMPLE,EXAMPLE_DIVISOR)
mymain(PUZZLE,PUZZLE_DIVISOR)
