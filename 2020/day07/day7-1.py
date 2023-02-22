#!/usr/bin/python3

import re
import sys
import math
import pprint

# part 1
#for filename in sys.argv[1:]:
#  print("For %s" % filename)
#  data = [x.strip() for x in open(filename, 'r').readlines()]
#  data = [re.sub("bags", "bag", x) for x in data]
#
#  all_outer = set()
#  all_inner = set(("shiny gold bag",),)
#  while True:
#    for line in data:
#      outer, inner = line.split(" contain ")
#      for search in all_inner:
#        if search in inner:
#          print("Can use a %s because %s" % (outer, search))
#          all_outer.add(outer)
#          all_inner.add(outer)
#          break
#      print("Total options %d" % len(all_outer))
#      ##contents = [x.strip() for x in contents.split(",")]
#      #print(outer)
#      #print(inner)

def parsenum(x):
  return (int(x.split(' ')[0]), re.sub("^[0-9]+ ", "", x))


def count_content(mydict, root, depth=0):
  print("searching ",root)
  contents = mydict[root]
  total = 0
  if not contents:
    print(" " * depth + "Returning size 1")
    return 1
  for num, sub_bag in contents:
    total += num*count_content(mydict, sub_bag, depth+1)
    print(" " * depth + "current total %d" % total)
  return 1+total


for filename in sys.argv[1:]:
  print("For %s" % filename)
  data = [x.strip() for x in open(filename, 'r').readlines()]
  data = [re.sub("bags", "bag", x) for x in data]

      ##contents = [x.strip() for x in contents.split(",")]

  mydict = dict()
  for line in data:
    outer, inner = line.split(" contain ")
    mydict[outer] = [x.strip().strip('.') for x in inner.split(',')]
    mydict[outer] = [x for x in mydict[outer] if x != 'no other bag']
    mydict[outer] = [(int(x.split(' ')[0]), re.sub("^[0-9]+ ", "", x)) for x in mydict[outer]]
    #print (outer, mydict[outer])
  pprint.pprint(mydict)

  print(count_content(mydict, "shiny gold bag")-1)
#  # brute force memoization
#  known_sizes = dict()
#  while len(known_sizes) < len(mydict):
#    for outer, inner in mydict.items():
#      if outer not in known_sizes:
#        if not inner:
#          known_sizes[outer] = 1
#        else:
#          total = 0
#          for count, sub_bag in inner:
#            if sub_bag in known_sizes:
#              total += count * known_sizes[sub_bag]
#            else:
#              total = 0
#              break
#          if total:
#            known_sizes[outer] = total+1
#  pprint.pprint(known_sizes)
#  print(known_sizes["shiny gold bag"]-1)
