#!/usr/bin/python3

import pprint
import copy

def effective_row(data, expansion_rate):
  result = dict()
  for r in range(len(data)):
    row = data[r]
    if len(set(row)) == 1 and row[0] =='.':
      result[r] = result.get(r-1, 0)+expansion_rate
    else:
      result[r] = result.get(r-1, 0)+1
  return result

def effective_col(data, expansion_rate):
  result = dict()
  for col in range(len(data[0])):
    transpose = [line[col] for line in data]
    if len(set(transpose)) ==1 and transpose[0]=='.':
      result[col] = result.get(col-1,0) + expansion_rate
    else:
      result[col] = result.get(col-1,0) + 1
  return result

def coordinates(data, eff_r, eff_c):
  result = dict()
  galaxy = 1
  for r in range(len(data)):
    for c in range(len(data[r])):
      if data[r][c]=='#':
        result[galaxy] = (eff_r[r],eff_c[c])
        galaxy += 1
  return result

def distance(a, b):
  return abs(a[0]-b[0]) + abs(a[1]-b[1])

def main(filename, expansion_rate):
  with open(filename, 'r') as f:
    data = [[x for x in line.strip()] for line in f.readlines()]

  effective_r = effective_row(data, expansion_rate)
  effective_c = effective_col(data, expansion_rate)
  #for row in data:
  #  print("".join(row))
  locs = coordinates(data, effective_r, effective_c)
  #pprint.pprint(locs)

  total = 0
  for a in locs.keys():
    for b in locs.keys():
      if a < b:
        total += distance(locs[a], locs[b])
  print(total)

main("example.txt", 1)
main("example.txt", 10)
main("example.txt", 100)
main("input.txt", 1)
main("input.txt", 1000000)
