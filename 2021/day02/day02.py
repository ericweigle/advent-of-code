#!/usr/bin/python3

# Part 1
data = [x.split() for x in open('day02-real.txt','r').readlines()]
#data = [x.split() for x in open('day02-1.txt','r').readlines()]
depth = 0
horiz = 0
for d, amt in data:
  amt = int(amt)
  if d == 'forward':
    horiz += amt
  elif d == 'down':
    depth += amt
  elif d == 'up':
    depth -= amt
  else:
    print("Unknown",d)
print(depth*horiz)

# part 2
aim = 0
depth = 0
horiz = 0
for d, amt in data:
  amt = int(amt)
  if d == 'forward':
    horiz += amt
    depth += aim * amt
  elif d == 'down':
    aim += amt
  elif d == 'up':
    aim -= amt
  else:
    print("Unknown",d)
print(depth*horiz)
