#!/usr/bin/python3

import copy
import pprint
import sys
import time
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
sys.path.insert(1, '/home/ehw/projects/advent-of-code/library/')
import aoc


def parse(lines):
  raw_data = dict()
  for line in lines:
    parts = line.split()
    valve = parts[1]
    rate = int(parts[4].split('=')[1].strip(';'))
    tunnels = [x.strip(',') for x in parts[9:]]

    #print(valve, rate, tunnels)
    raw_data[valve] = (rate, tunnels)
  #pprint.pprint(raw_data)

  # Translate from letters to bit indexes for all valve IDs.
  # This makes the math below faster. O(log n) -> O(1)
  valve_ids = {'AA': 1}
  valve_id = 2
  for valve_name in raw_data.keys():
    if valve_name not in valve_ids:
      valve_ids[valve_name] = valve_id
      valve_id*=2

  # Now rename all the valves
  result = dict()
  for valve_name in raw_data:
    tunnels = tuple(valve_ids[v] for v in raw_data[valve_name][1])
    result[valve_ids[valve_name]] = (raw_data[valve_name][0], tunnels)

  #pprint.pprint(result)
  return result


def bfs(paths, data, start):
  #print("BFS for ",start)
  # Direct adjacencies
  pending = [(valve, 1) for valve in data[start][1]]
  visited = set()
  visited.add(start)
  while pending:
    #print("Pending",pending)
    valve, cost = pending.pop(0)
    if valve in visited:
      #print("Skipping",valve)
      continue
    visited.add(valve)

    paths[start][valve] = cost
    for valve2 in data[valve][1]:
      pending.append((valve2,cost+1))
   

def build_shortest_paths(data):
  paths = dict()
  for valve in data.keys():
    paths[valve] = dict()
    paths[valve][valve] = 0
  for valve in data.keys():
    bfs(paths, data, valve)

  return paths


def explore(data, paths, opened_bitmap, nonzero_flows, location, time_left, memoized, visited, pressure):
  visited[0] += 1
  if visited[0] % 100000 == 0:
    print(f"Visited so far: {visited}")

  for neighbor in nonzero_flows:
    # This has to be BEFORE the recursion otherwise the results include the value of some arbitrary other set of valves being opened during the recursion which isn't marked in the index. That implies we can't sum up values in the memoized dictionary because we don't actually know which valves are being calculated as 'open' in a given entry. By doing the math here only on the "top half" of the recursion, we can freely compare between values for part2.
    if pressure > memoized.get(opened_bitmap, 0):
      memoized[opened_bitmap] = pressure

    remaining_time = time_left - paths[location][neighbor] - 1
    if (neighbor & opened_bitmap) or remaining_time <= 0:
      continue

    explore(data, paths, opened_bitmap|neighbor, nonzero_flows, neighbor, remaining_time, memoized, visited, pressure + (data[neighbor][0] * remaining_time))


def part2(paths, data):
  nonzero_flows = set([x for x in data.keys() if data[x][0]>0])
  #print("Neighbor list: ",len(nonzero_flows))

  visited = [0]
  memoized = dict()
  explore(data, paths, 0, nonzero_flows, location=1, time_left=26, memoized=memoized, visited=visited, pressure=0)
  print(f"Memoized: {len(memoized)}, Visited: {visited}")
  print("Best in 26 seconds:", max(memoized.values()))

  best = dict()
  for opened1 in memoized:
    for opened2 in memoized:
      if opened1 & opened2:
        continue
      assert opened1 != 0
      assert opened2 != 0

      both = opened1 | opened2
      best[both] = max(best.get(both, 0), memoized[opened1] + memoized[opened2])

  pressure = max(best.values())
  print(f"Part2: Relieved {pressure} pressure")

#TODO  part2     = max(v1+v2 for bitm1, v1 in visited2.items()
#TODO                  for bitm2, v2 in visited2.items() if not bitm1 & bitm2)
#TODO  print("Part 2", part2)

def mymain(filename):
  data = parse(aoc.lines(filename))
  paths = build_shortest_paths(data)

  print("Part 2")
  part2(paths, data)

aoc.run(mymain)
