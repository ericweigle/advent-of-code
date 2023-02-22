#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

solved = dict()
def expand(index, rules):
  if index in solved:
    return solved[index]

  #if len(rules[index])==1:
  #  if rules[index][0] == '"a"':
  #    solved[index] = 'a'
  #    return solved[index]
  #  elif rules[index][0] == '"b"':
  #    solved[index] = 'b'
  #    return solved[index]

  expanded = ['(']
  for token in rules[index]:
    if re.match("^\d+$", token):
      expanded.append(expand(int(token), rules))
    elif token == '"a"':
      expanded.append('a')
    elif token == '"b"':
      expanded.append('b')
    elif token == '|':
      expanded.append(')|(')
    else:
      print("Failed to match token '%s'"% token)
      assert False
  expanded.append(')')
  #print(expanded)
  solved[index] = '(%s)' % ''.join(expanded)
  #print(solved[index])
  return solved[index]

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)


def count():
  #pprint.pprint(solved)
  effective_regex = '^%s$' % solved[0]
  #print(effective_regex)
  count = 0
  for message in messages:
    if re.match(effective_regex, message):
      count+=1
  return count

for filename in sys.argv[1:]:
  rules, messages = open(filename, 'r').read().split('\n\n')
  rules = [x.strip() for x in rules.splitlines()]
  rules.sort(key=lambda x: int(x.split(':')[0].strip()))
  for i in range(len(rules)):
    rules[i] = [x.strip() for x in rules[i].split(':')[1].strip().split()]
  #print(rules)

  messages = [x.strip() for x in messages.splitlines()]

  # tokenize
  #pprint.pprint(rules)

  # part 1
  expand(0, copy.deepcopy(rules) )
  print(count())

  # part 2
  solved = dict()
  expand(31, rules)
  expand(42, rules)

  # 8: 42 | 42 8
  solved[8] = '((%s)+)' % solved[42]
  # 11: 42 31 | 42 11 31
  solved[11] = '((%s%s)|(%s%s%s%s)|(%s%s%s%s%s%s)|(%s%s%s%s%s%s%s%s)|(%s%s%s%s%s%s%s%s%s%s))' % (solved[42], solved[31],
  solved[42],solved[42], solved[31], solved[31],
  solved[42],solved[42],solved[42], solved[31], solved[31], solved[31],
  solved[42],solved[42],solved[42],solved[42], solved[31], solved[31], solved[31], solved[31],
  solved[42],solved[42],solved[42],solved[42],solved[42], solved[31], solved[31], solved[31], solved[31], solved[31])

  expand(0, rules)
  print(count())
