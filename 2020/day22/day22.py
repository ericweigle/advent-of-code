#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)


def simulate(p1, p2, game):
  memo = set() # TODO
  print("=== Game %d ===" % game)

  # regular combat
  for round_num in range(1, 1000000):
    # repeated position: p1 wins
    key = (tuple(p1), tuple(p2))
    if key in memo:
      p2 = None
      return True # p1
    else:
      memo.add(key)

    print("\n-- Round %d (Game %d) --" % (round_num, game))
    print("Player 1's deck:",", ".join([str(x) for x in p1]))
    print("Player 2's deck:",", ".join([str(x) for x in p2]))

    c1 = p1.pop(0)
    c2 = p2.pop(0)
    print("Player 1 plays:",c1)
    print("Player 2 plays:",c2)
    #print(c1, c2, len(p1), len(p2))
    if c1 <= len(p1) and c2 <= len(p2):
      print("Playing a sub-game to determine the winner...\n")
      game += 1
      if simulate(copy.deepcopy(p1[:c1]), copy.deepcopy(p2[:c2]), game):
        game -= 1
        print("\n...anyway, back to game %d." % game)
        print("Player 1 wins round %d of game %d!"% (round_num, game))
        p1.append(c1)
        p1.append(c2)
      else:
        game -= 1
        print("\n...anyway, back to game %d." % game)
        print("Player 2 wins round %d of game %d!"% (round_num, game))
        p2.append(c2)
        p2.append(c1)
    else:
      # regular combat
      if c1 > c2:
        print("Player 1 wins round %d of game %d!"% (round_num, game))
        p1.append(c1)
        p1.append(c2)
      elif c2 > c1:
        print("Player 2 wins round %d of game %d!"% (round_num, game))
        p2.append(c2)
        p2.append(c1)
      else: 
        assert False
    if not p1:
      print("The winner of game %d is player 2!"% game)
      break
    if not p2:
      print("The winner of game %d is player 1!"% game)
      break

    #print("")
    #print(p1)
    #print(p2)
  if p1:
    return True
  return False

def score(cards):
  mul = len(cards)
  total = 0
  for card in cards:
    total += mul*card
    mul-=1
  return total


# NOT 32784
# NOT 31235

for filename in sys.argv[1:]:
  p1, p2 = open(filename, 'r').read().split('\n\n')
  p1 = [int(x) for x in p1.splitlines()[1:]]
  p2 = [int(x) for x in p2.splitlines()[1:]]
  #pprint.pprint(p1)
  #pprint.pprint(p2)
  simulate(p1, p2, 1)
  if p1:
    #pprint.pprint(p1)
    print(score(p1))
  else:
    #pprint.pprint(p2)
    print(score(p2))

