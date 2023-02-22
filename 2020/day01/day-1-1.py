#!/usr/bin/python3

# Part 1
data = [int(x) for x in open('day-1-1.txt','r').readlines()]
for i in range(len(data)):
  for j in range(len(data)):
    if i == j:
      continue
    if (data[i] + data[j]) == 2020:
      print(data[i]*data[j])

# Part 2
for i in range(len(data)):
  for j in range(len(data)):
    for k in range(len(data)):
      if i == j or i == k or j == k:
        continue
      if (data[i] + data[j] + data[k]) == 2020:
        print(data[i]*data[j]*data[k])
