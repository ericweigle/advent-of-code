#!/usr/bin/python3

import re

def count_letter(password, letter):
  count = 0
  for c in password:
    if c == letter:
      count+= 1
  return count

# Part 1
data = [x.split(": ") for x in open('input.txt','r').readlines()]
valid = 0
invalid = 0
for policy, password in data:
  password = password.strip()
  counts, letter = policy.strip().split(" ")
  low, high = counts.split("-")
  low = int(low)
  high = int(high)
  count = count_letter(password, letter)
  if count >= low and count <= high:
    print("Valid: %s" % password)
    valid += 1
  else:
    print("INValid: %s" % password)
    invalid += 1
print("Valid: %d, invalid %d" % (valid, invalid))

# Part 2
data = [x.split(": ") for x in open('input.txt','r').readlines()]
valid = 0
invalid = 0
for policy, password in data:
  password = password.strip()
  counts, letter = policy.strip().split(" ")
  low, high = counts.split("-")
  low = int(low)-1
  high = int(high)-1

  matches = 0
  if low < len(password) and password[low]==letter:
    matches+=1
  if high < len(password) and password[high]==letter:
    matches+=1
  if matches==1:
    print("Valid: %s" % password)
    valid += 1
  else:
    print("INValid: %s" % password)
    invalid += 1
print("Valid: %d, invalid %d" % (valid, invalid))
