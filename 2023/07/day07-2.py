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
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1,
    }[card]

def two_pair(hist):
  cards = list(hist.keys())
  return len(hist) == 3 and (
      (hist[cards[0]] == 2 and hist[cards[1]]==2) or
      (hist[cards[0]] == 2 and hist[cards[2]]==2) or
      (hist[cards[1]] == 2 and hist[cards[2]]==2))

def category(hand):
  hist = dict()
  for card in hand:
    hist[card] = hist.get(card, 0) + 1
  #print(f"Hand {hand} hist {hist}")

  jokers = hist.get('J', 0)

  if jokers == 5:
    return 7 # 5 of a kind
  if jokers == 4:
    return 7 # 5 of a kind
  if jokers == 3:
    if len(hist) == 2:
      return 7 # 5 of a kind
    else:
      return 6 # 4 of a kind
  if jokers == 2:
    if len(hist) == 2:
      return 7 # 5 of a kind
    if two_pair(hist):
      return 6 # 4 of a kind
    # Can never achieve full house (score 5)
    # without also being able to do 4 of a kind
    return 4 # three of a kind is the worst we can do
  if jokers == 1:
    if len(hist) == 2:
      return 7 # 5 of a kind
    if 3 in hist.values():
      return 6 # 4 of a kind
    if two_pair(hist):
      return 5 # full house
    if 2 in hist.values():
      return 4 # 3 of a kind
    # Never do 2 pair here; we can always reach 3 of a kind
    return 2 # one pair

  if len(hist) == 1:
    return 7 # five of a kind

  if 4 in hist.values():
    return 6 # four of a kind

  if 3 in hist.values():
    if 2 in hist.values():
      return 5 # full house.
    return 4 # 3 of a kind

  if two_pair(hist):
    return 3 # two pair

  if 2 in hist.values():
    return 2 # one pair

  if len(hist) == 5:
    return 1
  print(f"Did not determine hand {hand}")
  sys.exit(1)


def hand_strength(hand):
  assert len(hand) == 5
  result = (category(hand), tuple(strength(c) for c in hand))
  # print(f"strength {result}")
  return result

def part2(data):
  hands = list(parse_cards(data))
  print(hands)
  #print(hand_strength(hands[0][0]))
  hands = list(sorted(hands, key=lambda x: hand_strength(x[0])))
  print(hands)

  winnings = 0
  for i in range(len(hands)):
    winnings += (i+1)*hands[i][1]
  print(f"winnings {winnings}")


def mymain(filename):
  data = aoc.lines(filename)

#  for hand in possible_hands(["J", "2", "J", "4", "5"]):
#    print(hand)
  print("Part 2")
  part2(data)

aoc.run(mymain)

