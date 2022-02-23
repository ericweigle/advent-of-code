#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc


class DeterministicDie(object):
  def __init__(self):
    self.value = 1
    self.rolls = 0

  def get(self):
    self.rolls += 1
    to_return = self.value
    self.value += 1
    if self.value > 100:
      self.value = 1
    return to_return

class Player(object):
  def __init__(self, position, score, win_score=1000):
    self.score = score
    self.position = position-1
    self.win_score = win_score

  def move(self, rolls):
    self.position += rolls
    self.position = self.position % 10
    self.score += self.position+1
    return self.score >= self.win_score


def part1():
  #p1 = Player(4, 0)
  #p2 = Player(8, 0)
  p1 = Player(3, 0)
  p2 = Player(5, 0)
  die = DeterministicDie()
  while True:
    if p1.move(die.get() + die.get() + die.get()):
      print("Player 1 wins!")
      print(p2.score * die.rolls)
      return
    if p2.move(die.get() + die.get() + die.get()):
      print("Player 2 wins!")
      print(p1.score * die.rolls)
      return


def part2():
  # key = (p1_pos, p1_score, p2_pos, p2_score)
  # value = universes
  universes = collections.defaultdict(int)
  #universes[(4, 0, 8, 0)] = 1
  universes[(3, 0, 5, 0)] = 1

  dirac_moves = (
    # Roll, universe count
    (3,  1),
    (4,  3),
    (5,  6),
    (6,  7),
    (7,  6),
    (8,  3),
    (9,  1),
  )

  p1_wins = 0
  p2_wins = 0

  while True:
    new_universes = collections.defaultdict(int)
    for universe in universes.keys():
      for roll, universe_count in dirac_moves:
        fanout = universes[universe]*universe_count

        p1 = Player(universe[0], universe[1], 21)
        p2 = Player(universe[2], universe[3], 21)
        if p1.move(roll):
          #print("Player 1 wins!")
          p1_wins += fanout
        else:
          key = (p1.position+1, p1.score, p2.position+1, p2.score)
          new_universes[key] += fanout
    if len(new_universes) == 0:
      break
    universes = new_universes

    new_universes = collections.defaultdict(int)
    for universe in universes.keys():
      for roll, universe_count in dirac_moves:
        fanout = universes[universe]*universe_count

        p1 = Player(universe[0], universe[1], 21)
        p2 = Player(universe[2], universe[3], 21)
        if p2.move(roll):
          #print("Player 2 wins!")
          p2_wins += fanout
        else:
          key = (p1.position+1, p1.score, p2.position+1, p2.score)
          new_universes[key] += fanout
    if len(new_universes) == 0:
      break
    universes = new_universes

  answer = max(p1_wins, p2_wins)
  print(f"Player 1 wins: {p1_wins}; Player 2 wins: {p2_wins}; answer {answer}")

def mymain():
  print("Part 1")
  part1()

  print("Part 2")
  part2()

mymain()

