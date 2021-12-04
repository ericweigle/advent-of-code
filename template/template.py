#!/usr/bin/python3

import re
import sys
import math
import pprint
import copy

if len(sys.argv) < 2:
  print("Usage: %s [filename]" % sys.argv[0])
  sys.exit(1)


for filename in sys.argv[1:]:
  data = [x.strip() for x in open(filename, 'r').readlines()]

  if len(data) < 100:
    # example
    pass
  else:
    # real
    pass
