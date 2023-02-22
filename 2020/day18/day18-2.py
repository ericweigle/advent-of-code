#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)

def tokenize(line):
  line = line.replace("(", " ( ")
  line = line.replace(")", " ) ")
  line = line.replace("  ", " ")
  line = line.replace("  ", " ")
  tokens = line.strip().split(" ")
  #print(tokens)
  return tokens

def is_op(token):
  return token in ('+', '*')

def is_num(token):
  return re.match("^\d+$", token)


def extract_subexpression(tokens):
  count = 0
  start = tokens.index('(')
  for index in range(start, len(tokens)):
    if tokens[index] == '(':
      count += 1
    elif tokens[index] == ')':
      count -= 1
      if count == 0:
        end = index
        #print("Matching pair: %s" % tokens[start:end+1])
        value = evaluate(tokens[start+1:end])
        new_list = tokens[:start] + [str(value)] + tokens[end+1:]
        #print("old list: %s" % tokens)
        #print("new list: %s" % new_list)
        return new_list


def evaluate(tokens):
  while '(' in tokens:
    tokens = extract_subexpression(tokens)

  if '+' in tokens and len(tokens)>3:
    index = tokens.index('+')
    new_tokens = tokens[:index-1] + ['(', tokens[index-1], '+', tokens[index+1], ')'] + tokens[index+2:]
    #print("old list: %s" % tokens)
    #print("new list: %s" % new_tokens)
    return evaluate(new_tokens)

  value = None
  operator = None
  for i in range(len(tokens)):
    token = tokens[i]
    if is_num(token):
      token = int(token)
      if value is None:
        value = token
      else:
        assert operator is not None
        if operator == '*':
          value = value * token
        elif operator == '+':
          value = value + token
        else:
          assert False
    elif is_op(token):
      operator = token
    else:
      assert False
  #print(value)
  return value

assert evaluate(tokenize("1 + 2 * 3 + 4 * 5 + 6")) == 231
assert evaluate(tokenize("1 + (2 * 3) + (4 * (5 + 6))")) == 51
assert evaluate(tokenize("2 * 3 + (4 * 5)")) == 46
assert evaluate(tokenize("5 + (8 * 3 + 9 + 3 * 4 * 3)")) == 1445
assert evaluate(tokenize("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")) == 669060
assert evaluate(tokenize("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")) == 23340

for filename in sys.argv[1:]:
  data = [x.strip() for x in open(filename, 'r').readlines()]
  overall_total = 0
  for line in data:
    overall_total += evaluate(tokenize(line))
  print("Overall total: %s" % overall_total)
