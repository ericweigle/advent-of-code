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
    machine[module] = {'type':mtype, 'state':state, 'outputs':outputs}
  machine['output'] = {'type':'o', 'state':{False:0,True:0}, 'outputs':[]}
  machine['rx'] = {'type':'o', 'state':{False:0,True:0}, 'outputs':[]}

  for module in machine:
    if machine[module]['type'] == '&':
      for inp in all_inputs(module, machine):
        machine[module]['state'][inp] = False
#  print("all inputs inv", list(all_inputs("inv", machine)))
#  print("all inputs con", list(all_inputs("con", machine)))

  return machine


def press_button(machine):
  def broadcast(signal):
    for output in machine[module]['outputs']:
      to_handle.append((signal, output, module))
      #machine[signal]+=1

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


def strip_submachine(machine):
  for module in machine:
    machine[module]['outputs'] = [x for x in machine[module]['outputs'] if x in machine]
  return machine

def build_submachine(machine, target, output):
  if target not in output:
    assert not output
    output[target] = {'type':'o', 'state':{False:0,True:0}, 'outputs':[]}

  for module in machine:
    if (target in machine[module]['outputs'] and
        module not in output):
      #print(f"Found {module} which points at {target}")
      output[module] = copy.deepcopy(machine[module])
      build_submachine(machine, module, output)
  return output

def submachine(machine, target):
  result = dict()
  build_submachine(machine, target, result)
  return strip_submachine(result)

def find_flip_interval(module, machine):
  baby = submachine(machine, module)
  #pprint.pprint(baby)
  last_false_count = 0
  last_flip = 0
  hist = {}
  for i in range(100000):
    press_button(baby)
    if baby[module]['state'][False] > last_false_count:
      period = i-last_flip
      #print(f"{i} Flip {period}")
      hist[period] = hist.get(period,0)+1
      last_false_count = baby[module]['state'][False]
      last_flip = i
  print(module,hist)
  assert len(hist) == 2
  for key in hist:
    if hist[key] > 2:
      return key
  

def part2(data):
  machine = make_machine(data)
  #pprint.pprint(machine)
  
  # This is specific to my machine; see dot graph
  # `dot -Tpdf input.dot > structure.pdf`
  total = 1
  total *= find_flip_interval('mf', machine)
  total *= find_flip_interval('fh', machine)
  total *= find_flip_interval('fz', machine)
  total *= find_flip_interval('ss', machine)
  print(total)

#  for i in range(1,100000000):
#    press_button(machine)

def mymain(filename):
  data = aoc.lines(filename)

  print("Part 2")
  part2(data)

aoc.run(mymain)

