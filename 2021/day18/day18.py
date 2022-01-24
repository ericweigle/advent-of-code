#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc


def flat_parse_num(str_num):
  result = []
  for c in str_num:
    if c in set(str(x) for x in range(10)):
      # Turn integers into ints; they may be multi-digit.
      v = int(c)
      if type(result[-1]) is int:
        result[-1] = result[-1]*10+v
      else:
        result.append(v)
    else:
      result.append(c)
  return result

def cat_num(num):
  return ''.join(str(x) for x in num)

def explode_str(num : str):
  #print("Input:",num)
  split_num = flat_parse_num(num)
  depth = 0
  for i, c in enumerate(split_num):
    if c == '[':
      depth += 1
    elif c == ']':
      depth -= 1
    if depth == 5:
      #print("Exploding",split_num[i+1], split_num[i+2], split_num[i+3])
      # Propagate left
      for j in range(i,-1,-1):
        if type(split_num[j]) is int:
          split_num[j]+= split_num[i+1]
          break
      # Propagate right
      for j in range(i+4,len(split_num)):
        if type(split_num[j]) is int:
          split_num[j]+= split_num[i+3]
          break
      # Remove exploded number
      split_num[i:i+5] = '0'
      result = cat_num(split_num)
      #print("output:",result)
      return result
  return num

def split_str(num: str):
  #print("Running split on",num)
  split_num = flat_parse_num(num)
  for i, c in enumerate(split_num):
    #print(type(c))
    if type(c) is int and c>= 10:
      left = c // 2
      right = c - left
      #print("splitting",c,'to',left,right)
      split_num[i] = f'[{left},{right}]'
      result=cat_num(split_num)
      #print("result",result)
      return result
  return num

#example = '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'
#example=explode_str(example)
#example=explode_str(example)
#print(flat_parse_num(example))

#def explode_num(num, depth=0):
#  assert len(num) == 2
#  if depth == 4:
#    print("exploding",num)
#    return num
#
#  left, right = num
#  if type(left) is not int:
#    to_explode = get_leaf(left, depth+1)
#    if to_explode:
#      return a
#  if type(right) is not int:
#    to_explode = get_leaf(right, depth+1)
#    if to_explode:
#  return (0,0)
# 
#print(explode_num([[[[[9,8],1],2],3],4]))

 
def do_reduce(num:str):
  while True:
    x = explode_str(num)
    if x == num:
      x = split_str(num)
      if x == num:
        return num
      num = x
    else:
      num = x

def add(n1: str, n2: str):
  #print("Adding",n1,"+",n2)
  result = f'[{n1},{n2}]'
  #print("result",result)
  result=do_reduce(result)
  #print("Final reduce",result)
  return result


def magnitude(num):
  if type(num) is int:
    return num
  return 3*magnitude(num[0]) + 2*magnitude(num[1])

def part1(lines):
  val = lines[0]
  for to_add in lines[1:]:
    val = add(val, to_add)
  print(val)
  print("Magnitude",magnitude(eval(val)))
  #print("Magnitude",magnitude(eval('[[1,2],[[3,4],5]]')))
  #print("Magnitude",magnitude(eval('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')))

def part2(lines):
  v = 0
  for i in range(len(lines)):
    print(i)
    for j in range(i+1,len(lines)):
      if i != j:
        m1 = magnitude(eval(add(lines[i], lines[j])))
        m2 = magnitude(eval(add(lines[j], lines[i])))
        v = max(v,m1)
        v = max(v,m2)
  print(v)

def mymain(filename):
  data = aoc.lines(filename)
  print("Part 1")
  part1(data)

  print("Part 2")
  part2(data)

aoc.run(mymain)
