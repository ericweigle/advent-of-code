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

def parse_cards(data):
  result = []
  for line in data:
    cards, bid = line.split()
    result.append((tuple([x for x in cards]), int(bid)))
  return result

def strength(card):
  return {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2}[card]

def category(hand):
  hist = dict()
  for card in hand:
    hist[card] = hist.get(card, 0) + 1
  #print(f"Hand {hand} hist {hist}")

  if len(hist) == 1:
    # five of a kind
    return 7
  if 4 in hist.values():
    # four of a kind
    return 6
  if 3 in hist.values():
    if 2 in hist.values():
      # full house
      return 5
    else:
      # 3 of a kind
      return 4
  if len(hist) == 3:
    cards = list(hist.keys())
    if ((hist[cards[0]] == 2 and hist[cards[1]]==2) or
        (hist[cards[0]] == 2 and hist[cards[2]]==2) or
        (hist[cards[1]] == 2 and hist[cards[2]]==2)):
      # two pair
      return 3
  if 2 in hist.values():
    # one pair
    return 2
  if len(hist) == 5:
    return 1
  print(f"Did not determine hand {hand}")
  sys.exit(1)


def hand_strength(hand):
  assert len(hand) == 5
  result = (category(hand), tuple(strength(c) for c in hand))
  # print(f"strength {result}")
  return result


def part1(data):
  hands = list(parse_cards(data))
  #print(hands)
  #print(hand_strength(hands[0][0]))
  hands = list(sorted(hands, key=lambda x: hand_strength(x[0])))
  print(hands)

  winnings = 0
  for i in range(len(hands)):
    winnings += (i+1)*hands[i][1]
  print(f"winnings {winnings}")


def part2(data):
  pass

def mymain(filename):
  data = aoc.lines(filename)

  print("Part 1")
  part1(data)

  print("Part 2")
  part2(data)

aoc.run(mymain)

