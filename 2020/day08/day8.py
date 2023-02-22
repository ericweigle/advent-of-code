#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

def terminates(program):
  accumulator = 0
  counter = 0
  while True:
    if counter >= len(program):
      return (True, accumulator)
    if program[counter]['visited']:
      return (False, accumulator)
    program[counter]['visited'] = True

    print("Executing " + str(program[counter]))
    if program[counter]['op'] == 'acc':
      accumulator += program[counter]['val']
      counter += 1
    elif program[counter]['op'] == 'jmp':
      counter += program[counter]['val']
    elif program[counter]['op'] == 'nop':
      counter += 1
    

for filename in sys.argv[1:]:
  data = [x.strip() for x in open(filename, 'r').readlines()]
  data = [x.split(" ") for x in data] # operation, param
  data = [{'op':x[0], 'val':int(x[1]), 'visited':False} for x in data]

  for operation in range(len(data)):
    print("Testing %d" % operation)
    copied = copy.deepcopy(data)
    if copied[operation]['op'] == 'jmp':
      print("  jmp -> nop")
      copied[operation]['op'] = 'nop'
      does, accumulator = terminates(copied)
      if does:
        print("Accumulator: ",accumulator)
        sys.exit(0)
    elif copied[operation]['op'] == 'nop':
      print("  nop -> jmp")
      copied[operation]['op'] = 'jmp'
      does, accumulator = terminates(copied)
      if does:
        print("Accumulator: ",accumulator)
        sys.exit(0)
    else: # acc
      print("  acc -> nothing to do")
      pass
  print("Failed to find solution")
