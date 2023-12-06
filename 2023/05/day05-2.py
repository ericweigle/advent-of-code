#!/usr/bin/python3

import collections

import copy
import math
import parse
import pprint
import re
import sys
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc

from intervaltree import IntervalTree
from intervaltree import Interval

def parse(filename):
  result = dict()
  data = open(filename, "r").read()
  chunks = data.split("\n\n")
  for chunk in chunks:
    lines = chunk.splitlines()
    assert lines[0].endswith(":")
    name = lines[0].rstrip(":")
    data = [[int(y) for y in x.strip().split()] for x in lines[1:]]
    if name == "seeds":
      result[name] = data[0]
    else:
      src, to, dst = name.split(" ")[0].split("-")
      result[(src,dst)] = data
  return result

def recurse_maps(maps, input_range, source_cat):
  print(f"Lookup for {source_cat}:{input_range}")
  if source_cat == "location":
    return input_range[0]

  for src, dst in maps.keys():
    if src != source_cat:
      continue

    # Found mapping; enforce range
    for dst_range_start, src_range_start, range_len in maps[(src,dst)]:
      # [closed, closed] ranges.
      source_range = (src_range_start, src_range_start+range_len-1)
      dest_range = (dst_range_start, dst_range_start+range_len-1)

      if input_range[0] >= source_range[0] and input_range[1] <= source_range[1]:
        # completely contained in this range, translate + recurse to next level down.
        print(f"Completely contained ({input_range})")
        return recurse_maps(maps, 
            (dest_range[0] + input_range[0]-src_range_start,
             dest_range[0] + input_range[1]-src_range_start),
             dst)
      elif input_range[0] >= source_range[0] and input_range[0] <= source_range[1]:
        # Right overlap; split and try again.
        left = (input_range[0], source_range[1])
        right = (source_range[1]+1, input_range[1])
        print(f"Right overlap ({left}, {right})")
        return min(recurse_maps(maps, left, source_cat),
                   recurse_maps(maps, right, source_cat))
      elif input_range[1] >= source_range[0] and input_range[1] <= source_range[1]:
        # left overlap
        left = (input_range[0], source_range[0]-1)
        right = (source_range[0], input_range[1])
        print(f"Left overlap ({left}, {right})")
        return min(recurse_maps(maps, left, source_cat),
                   recurse_maps(maps, right, source_cat))
      else:
        # no overlap
        continue

    # If we got here, the range maps directly (fall through)
    print(f"Fallthrough ({input_range})")
    return recurse_maps(maps, input_range, dst)


def part2(maps):
  seeds = maps.pop('seeds')
  ranges = []
  for i in range(0,len(seeds),2):
    # [Closed,closed] ranges
    ranges.append((seeds[i], seeds[i]+seeds[i+1]-1))

  best = min([recurse_maps(maps, r, 'seed')
              for r in ranges])

  print(f"Best: {best}")

def mymain(filename):
  maps = parse(filename)
  pprint.pprint(maps)

  print("Part 2")
  part2(maps)

aoc.run(mymain)

