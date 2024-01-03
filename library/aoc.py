"""Board helper library for AOC."""

import os
import sys 

def lines(filename):
  if os.path.isfile(filename):
    return [x.strip() for x in open(filename, 'r').readlines()]
  else:
    print("Warning: treating command line parameter as input.")
    # actually input
    return [filename.strip()]

def ints(filename):
  raw = [x.strip() for x in open(filename, 'r').readlines()]
  result = []
  for line in raw:
    line_value = re.sub('[^0-9]', ' ', line)
    result.append([int(x) for x in line_value.split()])
  if len(result) == 1:
    return result[0]
  return result

def run(callback):
  if len(sys.argv) < 2:
    print("Usage: %s [filename]" % sys.argv[0])
    sys.exit(1)

  for filename in sys.argv[1:]:
    print(f"For file '{filename}'")
    callback(filename)
