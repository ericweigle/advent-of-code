#!/usr/bin/python3

def turn_result(numbers, max_turns):
  state =[None]+numbers
   
  # init 
  number_to_turn = dict()
  turn_numbers = [None]
  next_to_say = None

  # cycle
  for turn in range(1,max_turns+1):
    if turn < len(state):
      number = state[turn]
    elif next_to_say is not None:
      number = next_to_say
    else:
      number = 0

    turn_numbers.append(number)
    if number in number_to_turn:
      next_to_say = turn - number_to_turn[number]
    else:
      next_to_say = None
    number_to_turn[number] = turn
  return turn_numbers[-1]

assert turn_result([0,3,6], 2020) == 436
assert turn_result([1,3,2], 2020) == 1
assert turn_result([2,1,3], 2020) == 10
assert turn_result([1,2,3], 2020) == 27
assert turn_result([2,3,1], 2020) == 78
assert turn_result([3,2,1], 2020) == 438
assert turn_result([3,1,2], 2020) == 1836
print(turn_result([8,13,1,0,18,9],2020))     #755
print(turn_result([8,13,1,0,18,9],30000000))  #11962
