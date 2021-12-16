#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc
 
def consume_packet(data, ver_no_sum, off, indent):
  #The three bits labeled V (110) are the packet version, 6.
  if off >= len(data):
    print(" "*indent + "Out of bits")
    sys.exit(1)
  version = int(data[off:off+3],2)
  ver_no_sum[0] += version
  off += 3
  #The three bits labeled T (100) are the packet type ID, 4, which means the packet is a literal value.
  type_id = int(data[off:off+3],2)
  off += 3
  print(" "*indent + f"{version} {type_id}")


  if type_id == 4:
    # literal value
    bits = []
    while True:
      bits.append(data[off+1:off+5])
      print(" "*indent + f"{data[off:off+5]} {bits}")
      if data[off] != '1':
        # last group
        off += 5
        break
      off += 5
    value = int(''.join(bits),2)
  else: # if type_id == 6:
    # operator
    length_type = int(data[off])
    off+=1
    if length_type == 0:
      #If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
      sub_packet_bits = int(data[off:off+15], 2)
      print(" "*indent + f"op15 binary {data[off:off+15]}")
      print(" "*indent + f"op15 {sub_packet_bits}")
      off += 15
      target = off + sub_packet_bits
      while True:
        off = consume_packet(data, ver_no_sum, off, indent+2)
        if off>=target:
          break
    else:
      print(" "*indent + f"op11")
      #If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
      sub_packet_count = int(data[off:off+11],2)
      off += 11
      for i in range(sub_packet_count):
        off = consume_packet(data, ver_no_sum, off, indent+2)

  return off


def part1(data):
  #print(data[0])
  in_bin = ''.join([format(int(x,16), "04b") for x in data])
  print(in_bin)
  #  6   1 B
  #[ 110 001 0 000000001000000 ] [ 000 000 0000001011000010001010101100010110010001000000000100001000 11000111000110100 ]
  ver_no_sum = [0]
  consume_packet(in_bin, ver_no_sum, off=0, indent=0)

  print("version no sum", ver_no_sum)



def part2(data):
  pass

def mymain(filename):
  data = aoc.lines(filename)

  print("Part 1")
  part1(data)

  print("Part 2")
  part2(data)

aoc.run(mymain)

