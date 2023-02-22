#!/usr/bin/python3


import re
import sys
import math
import pprint
import copy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)

def parse_mask(mask):
  assert len(mask)==36
  one_mask = 0
  zero_mask = 0
  for i in range(len(mask)):
    one_mask = one_mask << 1
    zero_mask = zero_mask << 1
    if mask[i] == '1':
      one_mask = one_mask | 1
    if mask[i] != '0':
      zero_mask = zero_mask | 1

  #print(one_mask, zero_mask)
  return one_mask, zero_mask

def process_chunk(lines, memory):
  mask = lines[0].strip()
  one_mask, zero_mask = parse_mask(mask)
  for line in lines[1:]:
    m = re.match("^mem.([0-9]+). = ([0-9]+)$", line)
    address = int(m.group(1))
    amount = int(m.group(2))
    memory[address] = (amount | one_mask) & zero_mask
    #print(memory)

def get_total(memory):
  return sum(memory.values())

for filename in sys.argv[1:]:
  data = open(filename, 'r').read().split("mask =")
  print(data)
  memory = {0:0}
  for lines in data:
    if lines:
      process_chunk(lines.splitlines(), memory)
  print(memory)
  print(get_total(memory))
