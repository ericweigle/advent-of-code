#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)

def recur(mask, address):
  #print("recur on %s %s" % ("".join(mask), "".join(address)))
  assert len(mask)==36
  assert len(address) == 36

  for i in range(len(mask)):
    if mask[i] == '0':
      continue
      #If the bitmask bit is 0, the corresponding memory address bit is unchanged.
    if mask[i] == '1':
      # If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
      address[i] = '1'
    if mask[i] == 'X':
      # If the bitmask bit is X, the corresponding memory address bit is floating.
      newmask = copy.copy(mask)
      #print("newmask: %s"% newmask)
      left = copy.copy(address)
      right = copy.copy(address)
      newmask[i] = '0'
      left[i] = '0'
      right[i] = '1'
      return recur(newmask, left) + recur(newmask, right)
  return [int("".join(address), 2)]
  

def get_addresses(raw_mask, raw_address):
  #print('raw mask: %s %s' % (raw_mask, raw_address))
  mask = list(raw_mask)
  address = list(format(int(raw_address), 'b'))
  #print('raw mask: %s %s' % (mask, address))
  if len(address) < 36:
    address = (['0']*(36-len(address))) + address
  #kprint("First %s %s" % (mask, address))
  return recur(mask, address)


def process_chunk(lines, memory):
  mask = lines[0].strip()
  for line in lines[1:]:
    m = re.match("^mem.([0-9]+). = ([0-9]+)$", line)
    raw_address = int(m.group(1))
    amount = int(m.group(2))
    all_addresses =get_addresses(mask, raw_address) 
    #print(all_addresses)
    for address in all_addresses:
      memory[address] = amount

def get_total(memory):
  return sum(memory.values())

for filename in sys.argv[1:]:
  data = open(filename, 'r').read().split("mask =")
  #print(data)
  memory = {0:0}
  for lines in data:
    if lines:
      process_chunk(lines.splitlines(), memory)
  #print(memory)
  print(get_total(memory))
