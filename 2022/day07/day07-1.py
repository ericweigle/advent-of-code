#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc


def part1(data):
  pass


def part2(data):
  pass


def path2str(path):
  return '/'.join(path)


class MyDir(object):
  def __init__(self):
    self.path = None
    self.parent = None
    self.files = {}
    self.dirs = dict()


def get_sizes(root, eligible=[]):
  total = 0
  for child in root.dirs.keys():
    total += get_sizes(root.dirs[child])[0]
  for filename in root.files.keys():
    total += root.files[filename]
  #print(f"Size of {root.path}: {total}")
  if total <= 100000:
    eligible.append(total)
  return total, eligible


def find_smallest_above(root, required, eligible=[]):
  total = 0
  for child in root.dirs.keys():
    total += find_smallest_above(root.dirs[child], required)[0]
  for filename in root.files.keys():
    total += root.files[filename]
  #print(f"2 Size of {root.path}: {total}")
  if total >= required:
    eligible.append(total)
  #else:
  #  print("Too small")
  return total, eligible



def mymain(filename):
  lines = [x for x in open(filename, 'r').read().split("$") if x]
  lines = [x.strip().splitlines() for x in lines]
  #print(lines)

  root = MyDir()
  root.path = "/"

  cur_path = None
  for command in lines:
    #pprint.pprint(command)
    if command[0].startswith("cd "):
      # Directories
      assert len(command) == 1
      new_path = command[0][len("cd "):].strip()
      if new_path == '/':
        cur_path = root
      elif new_path == "..":
        cur_path = cur_path.parent
      else:
        assert new_path in cur_path.dirs
        cur_path = cur_path.dirs[new_path]
        #if new_path not in cur_path.dirs:
        #  cur_path.dirs[new_path] = MyDir()
        #  cur_path.dirs[new_path].parent = cur_path
      #print(f"New path '{new_path}' current path {cur_path}")
      #print('/'.join(cur_path))
    elif command[0] == 'ls':
      for line in command[1:]:
        if line.startswith("dir "):
          dirname = line[len("dir "):].strip()
          if dirname not in cur_path.dirs:
            cur_path.dirs[dirname] = MyDir()
            cur_path.dirs[dirname].parent = cur_path
            cur_path.dirs[dirname].path = f'{cur_path.path}/{dirname}'
        else:
          size, name = line.split(" ")
          if name not in cur_path.files:
            cur_path.files[name] = int(size)
    else:
      print(f"Unknown command {command}")

  total, eligible = get_sizes(root)
  print('PART 1 answer: ',sum(eligible))

  free_space = 70000000-total
  #print("Free space", free_space)
  required = 30000000-free_space
  #print("Required",required)
  print('PART 2 answer: ',sorted(find_smallest_above(root, required)[1])[0])


aoc.run(mymain)
