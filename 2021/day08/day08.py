#!/usr/bin/python3

import sys
import math
import pprint
import copy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)

def parse(filename):
  lines = [x.strip() for x in open(filename, 'r').readlines()]
  result = []
  for line in lines:
    i, o = line.split(' | ')
    result.append([i.split(), o.split()])
  return result

def part1(data):
  count = 0
  for i, o in data:
    #print("iterating",o)
    for val in o:
      if len(val) in (2,3,4,7):
        count+= 1
  print('part 1',count)


def normalize(chars):
  return ''.join(sorted(chars))

def decode(crypto):
  # (1, '  c  f '), # easy
  # (4, ' bcd f '), # easy
  # (7, 'a c  f '), # easy
  # (8, 'abcdefg'), # easy
  # (6, 'ab defg'), # len 6 not containing CF/'1' chars
  # (3, 'a cd fg'), # len 5     containing CF/'1' chars
  # (5, 'ab d fg'), # len 5 containing BD chars
  # (9, 'abcd fg'), # len 6 containing BD chars
  # (2, 'a cde g'), # last len 5
  # (0, 'abc efg'), # last len 6

  one = [x for x in crypto if len(x)==2]
  four = [x for x in crypto if len(x)==4]
  seven = [x for x in crypto if len(x)==3]
  eight = [x for x in crypto if len(x)==7]
  assert len(one) == 1
  assert len(four) == 1
  assert len(seven) == 1
  assert len(eight) == 1
  one =   one[0]
  four =  four[0]
  seven = seven[0]
  eight = eight[0]
  crypto.remove(one)
  crypto.remove(four)
  crypto.remove(seven)
  crypto.remove(eight)

  six = [x for x in crypto if len(x) == 6 and (one[0] not in x or one[1] not in x)]
  assert len(six) == 1
  six = six[0]
  crypto.remove(six)

  three = [x for x in crypto if len(x) == 5 and (one[0] in x and one[1] in x)]
  assert len(three) == 1
  three = three[0]
  crypto.remove(three)

  bd = ''.join([x for x in four if x not in one])

  five = [x for x in crypto if len(x) == 5 and (bd[0] in x and bd[1] in x)]
  assert len(five) == 1
  five = five[0]
  crypto.remove(five)

  nine = [x for x in crypto if len(x) == 6 and (bd[0] in x and bd[1] in x)]
  assert len(nine) == 1
  nine = nine[0]
  crypto.remove(nine)

  two = [x for x in crypto if len(x) == 5]
  assert len(two) == 1
  two = two[0]
  crypto.remove(two)

  zero = crypto[0]
  crypto.remove(zero)

  return {
    normalize(zero): 0,
    normalize(one): 1,
    normalize(two): 2,
    normalize(three): 3,
    normalize(four): 4,
    normalize(five): 5,
    normalize(six): 6,
    normalize(seven): 7,
    normalize(eight): 8,
    normalize(nine): 9
  }

def use_map(mapping, digits):
  result = 0
  for digit in digits:
    result *= 10
    result += mapping[normalize(digit)]
  return result

def part2(data):
  total = 0
  for i, o in data:
    mapping = decode(i)
    digits = use_map(mapping, o)
    #print('result:',digits)
    total+= digits
  print('part 2',total)

for filename in sys.argv[1:]:
  print(f"For file '{filename}'")
  data = parse(filename)
  #print(data)
  part1(copy.deepcopy(data))
  part2(data)
