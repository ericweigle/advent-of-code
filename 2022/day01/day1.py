#!/usr/bin/python3

import pprint

INPUT = "example.txt"
INPUT = "input.txt"

elves = []
for elf in open(INPUT).read().split("\n\n"):
  elves.append([int(x) for x in elf.strip().splitlines()])

print(list(sorted(sum(x) for x in elves)))

