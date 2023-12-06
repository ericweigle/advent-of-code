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


def recurse_maps(maps, source_val, source_cat):
  print(f"Lookup for {source_cat}:{source_val}")
  for key in maps.keys():
    if key == 'seeds':
      continue
    src, dst = key

    if src == source_cat:
      # Found mapping; enforce range
      for dst_range_start, src_range_start, range_len in maps[(src,dst)]:
        if source_val >= src_range_start and source_val < (src_range_start+range_len):
          dst_val = dst_range_start+(source_val - src_range_start)
          break
        else:
          print(f"  Fail {dst_range_start} {src_range_start} {range_len}")
      else:
        dst_val = source_val
      print(f"Source val {source_cat}:{source_val} maps to dest {dst}:{dst_val}")
  
      # Recurse if re'd
      if dst == "location":
        return dst_val
      else:
        return recurse_maps(maps, dst_val, dst)


def mymain(filename):
  maps = parse(filename)
  #pprint.pprint(maps)

  print("Part 1")
  best = min([recurse_maps(maps, seed_id, 'seed')
              for seed_id in maps['seeds']])
  print(f"Best is {best}")

aoc.run(mymain)

