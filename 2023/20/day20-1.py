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

def all_inputs(dest, machine):
  for module in machine:
    x = machine[module]
    if type(x) is dict and dest in machine[module]['outputs']:
      yield module

def make_machine(data):
  machine = dict()
  for line in data:
    module, outputs = line.split(" -> ")
    outputs = [x.strip() for x in outputs.split(',')]
    if module.startswith("&"):
      state = {}
      mtype = '&'
      module = module[1:]
    elif module.startswith("%"):
      state = False
      mtype = '%'
      module = module[1:]
    else:
      assert module == "broadcaster"
      mtype = 'b'
      state = None
    machine[module] = {'type':mtype, 'state':state, 'outputs':outputs, 'cycle':None}
  machine['output'] = {'type':'o', 'state':{False:0,True:0}, 'outputs':[]}
  machine['rx'] = {'type':'o', 'state':{False:0,True:0}, 'outputs':[]}

  for module in machine:
    if machine[module]['type'] == '&':
      for inp in all_inputs(module, machine):
        machine[module]['state'][inp] = False
#  print("all inputs inv", list(all_inputs("inv", machine)))
#  print("all inputs con", list(all_inputs("con", machine)))
#

  machine[False] = 0
  machine[True] = 0

  return machine


def press_button(machine):
  def broadcast(signal):
    for output in machine[module]['outputs']:
      to_handle.append((signal, output, module))
      machine[signal]+=1

  machine[False] += 1  # button module send to broadcaster
  to_handle = [(False, "broadcaster", None)]
  while to_handle:
    #pprint.pprint(to_handle)
    signal, module, source = to_handle.pop(0)
    #prettyname = '-high' if signal else '-low'
    #print(f"Handling {source}: {prettyname} -> {module}")
    if machine[module]['type'] == 'b':
      #print("  Broadcaster")
      broadcast(signal)
    elif machine[module]['type'] == '%':
      #print("  flipper")
      if not signal:
        machine[module]['state'] = not machine[module]['state']
        broadcast(machine[module]['state'])
    elif machine[module]['type'] == '&':
      # TODO: questionable initialization of this dictionary
      #pprint.pprint(machine)
      machine[module]['state'][source] = signal
      #pprint.pprint(machine[module])
      if all(machine[module]['state'].values()):
        #print("  broadcasting False")
        broadcast(False)
      else:
        #print("  broadcasting True")
        broadcast(True)
    elif machine[module]['type'] == 'o':
      machine[module]['state'][signal] += 1
      #TODO machine[signal] += 1
    else:
      raise ValueError(f"Bad mtype: '{machine[module]['type']}'")

#  pprint.pprint(machine)

def part1(data):
  machine = make_machine(data)
  #pprint.pprint(machine )
  #for i in range(3):
  #  for press in range(4):
  #    press_button(machine)
  #  pprint.pprint(machine )
  for i in range(1000):
     press_button(machine)
  pprint.pprint(machine )
  print(f"Result: {machine[False]*machine[True]}")

def part2(data):
  machine = make_machine(data)
  for i in range(9999999999):
    press_button(machine)
    if i %10000==0:
      print(i)
    if machine['rx']['state'][False]>0:
      print(f"Result: {i}")
      break

def mymain(filename):
  data = aoc.lines(filename)

  # 16980 48053*p 815939940  #TOO HIGH
  # 16979 48054*p 815908866  #TOO HIGH
  print("Part 1")
  part1(data)

#  print("Part 2")
#  part2(data)

aoc.run(mymain)

