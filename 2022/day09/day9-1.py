#!/usr/bin/python3

import collections

import sys
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc


def move_head(way, head):
  if way == 'U':
    return (head[0],head[1]+1)
  elif way == 'D':
    return (head[0],head[1]-1)
  elif way == 'L':
    return (head[0]-1,head[1])
  elif way == 'R':
    return (head[0]+1,head[1])
  else:
    assert False 


def move_tail(head, tail):
  x = head[0]-tail[0]
  y = head[1]-tail[1]
  if max(abs(x),abs(y)) <= 1:
    # Tail doesn't move.
    return tail

  # Same column or row
  if x == 0:
    assert abs(y)==2
    # tail moves up/down
    tail = (tail[0],tail[1]+(y//2))
    return tail
  if y == 0:
    assert abs(x)==2
    # tail moves left/right
    tail = (tail[0]+(x//2),tail[1])
    return tail

  # Diagonal moves
  if abs(x) < 2:
    x = x*2
  if abs(y) < 2:
    y = y*2
  tail = (tail[0]+(x//2), tail[1]+(y//2))
  return tail


def solve(data, length=10):
  visited = set()
  rope = length*[(0,0)]
  visited.add((0,0))
  for way, amount in data:
    for _ in range(amount):
      # head is rope 0
      rope[0] = move_head(way,rope[0])
      # rest is rope [1..9]
      for i in range(1,length):
        rope[i] = move_tail(rope[i-1],rope[i])
      visited.add(rope[-1])
  return len(visited)


def mymain(filename):
  data = aoc.lines(filename)
  data = [v.split() for v in data]
  data = [(x,int(y)) for (x,y) in data]
  #print(data)

  print("Part 1:",  solve(data,length=2))
  print("Part 2:",  solve(data,length=10))

aoc.run(mymain)

