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


def doparse(data):
  for line in data:
    dots, numbers = line.split()
    #dots = [x for x in dots.split(".") if x]
    dots = [x for x in dots]
    numbers = [int(x) for x in numbers.split(',')]
    yield (dots, numbers)


def unfold(data):
  for d, n in data:
    yield (d+['?']+d+['?']+d+['?']+d+['?']+d, 
           n+n+n+n+n) 

def first_consistent(dots, numbers):
  if len(dots) > 0 and dots[0]=='?':
    return "?"
  count = 0
  for i in range(len(dots)):
    if dots[i]== '.':
      if count > 0:
        if not numbers:
          #print(f"No: case 1 -- {count} {i} {numbers}")
          return 'N'
        if count == numbers[0]:
          return 'Y'
        else:
          #print(f"No: case 2 -- {count} {i} {numbers}")
          return 'N'
    elif dots[i]== '#':
      count += 1
    elif dots[i] == '?':
      if count > 0 and numbers and count>numbers[0]:
        #print(f"No: case 3 -- {count} {i} {numbers}")
        return 'N'
      return "?"
  if count > 0:
    if len(numbers) == 1 and count == numbers[0]:
      return 'Y'
    else:
      #print(f"No: case 4 -- {count} {i} {numbers}")
      return 'N'
  if numbers:
    return 'N'
  else:
    return 'Y'


def strip_first(dots, nums):
  if not dots and not nums:
    return [], []
  if dots[0] == '.':
    return strip_first(dots[1:], nums)
  elif dots[0] == '#':
    return (dots[nums[0]+1:], nums[1:])
  else:
    raise ValueError(f"Can't simplify {dots} {nums}")


def consistent(dots, numbers):
  count = 0
  counts = []
  for i in range(len(dots)):
    if dots[i]== '.':
      if count > 0:
        counts.append(count)
      count = 0
    elif dots[i]== '#':
      count += 1
    else:
      raise ValueError("Undefined symbol")
  if count > 0:
    counts.append(count)
  if counts != numbers:
    #print(f"Inconsistent {dots} {counts} != {numbers}")
    return False

  #print(f"Consistent {dots} {numbers}")
  return True     

def simplify(dots, nums):
  if not dots and not nums:
    return ['#',], [1,], False
  if dots[0] == '.':
    dots, nums, _ = simplify(dots[1:], nums)
    return dots, nums, True
  if dots[-1] == '.':
    dots, nums, _ = simplify(dots[:-1], nums)
    return dots, nums, True
  if dots[0] == '#':
    dots, nums, _ = simplify(dots[nums[0]+1:], nums[1:])
    return dots, nums, True
  if dots[-1] == '#':
    dots, nums, _ = simplify(dots[:-(nums[-1]+1)], nums[:-1])
    return dots, nums, True
  return dots, nums, False

def cachekey(dots, nums):
  return "".join(dots) + " " + ','.join([str(n) for n in nums])

def expand(dots, nums, cache, i):
  prefix_match = first_consistent(dots, nums)
  if prefix_match == 'N':
    #print(f"Early return on {dots} {nums}")
    return 0
  if prefix_match == 'Y':
    #print(f"Original   is {''.join(dots)} {nums}")
    dots, nums = strip_first(dots, nums)
    #print(f"Simplified to {''.join(dots)} {nums}")
    if not dots and not nums:
      #print("---Success!")
      return 1
    return expand(dots, nums, cache, 0)

  key = cachekey(dots, nums)
  if key in cache:
    return cache[key]

  total = 0
  if i == len(dots):
    if consistent(dots, nums):
      return 1
    return 0
  elif dots[i] == '?':
    dots[i] = '#'
    total += expand(dots, nums, cache, i+1)
    dots[i] = '.'
    total += expand(dots, nums, cache, i+1)
    dots[i] = '?'
  else:
    total += expand(dots, nums, cache, i+1)
  cache[key] = total
  return total



def part2(data):
  total = 0
  cache = dict()
  i=0
  for dots, nums in data:
    print("Working on...  ", ''.join(dots), nums)
    #dots, nums = simplify(dots, nums)
    #print("Simplified", ''.join(dots), nums)
    count = expand(dots, nums, cache, 0)
    print(f"Result row {i} count {count}\n\n\n\n\n")
    total += count
    i+=1
  print(total)

def mymain(filename):
  data = aoc.lines(filename)
  data = list(doparse(data))
  data = list(unfold(data))

  print("Part 2")
  part2(data)

aoc.run(mymain)

