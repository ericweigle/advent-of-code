#!/usr/bin/python3

pt1_example = (
  # time, distance
  (7, 9),
  (15, 40),
  (30, 200),
)

pt1_real = (
  # time, distance
  (62, 553),
  (64, 1010),
  (91, 1473),
  (90, 1074),
)

pt2_example = ((71530, 940200),)
pt2_real = ((62649190, 553101014731074),)

def get_distance(race_time, button_time):
  if button_time >= race_time or button_time <=0:
    return 0
  return button_time * (race_time - button_time)


def part1(data):
  result = 1
  for time, distance in data:
    wins = 0
    for button_time in range(1, time):
      if get_distance(time, button_time) > distance:
        wins += 1
    print(f"Wins {wins}")
    result *= wins
  return result

print("Part 1")
print(f"Example: {part1(pt1_example)}")
print(f"Real: {part1(pt1_real)}")

print("Part 2")
print(f"Example: {part1(pt2_example)}")
print(f"Real: {part1(pt2_real)}")
