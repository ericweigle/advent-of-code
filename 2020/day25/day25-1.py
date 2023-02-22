#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

def handshake(subject,loops):
  value = 1
  for i in range(loops):
    value = (value * subject) % 20201227
  return value

def get_loopsize1(publickey):
  # Get public keys
  for i in range(1000000):
    #print(handshake(7,i))
    if handshake(7,i)==publickey:
      return i


def get_loopsize2(publickey):
  value = 1
  for i in range(10000000):
    value = (value * 7) % 20201227
    if value==publickey:
      return i+1

# Test
#key1= 5764801
#key2=17807724
## REAL
key1=335121
key2=363891
#print(get_loopsize1(key1))
#print(get_loopsize1(key2))

# WRONG: 17531283
# WRONG: 7516210

#print(get_loopsize1(key1))
#print(get_loopsize2(key1))

#print(handshake(key2,get_loopsize1(key1)))
# CORRECT (for test) 14897079
print(handshake(key1, get_loopsize2(key2)))
