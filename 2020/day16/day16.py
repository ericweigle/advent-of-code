#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)

def is_valid(number, rules):
  for v1, v2, v3, v4 in rules.values():
    if v1<=number<=v2 or v3<=number<=v4:
      return True
  return False


def invalid_sum(ticket, rules):
  total = 0
  for number in ticket:
    if not is_valid(number, rules):
      total += number
  return total


def parse_rules(rules):
  result = dict()
  for line in rules.splitlines():
    #print(line)
    m = re.match("^(.*): (\d*)-(\d*) or (\d*)-(\d*)$", line.strip())
    assert m
    result[m.group(1)] = (int(m.group(2)),
                          int(m.group(3)),
                          int(m.group(4)),
                          int(m.group(5)))
  #pprint.pprint(result)
  return result

def parseticket(raw_ticket):
  return [int(x) for x in raw_ticket.split(',')]


def can_be(ranges, index, tickets):
  v1, v2, v3, v4 = ranges
  for ticket in tickets:
    number = ticket[index]
    if not (v1<=number<=v2 or v3<=number<=v4):
      return False
  return True

def count_occur(key, possibilities):
  count = 0
  last = None
  for index in possibilities:
    if key in possibilities[index]:
      count+=1
      last = index
  return (count, last)

def dfs_by_key(possibilities, solution):
  keys = set(rules.keys())
  
  for key in keys:
    count, last_index = count_occur(key, possibilities)
    if count == 1:
      solution[last_index] = key
      possibilities.pop(last_index)
      dfs_by_key(possibilities, solution)


for filename in sys.argv[1:]:
  rules, my_ticket, nearby = open(filename, 'r').read().split("\n\n")
  my_ticket = parseticket(my_ticket.splitlines()[1])
  nearby = nearby.splitlines()[1:]
  nearby = [parseticket(x) for x in nearby]
  #print('rules:',rules)
  #print('ticket:',ticket)
  #print('nearby:',nearby)

  rules = parse_rules(rules)

  total = 0
  for ticket in nearby:
    total+= invalid_sum(ticket, rules)
  print("Part 1",total)

  assert invalid_sum(my_ticket, rules)==0
  valid_tickets = [my_ticket]
  for ticket in nearby:
    if invalid_sum(ticket, rules) == 0:
      valid_tickets.append(ticket)

  #print("Found %d valid tickets" % len(valid_tickets))
  possibilities = dict()
  for index in range(len(my_ticket)):
    possibilities[index] = []
    for key in rules:
      if can_be(rules[key], index, valid_tickets):
        #print("Index %d can be %s"%  (index, key))
        possibilities[index].append(key)
 
  solution = dict()
  dfs_by_key(possibilities, solution)
  #pprint.pprint(solution)

  departures = [x for x in solution if solution[x].startswith('departure')]
  #print(departures)
  
  total = 1
  for idx in departures:
    total *= my_ticket[idx]
  print("Part 2",total)
