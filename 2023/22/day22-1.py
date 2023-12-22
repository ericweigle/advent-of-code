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

def xyz(s):
  return [int(x) for x in s.split(",")]

def orientation(brick):
  if brick[0][0] == brick[1][0] and  brick[0][1] == brick[1][1]:
    return "Z", abs(brick[0][2]-brick[1][2])+1
  if brick[0][0] == brick[1][0] and  brick[0][2] == brick[1][2]:
    return "Y", abs(brick[0][1]-brick[1][1])+1
  if brick[0][1] == brick[1][1] and  brick[0][2] == brick[1][2]:
    return "X", abs(brick[0][0]-brick[1][0])+1
  raise ValueError(f"Not aligned: {brick}")


def brick_points(brick):
  if brick[0][0] == brick[1][0] and  brick[0][1] == brick[1][1]:
    # "Z"
    lo = min(brick[0][2], brick[1][2])
    hi = max(brick[0][2], brick[1][2])
    return [(brick[0][0], brick[0][1], z) for z in range(lo, hi+1)]
  if brick[0][0] == brick[1][0] and  brick[0][2] == brick[1][2]:
    #"Y"
    lo = min(brick[0][1], brick[1][1])
    hi = max(brick[0][1], brick[1][1])
    return [(brick[0][0], y, brick[0][2]) for y in range(lo, hi+1)]
  if brick[0][1] == brick[1][1] and  brick[0][2] == brick[1][2]:
    #"X"
    lo = min(brick[0][0], brick[1][0])
    hi = max(brick[0][0], brick[1][0])
    return [(x, brick[0][1], brick[0][2]) for x in range(lo, hi+1)]
  raise ValueError(f"Not aligned: {brick}")
 

def get_brick_points(data):
  for line in data:
    a, b = line.split("~")
    brick = (xyz(a), xyz(b))
    #print(f"Orientation: {orientation(brick)}: {brick}")
    assert orientation(brick)[1]<=5
    yield brick_points(brick)


def move(brick, x, y, z):
  pts = []
  for pt in brick:
    pts.append([pt[0]+x, pt[1]+y, pt[2]+z])
  return pts

def move_down(brick):
  return move(brick, 0, 0, -1)

def collides(brick, brick_id, cloud):
  """Returns ([collision], [brick ID collided with])"""
  for pt in brick: 
    pt = tuple(pt)
    if pt in cloud and cloud[pt] != brick_id:
      return (True, cloud[pt])
    if pt[2] < 1: # ground
      return (True, None)
  return (False, None)

def name(brick_id):
  if brick_id is None:
    return "Ground"
  return chr(brick_id+ord('A'))

def bricks_that_would_fall(brick_id, bricks, cloud):
  for pt in bricks[brick_id]:
    cloud.pop(tuple(pt))

  falls = 0
  for other_id in range(len(bricks)):
    if other_id == brick_id:
      continue

    new_brick = move_down(bricks[other_id])
    hits, coll_brick = collides(new_brick, other_id, cloud)
    if hits:
      pass
      #print(f"{name(other_id)} is safe under disintegrate of {name(brick_id)}- resting on {name(coll_brick)}")
    else:
      #print(f"Can't disintegrate {name(brick_id)} because  {name(other_id)} would fall.")
      falls += 1

  for pt in bricks[brick_id]:
    cloud[tuple(pt)] = brick_id

  return falls


def chain_fall(brick_id, bricks, cloud):
  for pt in bricks[brick_id]:
    cloud.pop(tuple(pt))

  tmp_bricks = copy.copy(bricks)
  tmp_cloud = copy.copy(cloud)
  settle_bricks(tmp_bricks, tmp_cloud, brick_id)
  falls = 0
  for i in range(len(bricks)):
    if tuple(bricks[i]) != tuple(tmp_bricks[i]):
      falls += 1

  for pt in bricks[brick_id]:
    cloud[tuple(pt)] = brick_id

  return falls


def settle_bricks(bricks, cloud, ignore_brick_id=None):
  unsettled_ids = set(range(len(bricks)))
  settled_ids = set()
  if ignore_brick_id:
    settled_ids.add(ignore_brick_id)
    unsettled_ids.difference_update(settled_ids)

  while unsettled_ids:
    for brick_id in unsettled_ids:
      old_brick = bricks[brick_id]
      new_brick = move_down(old_brick)
      collided, other_brick_id = collides(new_brick, brick_id, cloud)
      if not collided:
        bricks[brick_id] = new_brick
        for pt in old_brick:
          cloud.pop(tuple(pt))
        for pt in new_brick:
          cloud[tuple(pt)] = brick_id
        continue

      # Collision happened
      if other_brick_id is None: # ground
        #print(f"Settled brick {brick_id} on the ground")
        settled_ids.add(brick_id)
      elif other_brick_id in settled_ids:
        #print(f"Settled brick {brick_id} on top of {other_brick_id}")
        settled_ids.add(brick_id)
    unsettled_ids.difference_update(settled_ids)

def part1(data):
  bricks = list(get_brick_points(data))
  cloud = dict()
  for i, brick in enumerate(bricks):
    for pt in brick:
      cloud[pt] = i
  settle_bricks(bricks, cloud)

  safe_total = 0
  for i in range(len(bricks)):
    if bricks_that_would_fall(i, bricks, cloud)==0:
      safe_total += 1
  print(f"Safe to disintegrate: {safe_total}")

def part2(data):
  bricks = list(get_brick_points(data))
  cloud = dict()
  for i, brick in enumerate(bricks):
    for pt in brick:
      cloud[pt] = i
  settle_bricks(bricks, cloud)

  chain_total = 0
  for i in range(len(bricks)):
    c = chain_fall(i, bricks, cloud)
    print(f"{c} would fall if you disintegrate {i}")
    chain_total += c
  print(f"Chain reaction total: {chain_total}")


def mymain(filename):
  data = aoc.lines(filename)

  print("Part 1")
  part1(data)

  print("Part 2")
  part2(data)

aoc.run(mymain)

