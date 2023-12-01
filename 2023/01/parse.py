#!/usr/bin/python3

import re

def calibrate(digits):
  first = digits[0]
  last = digits[-1]
  return first*10+last

def get_digits(line):
  digits = []
  for i in range(len(line)):
    m = re.match("[0-9]", line[i])
    if m:
      digits.append(int(line[i]))
    elif line[i:].startswith("one"):    
      digits.append(1)
    elif line[i:].startswith("two"):    
      digits.append(2)
    elif line[i:].startswith("three"):  
      digits.append(3)
    elif line[i:].startswith("four"):   
      digits.append(4)
    elif line[i:].startswith("five"):   
      digits.append(5)
    elif line[i:].startswith("six"):    
      digits.append(6)
    elif line[i:].startswith("seven"):  
      digits.append(7)
    elif line[i:].startswith("eight"):  
      digits.append(8)
    elif line[i:].startswith("nine"):   
      digits.append(9)
  print(digits)
  return digits

total = 0
lines = open("input.txt", "r").readlines()
#lines = open("example.txt", "r").readlines()
for line in lines:
  digits = get_digits(line.strip())
  print(calibrate(digits))
  total += calibrate(digits)
print(total)
