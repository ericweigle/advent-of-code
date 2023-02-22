#!/usr/bin/python3

import re
import sys

all_fields = (
  'byr', #  ("Birth Year", ),
  'iyr', #  ("Issue Year", ),
  'eyr', #  ("Expiration Year", ),
  'hgt', #  ("Height", True),
  'hcl', #  ("Hair Color", ),
  'ecl', #  ("Eye Color", ),
  'pid', #  ("Passport ID", ),
  'cid', #  ("Country ID", ), # valid if only field missing
)

def is_passport_valid(passport):
  fields = passport.strip().split(" ")
  fields = [x.strip() for x in fields]
  fields = [x for x in fields if x]
  for field in fields:
    assert len(field.split(":"))==2
  keys = [x.split(":")[0] for x in fields]
  assert len(keys) == len(set(keys))
  matches = set(keys).intersection(all_fields)

  print("")
  print(passport.strip())
  if not ((len(matches) == len(all_fields)) or (len(matches) == (len(all_fields)-1) and 'cid' not in matches)):
    #print(" INVALID  missing fields")
    return 0

  v = dict(x.split(":") for x in fields)
  print(v)
  #byr (Birth Year) - four digits; at least 1920 and at most 2002.
  if len(v['byr'])!=4 or int(v['byr']) < 1920 or int(v['byr'])>2002:
    print("  INVALID byr (Birth Year) - four digits; at least 1920 and at most 2002." + v['byr'])
    return 0
  #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
  if len(v['iyr'])!=4 or int(v['iyr']) < 2010 or int(v['iyr'])>2020:
    print("  INVALID iyr (Issue Year) - four digits; at least 2010 and at most 2020." + v['iyr'])
    return 0
  #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
  if len(v['eyr'])!=4 or int(v['eyr']) < 2020 or int(v['eyr'])>2030:
    print("  INVALID eyr (Expiration Year) - four digits; at least 2020 and at most 2030." + v['eyr'])
    return 0
  #hgt (Height) - a number followed by either cm or in:
  if re.match("^[0-9]+cm$", v['hgt']):
    # If cm, the number must be at least 150 and at most 193.
    h = int(v['hgt'][:-2])
    if h < 150 or h > 193:
      print(" INVALID height cm cm, the number must be at least 150 and at most 193. " + v['hgt'])
      return 0
  elif re.match("^[0-9]+in$", v['hgt']):
    # If in, the number must be at least 59 and at most 76.
    h = int(v['hgt'][:-2])
    if h < 59 or h > 76:
      print(" INVALID height in, the number must be at least 59 and at most 76." + v['hgt'])
      return 0
  else:
    print(" INVALID height not in in/cm " + v['hgt'])
    return 0

  #  hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
  if not re.match("^#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$", v['hcl']):
    print("  INVALID hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f." + v['hcl'])
    return 0

  #  ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
  if v['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
    print("  INVALID ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth." + v['ecl'])
    return 0

  #  pid (Passport ID) - a nine-digit number, including leading zeroes.
  if not re.match('^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$', v['pid']):
    print("   INVALID pid (Passport ID) - a nine-digit number, including leading zeroes. " +  v['pid'])
    return 0

  result = []
  for key in sorted(all_fields):
    if key in v:
      result.append(key+':'+v[key])
  print("  VALID! " + "\t".join(result))
  return 1


for filename in sys.argv[1:]:
  print("For %s" % filename)
  data = [x.strip() for x in open(filename, 'r').readlines()]
  passport = ""
  count = 0
  for line in data:
    if not line:
      count += is_passport_valid(passport)
      passport = ""
    passport = passport + " " + line
  if passport:
    count += is_passport_valid(passport)
  print("Count is %d" % count)

# part one was 2, 264
# part 2 was 224...

