#!/usr/bin/python3

import re
import itertools
import sys
import math
import pprint
import copy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)


def parse_line(line):
  m = re.match("^(.*) \(contains (.*)\)$", line)
  assert m
  ingredients = m.group(1).split(' ')
  allergens = [x.strip(',') for x in m.group(2).split(' ')]
  return (ingredients, allergens)


# Takes a dict of {key:str -> set(values)}
def bipartite_match(key_to_values):
  def onlyvalue(my_iterable):
    t = list(my_iterable)
    assert len(t) ==1
    return t[0]

  #print(type(key_to_values))
  result = dict()
  while key_to_values:
    # Find uniquely specified nodes
    for key, values in key_to_values.items():
      if len(values)==1:
        result[key] = onlyvalue(values)
    assert result
    #print("Matched: ",end="")
    #pprint.pprint(result)

    # Remove those as options from the set.
    #print("Used values: ",end="")
    #pprint.pprint(result.values())
    used_values = set(result.values())
    #print("Used values: ",end="")
    #pprint.pprint(used_values)
    residual = dict()
    for key, values in key_to_values.items():
      if key not in result:
        residual[key] = values.difference(used_values)
    key_to_values = residual
    #print("Residual: ",end="")
    #pprint.pprint(residual)

  return result

def main():
  for filename in sys.argv[1:]:
    data = [x.strip() for x in open(filename, 'r').readlines()]
    data = [parse_line(x) for x in data]
    #pprint.pprint(data)

  # Map of ingredients to all possible allergens
  ingredients = dict()
  # Map of allergens to all possible ingredients
  allergens = dict()
  for ing_list, all_list in data:
    #for ingredient in ing_list:
    #  if ingredient not in ingredients:
    #    ingredients[ingredient] = set(all_list)
    #  else:
    #    ingredients[ingredient].update(all_list)
    for allergen in all_list:
      if allergen not in allergens:
        allergens[allergen] = set(ing_list)
      else:
        allergens[allergen].intersection_update(ing_list)
  
  #pprint.pprint(ingredients)
  #pprint.pprint(allergens)
  all_maybes = set(itertools.chain.from_iterable(allergens.values()))
  all_ingredients = set(itertools.chain.from_iterable([x[0] for x in data]))
  all_safe = all_ingredients.difference(all_maybes)
  #pprint.pprint(all_ingredients)
  #pprint.pprint(all_maybes)
  #pprint.pprint(all_safe)
  count = 0
  for ing_list, _ in data:
    for ingredient in ing_list:
      if ingredient in all_safe:
        count += 1
  print('Part 1:', count)

  # allergen -> potential ingredients
  #pprint.pprint(allergens)
  result = bipartite_match(allergens)
  #pprint.pprint(result)
  result = list(sorted([(a, i) for a, i in result.items()]))
  print('Part 2:', ",".join([x[1] for x in result]))

main()
