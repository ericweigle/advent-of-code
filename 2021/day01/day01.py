#!/usr/bin/python3

## Part 1
data = [int(x) for x in open('day01-1.txt','r').readlines()]
increased = 0
for i in range(1,len(data)):
  if data[i]>data[i-1]:
    increased += 1
print(increased)

# Part 2
increased = 0
for i in range(0,len(data)):
   try:
     if (data[i]+data[i+1]+data[i+2]) < (data[i+1] +data[i+2]+data[i+3]):
       increased += 1
   except:
     pass
print(increased)
