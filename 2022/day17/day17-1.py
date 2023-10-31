#!/usr/bin/python3

jets = open("example.txt").readlines()[0].strip()
#jets = open("input.txt").readlines()[0].strip()
jets = [-1 if x=='<' else 1 for x in jets]

ROCKS = (
  #   XXXX
  ((0,0),(0,1),(0,2),(0,3)),

  #   .X.
  #   XXX
  #   .X.
  ((0,1),(1,0),(1,1),(1,2),(2,1)),

  #   ..X
  #   ..X
  #   XXX
  ((0,0),(0,1),(0,2),(1,2),(2,2)),

  #   X
  #   X
  #   X
  #   X
  ((0,0),(1,0),(2,0),(3,0)),

  #   XX
  #   XX
  ((0,0),(0,1),(1,0),(1,1))
)


def get_board_top(board, last_top):
  for r in range(last_top+4, last_top-1,-1):
    for c in range(0,7):
      if (r,c) in board:
        return r+1
  return last_top


def hit_something(rock, board):
  for r, c in rock:
    if (r,c) in board:
      return True
    if c<0 or c>6 or r<0:
      return True
  return False


def translate(rock, r_delta, c_delta, board):
  new_rock = [(r+r_delta,c+c_delta) for r,c in rock]
  if hit_something(new_rock, board):
    return rock
  return new_rock

def complete_rows(board):
  for r in range(4000):
    for c in range(7):
      if (r,c) not in board:
        break
    else:
      print(f"Complete row {r}")

def main():
  board = dict()
  current_board_top = 0
  current_rock_index = 0
  current_jet = 0

  for i in range(2022):
    print(f"Moving rock {i} index {current_rock_index} height {current_board_top}")
    rock = ROCKS[current_rock_index]
    rock = translate(rock, current_board_top+3, 2, board)

    while True:
      #print(f"  initial {rock}")
      # Apply jets and move down
      rock = translate(rock, 0, jets[current_jet], board)
      current_jet = (current_jet+1)%len(jets)
      #print(f"  translated {rock}")
      next_rock = translate(rock, -1, 0, board)
      #print(f"  dropped {next_rock}")

      if rock == next_rock:
        #print("Rock has stopped moving.")
        # Rock has stopped moving.
        for r, c in rock:
          board[(r,c)] = True
        current_board_top = get_board_top(board, current_board_top)
        current_rock_index = (current_rock_index+1)%5
        break
      else:
        rock = next_rock

  print(f"Tower is {current_board_top} units tall.")
  

main()
