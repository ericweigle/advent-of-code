#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)


def raw_flip_horiz(lines):
  return [x[::-1] for x in lines]

def raw_rotate_clock(lines):
  newlines = []
  for column in range(len(lines[0])):
    chars = [line[column] for line in reversed(lines)]
    newlines.append(''.join(chars))
  return newlines

#def borders(tile):
#  return {
#      't': tile[0], # top
#      'b': tile[-1], # bottom,
#      'l': ''.join([x[0] for x in tile]), # left
#      'r': ''.join([x[-1] for x in tile]), # right
#  }
# 
#def all_borders(tile):
#  raw = list(borders(tile))
#  raw.append(raw[0][::-1])
#  raw.append(raw[1][::-1])
#  raw.append(raw[2][::-1])
#  raw.append(raw[3][::-1])
#  return raw


def strip_border(raw_tile):
  lines = raw_tile[1:-1]
  lines = [x[1:-1] for x in lines]
  return lines

def parse(raw_tile):
  #pprint.pprint(raw_tile)
  #pprint.pprint(strip_border(raw_tile))
  result = {
      # raw characters
      'tile': raw_tile, # strip_border(raw_tile),
      # borders
      't': raw_tile[0], # top
      'b': raw_tile[-1], # bottom,
      'l': ''.join([x[0] for x in raw_tile]), # left
      'r': ''.join([x[-1] for x in raw_tile]), # right
      # bordering tile number
      'bt': None,
      'bb': None,
      'bl': None,
      'br': None,
      'num': num,
  }
  # borders in other direction
  result['t'] = set([result['t'],result['t'][::-1]])
  result['b'] = set([result['b'],result['b'][::-1]])
  result['l'] = set([result['l'],result['l'][::-1]])
  result['r'] = set([result['r'],result['r'][::-1]])
  return result


def flip_horiz(tile):
  other = copy.deepcopy(tile)
  other['tile'] = raw_flip_horiz(tile['tile'])
  other['l'] = tile['r']
  other['r'] = tile['l']
  other['bl'] = tile['br']
  other['br'] = tile['bl']
  return other

# Rotate clockwise
def rotate(tile):
  other = copy.deepcopy(tile)

  # raw characters
  other['tile'] = raw_rotate_clock(tile['tile'])
  # borders
  other['t'] = tile['l']
  other['b'] = tile['r']
  other['l'] = tile['b']
  other['r'] = tile['t']
  # bordering tile number
  other['bt'] = tile['bl']
  other['bb'] = tile['br']
  other['bl'] = tile['bb']
  other['br'] = tile['bt']

  return other


def make_top_left(tile):
  for flip in (False, True):
    for rot in range(4):
      if tile['br'] and tile['bb']:
        return tile
      tile = rotate(tile)
    tile = flip_horiz(tile)
  assert False


def align_right(base, neighbor):
  side = ''.join([x[-1] for x in base['tile']]) # right side, read from top
  for flip in (False, True):
    for rot in range(4):
      if side == ''.join([x[0] for x in neighbor['tile']]): # left side, read from top
        return neighbor
      neighbor = rotate(neighbor)
    neighbor = flip_horiz(neighbor)
  assert False


def align_down(base, neighbor):
  side = base['tile'][-1] # bottom
  for flip in (False, True):
    for rot in range(4):
      if side == neighbor['tile'][0]: # top
        return neighbor
      neighbor = rotate(neighbor)
    neighbor = flip_horiz(neighbor)
  assert False


def is_corner(tile):
 adjacent = 0
 for border in ('bt', 'bb', 'bl', 'br'):
   if tile[border]:
     adjacent += 1
 return adjacent==2


def do_layout(row, col, tiles, layout):
  base = layout[row][col]
  #pprint.pprint(base)
  if base['bb'] and layout[row+1][col] is None:
    # Grow down
    #print("Grow down") 
    neighbor = tiles.pop(base['bb'])
    layout[row+1][col] = align_down(base, neighbor)
    do_layout(row+1,col, tiles, layout)
  if base['br'] and layout[row][col+1] is None:
    # Grow right
    #print("Grow right")
    neighbor = tiles.pop(base['br'])
    layout[row][col+1] = align_right(base, neighbor)
    do_layout(row,col+1, tiles, layout)

def count_monster(board):
  count = 0
  for row in range(len(board)-2):
    for col in range(len(board[row])):
      if (re.match("^..................#", board[row][col:]) and 
          re.match("^#....##....##....###", board[row+1][col:]) and 
          re.match("^.#..#..#..#..#..#", board[row+2][col:])):
        count += 1
  return count

def count_monsters(board, roughness):
  mine = copy.deepcopy(board)
  for flip in (False, True):
    for rot in range(4):
      monsters = count_monster(board)
      if monsters>0:
        print("Part 2:",roughness-15*monsters)
        #print(monsters, roughness-15*monsters)
      board = raw_rotate_clock(board)
    board = raw_flip_horiz(board)

for filename in sys.argv[1:]:
  tiles = open(filename, 'r').read().split('\n\n')
  #pprint.pprint(tiles)
  results = dict()
  for tile in tiles:
    #print(tile)
    lines = tile.splitlines()
    num = int(re.findall("\d+", lines[0])[0])
    tile = lines[1:]
    results[num] = parse(lines[1:])
    #pprint.pprint(results[num])
    #print(borders(lines[1:]))
    #sys.exit(1)
  tiles = results
  #pprint.pprint(tiles)

  for num1, tile1 in tiles.items():
    for border1 in ('t', 'b', 'l', 'r'):
      for num2, tile2 in tiles.items():
        if num1 != num2:
          for border2 in ('t', 'b', 'l', 'r'):
            if tile1[border1].intersection(tile2[border2]):
              tile1['b'+border1] = num2
              tile2['b'+border2] = num1
  #pprint.pprint(tiles)

  chosen_corner = None
  mul = 1
  for num, tile in tiles.items():
    if is_corner(tile):
      #print("%d is a corner" % num)
      #pprint.pprint(tile)
      mul *= num  
      chosen_corner = num
  print("Part 1:",mul)

  #pprint.pprint(tiles[chosen_corner])
  top_left = make_top_left(tiles[chosen_corner])
  # Build off chosen corner
  #print("Top left")
  #pprint.pprint(top_left)

  if len(tiles) == 9:
    rows = 3
    cols = 3
  elif len(tiles) == 144:
    rows = 12
    cols = 12

  layout = [None]*rows
  for row in range(rows):
    layout[row] = [None]*rows
  layout[0][0] = top_left
  tiles.pop(top_left['num'])
  #print(len(tiles))

  do_layout(0,0, tiles, layout)
  #print(len(tiles))

  for row in range(rows):
    for col in range(cols):
      layout[row][col]['tile'] = strip_border(layout[row][col]['tile'])

  board = []
  for bigrow in range(rows):
    for littlerow in range(len(layout[row][col]['tile'])):
      line = []
      for bigcol in range(cols):
        line.append(layout[bigrow][bigcol]['tile'][littlerow])
      board.append("".join(line))
  #pprint.pprint(board)

  roughness = 0
  for line in board:
    roughness += len(re.findall('#', line))
  #print("Roughness: %d" % roughness)

  count_monsters(board, roughness)
