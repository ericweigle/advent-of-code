#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc
 
def apply_op(type_id, subpacket_values, indent):
  print(" "*indent + f"applying op {type_id} against {subpacket_values}")
  # Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
  if type_id == 0:
    return(sum(subpacket_values))
  # Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
  if type_id == 1:
    v = 1
    for x in subpacket_values:
      v *= x
    return v
  # Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
  if type_id == 2:
    return min(subpacket_values)
  # Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
  if type_id == 3:
    return max(subpacket_values)
  # Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
  if type_id == 5:
    assert len(subpacket_values) == 2
    return 1 if subpacket_values[0] > subpacket_values[1] else 0

  # Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
  if type_id == 6:
    assert len(subpacket_values) == 2
    return 1 if subpacket_values[0] < subpacket_values[1] else 0

  # Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
  if type_id == 7:
    assert len(subpacket_values) == 2
    return 1 if subpacket_values[0] == subpacket_values[1] else 0

  assert False

ver_no_sum = [0]
def consume_packet(data, packet_value, indent):
  print(" "*indent + f"Working with {data}")
  # Header is six bits long. If less than that, we're residual.
  #The three bits labeled V (110) are the packet version, 6.
  if len(data) < 6:
    print(" "*indent + f"Out of bits: {data}")
    return data
  version = int(data[:3],2)
  ver_no_sum[0] += version
  data = data[3:]
  #The three bits labeled T (100) are the packet type ID, 4, which means the packet is a literal value.
  type_id = int(data[:3],2)
  data = data[3:]

  print(" "*indent + f"{version} {type_id}")

  if type_id == 4:
    print(" "*indent + f"literal value {data[:5]} {data[5:10]} {data[10:15]} ...")
    # literal value
    bits = []
    while True:
      last_group = data[0]
      bits.append(data[1:5])
      data = data[5:]
      print(" "*indent + f"{data[:5]} {bits}")
      if last_group != '1':
        break
    value = int(''.join(bits),2)
    print(" "*indent + f"parsed binary: {value}")
    packet_value.append(value)
  else: # if type_id == 6:
    # operator
    length_type = int(data[0])
    data = data[1:]
    if length_type == 0:
      #If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
      sub_packet_bits = int(data[:15], 2)
      print(" "*indent + f"subpacket length binary: {data[:15]}")
      print(" "*indent + f"subpacket length parsed: {sub_packet_bits}")
      data = data[15:]
      print(" "*indent + f"residual: {data}")
      subpacket_values = []
      sub_data = data[:sub_packet_bits]
      while len(sub_data) > 6:
        print(" "*indent + "going on...")
        sub_data = consume_packet(sub_data, subpacket_values, indent+2)
      print(" "*indent + f"done with sub-parse {subpacket_values}...")
      data = data[sub_packet_bits:]
      packet_value.append(apply_op(type_id, subpacket_values, indent))
    else:
      #If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
      sub_packet_count = int(data[:11],2)
      print(" "*indent + f"subpacket count binary: {data[:11]}")
      print(" "*indent + f"subpacket count parsed: {sub_packet_count}")
      data = data[11:]
      print(" "*indent + f"residual: {data}")
      subpacket_values = []
      for i in range(sub_packet_count):
        data = consume_packet(data, subpacket_values, indent+2)
      packet_value.append(apply_op(type_id, subpacket_values, indent))

  return data


def part1(data):
  in_bin = ''.join([format(int(x,16), "04b") for x in data])
  #  6   1 B
  #[ 110 001 0 000000001000000 ] [ 000 000 0000001011000010001010101100010110010001000000000100001000 11000111000110100 ]
  packet_value = []
  consume_packet(in_bin, packet_value, indent=0)

  assert ver_no_sum[0] == 974
  print("version no sum", ver_no_sum)
  assert packet_value[0] == 180616437720
  print("packets value", packet_value)

def mymain(filename):
  data = aoc.lines(filename)

  print("Part 1")
  part1(data[0])

aoc.run(mymain)

