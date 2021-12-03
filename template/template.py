Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@ericweigle 
ericweigle
/
aoc2020
Public
1
0
0
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
aoc2020/template/template.py /
@ericweigle
ericweigle show an error if you forget the input
Latest commit cc4844a on Dec 13, 2020
 History
 1 contributor
Executable File  22 lines (17 sloc)  330 Bytes
   
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
