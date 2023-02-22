#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

for filename in sys.argv[1:]:
  data = [x.strip() for x in open(filename, 'r').readlines()]
  for i in range(len(data)):
    data[i] = [data[i][j] for j in range(len(data[i]))]
  #pprint.pprint(data)

  HEIGHT = len(data)
  WIDTH = len(data[0])

  def adjacencies_pt1(row,col,query):
    count = 0
    for r in (row-1,row,row+1):
      for c in (col-1,col,col+1):
        try:
          if (r==row and c==col) or r<0 or c<0 or r>=HEIGHT or c>=WIDTH:
            continue
          if data[r][c] == query:
            count += 1
        except IndexError:
          pass
    return count

  def adjacencies_pt2(row,col,query):
    count = 0

    for d_r, d_c in [(-1, -1), (0, -1), (1, -1),
                     (-1,  0),          (1,  0),
                     (-1,  1), (0,  1), (1,  1)]:
      r = row
      c = col
      while True:
        r += d_r
        c += d_c
        if r<0 or c<0 or r>=HEIGHT or c>=WIDTH:
          break
        if data[r][c] == 'L':
          break
        if data[r][c] == '#':
          count += 1
          break
    return count

  def automata(data):
    new_data = copy.deepcopy(data)
    for row in range(len(data)):
      for col in range(len(data[0])):
        ## If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        if data[row][col]=='L':
          if adjacencies_pt2(row,col,'#')==0:
            new_data[row][col]='#'
        ## If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
  
        elif data[row][col]=='#':
          if  adjacencies_pt2(row,col,'#')>=5: # 4 for part 1
            new_data[row][col]='L'
        ## Otherwise, the seat's state does not change.
    return new_data

  def total(data, query):
    return sum(sum([1 for x in row if x==query])
               for row in data)

  while True:
    new_data = automata(data)
    #pprint.pprint(automata(data))
    #print("\n")
    if new_data == data:
      break
    data = new_data

  print(total(data, '#'))
