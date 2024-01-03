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

def read_wires(data):
  mymap = dict()
  def doadd(a, b):
    if a in mymap:
      mymap[a].append(b)
    else:
      mymap[a] = [b]

  for line in data:
    component, others = line.split(":")
    component = component.strip() 
    others = others.strip()
    others = [x.strip() for x in others.split(" ")]
    for c in others:
      doadd(component, c)
      doadd(c, component)
      # neato -Tpdf output.dot > output.pdf; evince output.pdf
      # ljm -- sfd
      # gst -- rph
      # jkn -- cfn
      # print(f"{component} -- {c}")
  return mymap

def groupsize(m, start):
  visited = set()
  to_visit = set([start])
  while to_visit:
    a = to_visit.pop()
    if a in visited:
      continue
    visited.add(a)
    for b in m[a]:
      to_visit.add(b)
  return len(visited)
  
def part1(data):
  mymap = read_wires(data)
  mymap['ljm'].remove('sfd')
  mymap['sfd'].remove('ljm')
  mymap['gst'].remove('rph')
  mymap['rph'].remove('gst')
  mymap['jkn'].remove('cfn')
  mymap['cfn'].remove('jkn')
  group1 = groupsize(mymap, 'ljm')
  group2 = groupsize(mymap, 'sfd')
  print(group1*group2)

def part2(data):
  pass

def mymain(filename):
  data = aoc.lines(filename)

  print("Part 1")
  part1(data)

  print("Part 2")
  part2(data)

aoc.run(mymain)

