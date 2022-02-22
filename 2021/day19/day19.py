#!/usr/bin/python3

import collections

import pickle
import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc
import numpy

def get_scanners(filename):
  def parse_scanner(lines):
    #print(lines)
    result = []
    for line in lines[1:]:
      #print("Parsing",line)
      result.append([int(x) for x in line.split(',')])
    return set(tuple(x) for x in result)

  scanners = open(filename, 'r').read().split("\n\n")
  scanners = [parse_scanner(x.splitlines()) for x in scanners]
  return scanners



def permutation():
  for order in (
    (0,1,2),
    (0,2,1),
    (1,0,2),
    (1,2,0),
    (2,0,1),
    (2,1,0)):
    for posneg in (
      (1,1,1),
      (1,1,-1),
      (1,-1,1),
      (1,-1,-1),
      (-1,1,1),
      (-1,1,-1),
      (-1,-1,1),
      (-1,-1,-1)):
      yield order +posneg


def permute(scanner, rule):
  result = set()
  for line in scanner:
    x = line[rule[0]]*rule[3]
    y = line[rule[1]]*rule[4]
    z = line[rule[2]]*rule[5]
    result.add((x,y,z))
  return result


def beacons_match(beacon1, beacon2, scanner1, scanner2):
  loc = numpy.subtract(beacon1, beacon2)
  beacons = set(tuple(numpy.add(loc,x)) for x in scanner2)
  if len(scanner1.intersection(beacons)) >=12:
    return (beacons, list(loc))

  return (None, None)

def overlap(scanner1, scanner2):
  for i, rule in enumerate(permutation()):
    #print("Permutation",i,rule)
    variant = permute(scanner2, rule)
    for beacon1 in scanner1:
      for beacon2 in variant:
        beacons, scanner = beacons_match(beacon1, beacon2, scanner1, variant)
        if beacons:
          return beacons, scanner
  return (None,None)

def manhattan_distance(p1, p2):
  return (math.fabs(p1[0]-p2[0])+
          math.fabs(p1[1]-p2[1])+
          math.fabs(p1[2]-p2[2]))

def solve(scanners):
  checked = []
  to_check = [scanners[0]]
  all_scanners = [(0,0,0)]
  scanners.pop(0)

  while to_check:
    print("Main loop,",len(to_check),"to check")
    scanner1 = to_check.pop(0)
    to_delete = []
    for j, scanner2 in enumerate(scanners):
      print("  Comparing",j,'of',len(scanners))
      normalized_beacons2, normalized_scanner2 = overlap(scanner1, scanner2)
      if normalized_beacons2:
        print("    Match")
        to_delete.append(j)
        to_check.append(normalized_beacons2)
        all_scanners.append(normalized_scanner2)
        print("    All scanners",all_scanners)
    print("  Deleting",to_delete)
    for j in reversed(to_delete):
      scanners.pop(j)
    checked.append(scanner1)
  print("Finished")
  print("Checked",len(checked))

  # Part 1 solution
  all_beacons = set()
  for scanner in checked:
    for beacon in scanner:
      all_beacons.add(tuple(beacon))
  print("Part 1",len(all_beacons),"beacons")

  # Part 2 solution
  biggest = -99999
  for i in range(len(all_scanners)):
    for j in range(i+1,len(all_scanners)):
      curr = manhattan_distance(all_scanners[i], all_scanners[j])
      if curr > biggest:
        biggest = curr
  print("part 2",biggest)


def mymain(filename):
  scanners = get_scanners(filename)
  solve(scanners)

aoc.run(mymain)

