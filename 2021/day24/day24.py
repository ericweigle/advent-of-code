#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/2021/day24/')
import aoc
import random
import pyalu

class Alu(object):
  def __init__(self, input_list):
    self.w = 0
    self.x = 0
    self.y = 0
    self.z = 0
    self.input_list = input_list

  def _set(self, var, value):
    if var == 'w':
      self.w = value
    elif var == 'x':
      self.x = value
    elif var == 'y':
      self.y = value
    elif var == 'z':
      self.z = value
    else:
      print(f"failed to find {var}")
      assert var in ('w', 'x', 'y', 'z')

  def _get(self, var):
    if var == 'w':
      return self.w
    elif var == 'x':
      return self.x
    elif var == 'y':
      return self.y
    elif var == 'z':
      return self.z
    else:
      return int(var)

  def execute(self, cmd, op1, op2):
    if cmd == 'inp':
      self._set(op1, self.input_list.pop(0))
    elif cmd == 'add':
      self._set(op1, self._get(op1) + self._get(op2))
    elif cmd == 'mul':
      self._set(op1, self._get(op1) * self._get(op2))
    elif cmd == 'div':
      self._set(op1, self._get(op1) // self._get(op2))
    elif cmd == 'mod':
      self._set(op1, self._get(op1) % self._get(op2))
    elif cmd == 'eql':
      if self._get(op1)==self._get(op2):
        self._set(op1, 1)
      else:
        self._set(op1, 0)

  def dump_registers(self):
    print("Registers")
    #print(f"  w={self.w}")
    #print(f"  x={self.x}")
    print(f"  y={self.y}")
    print(f"  z={self.z}")

def parse(data):
  """Returns list of (instruction, operand1, operand2)."""
  result = []
  for line in data:
    ops = line.split()
    if len(ops) == 3:
      result.append(ops)
    elif len(ops) == 2:
      assert ops[0]=='inp'
      result.append([ops[0],ops[1],None])
  return result

def validate_number(number:int):
  assert number>=10000000000000 and number <=99999999999999
  model_no = [int(x) for x in str(number)]
  for x in model_no:
    if x==0:
      return None
  return model_no 


def run_alu(number, program):
  model_no = validate_number(number)
  if model_no is None:
    return None

  alu = Alu(model_no)
  for cmd, op1, op2 in program:
    alu.execute(cmd, op1, op2)
  return alu.z


def py_alu(number):
  model_no = validate_number(number)
  if model_no is None:
    return None
  return pyalu.pyalu(model_no)


def part1(data):
  program = parse(data)

#   Invariant: d0    == d13
#   Invariant: d3+4  == d4
#   Invariant: d6-6  == d7
#   Invariant: d5-5  == d8
#   Invariant: d2-7  == d9
#   Invariant: d1+6  == d10
#   Invariant: d11+1 == d12
# Smallest            01234567890123
  print('ALU:',py_alu(11815671117121))

# Highest             01234567890123
  print('ALU:',py_alu(93959993429899))
  for i in range(5000):
    number = random.randint(10000000000000,99999999999999)
    assert run_alu(number, program)==py_alu(number)
  print("OK!")
   

def mymain(filename):
  data = aoc.lines(filename)

  print("Part 1")
  part1(data)

aoc.run(mymain)

