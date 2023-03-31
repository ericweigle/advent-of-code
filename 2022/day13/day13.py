#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc

def parse_packet(packet:str):
  return eval(packet)

def parse_input(filename):
  data = open(filename, "r").read()
  pairs = data.split("\n\n")
  return [[parse_packet(y) for y in x.splitlines()] for x in pairs]

def compare(left, right, indent=""):
  if type(left) is int and type(right) is int:
    #print(f"{indent}- [int]Compare {left} vs {right}")
    if left < right:
      return -1 # less
    if right < left:
      return 1  # more
    return 0  # equal

  if type(left) is list and type(right) is list:
    #print(f"{indent}- [list]Compare {left} vs {right}")
    for i in range(max(len(left), len(right))):
      if i < len(left) and i < len(right):
        c = compare(left[i], right[i],indent+"  ")
        if c != 0:
          return c
      elif i < len(right):
        #print(f"{indent}Left side ran out of items, so inputs are in the right order")
        return -1
      elif i < len(left):
        #print(f"{indent}Right side ran out of items, so inputs are in the wrong order")
        return 1
    return 0

  if type(left) is int and type(right) is list:
    return compare([left],right,indent+"  ")
  if type(left) is list and type(right) is int:
    return compare(left,[right],indent+"  ")

  raise ValueError("Should be impossible:",left,right,type(left),type(right))


def part1(filename):
  data = parse_input(filename)
  corrects = 0
  for i in range(len(data)):
    #print(f"-- Pair {i+1} ==")
    left, right = data[i]
    result = compare(left,right)
    if result < 0:
      corrects += (i+1)
    #print(f"Pair {i+1}: {result}")
  print(corrects)

def get_index(data, query):
  for i in range(len(data)):
    if data[i] == query:
      return i+1

def part2(filename):
  data = parse_input(filename)
  unpaired = []
  for left, right in data:
    unpaired.append(left)
    unpaired.append(right)
  unpaired.append([[2]])
  unpaired.append([[6]])
  data = unpaired

  for i in range(len(data)):
    for j in range(i+1,len(data)):
      if compare(data[i],data[j]) > 0:
        tmp = data[i]
        data[i] = data[j]
        data[j] = tmp
  #pprint.pprint(data)
  print(get_index(data, [[2]])*get_index(data,[[6]]))

def mymain(filename):
  print("Part 1")
  part1(filename)
  print("Part 2")
  part2(filename)

aoc.run(mymain)
