#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)

def tokenize(line):
  i = 0
  tokens = []
  while i < len(line):
    if line[i] == 'e':
      tokens.append('e')
      i+=1
    elif line[i] == 'w':
      tokens.append('w')
      i+=1
    elif line[i:i+2] == 'se':
      tokens.append('se')
      i+=2
    elif line[i:i+2] == 'sw':
      tokens.append('sw')
      i+=2
    elif line[i:i+2] == 'nw':
      tokens.append('nw')
      i+=2
    elif line[i:i+2] == 'ne':
      tokens.append('ne')
      i+=2
    else:
      assert False
  #print(tokens)
  return tokens

def tokens_to_coord(tokens):
  row, col = (0,0)
  for token in tokens:
    if token  == 'e':
      col+=2
    elif token  == 'w':
      col-=2
    elif token == 'se':
      row-=1
      col+=1
    elif token == 'sw':
      row-=1
      col-=1
    elif token == 'ne':
      row+=1
      col+=1
    elif token == 'nw':
      row+=1
      col-=1
  return (row, col)


def get_neighbors(row, col):
  return ((row, col+2),
          (row, col-2),
          (row+1, col+1),
          (row+1, col-1),
          (row-1, col-1),
          (row-1, col+1))


for filename in sys.argv[1:]:
  data = [x.strip() for x in open(filename, 'r').readlines()]

  blacks = set()
  for tile in data:
    coords = tokens_to_coord(tokenize(tile))
    if coords in blacks:
      blacks.remove(coords)
    else:
      blacks.add(coords)
  #pprint.pprint(blacks)
  print("initial",len(blacks)) # part 1


def count_neighbors(row, col, blacks):
  count = 0
  for neighbor in get_neighbors(row, col):
    if neighbor in blacks:
      #print("  neighbor: ",neighbor)
      count+=1
  return count

print(sorted(blacks))

for gameround in range(100):
  newblacks = set()
  # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
  for tile in blacks:
    assert len(tile)==2
    (row,col) = tile
    neighbors = count_neighbors(row, col, blacks)
    if neighbors == 0 or neighbors > 2:
      pass
      #print("%d Neighbors of %s: WHITE" % ( neighbors, tile))
    else:
      #print("%d Neighbors of %s: BLACK" % ( neighbors, tile))
      newblacks.add(tile)
  #print("----"*5)

  # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
  for row in range(-200,200):
    for col in range(-200,200):
      if (row, col) not in blacks:
        neighbors = count_neighbors(row, col, blacks)
        #if neighbors:
        #  #print("%d neighbors of %s" % (neighbors, (row,col)))
        if neighbors == 2:
          newblacks.add((row, col))
  blacks = newblacks
  #print(sorted(newblacks))
  print('round',gameround,len(blacks))

