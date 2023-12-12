#!/usr/bin/python3

import itertools
import png
import os

class DrawableBoard(object):
  def __init__(self, rows, cols, base_filename, sampling_interval=1):
    self.clear(rows, cols)
    self._save_count = 0
    self._output_count = 0
    self._sampling_interval = sampling_interval
    self._base_filename = base_filename

  def clear(self, rows, cols):
    """initialize white background"""
    self._board = []
    for r in range(rows):
      self._board.extend([[],[],[]])
    for r in range(len(self._board)):
      for c in range(cols):
        self._board[r].extend([(255,255,255),(255,255,255),(255,255,255)])

  def render_char(self, r, c, val, color=(0,0,0)):
    """Renders 'val' with (r,c) in original domain units."""
    r = r*3
    c = c*3
    if val == '|':
      self._board[r+0][c+1] = color
      self._board[r+1][c+1] = color
      self._board[r+2][c+1] = color
    elif val == '-':
      self._board[r+1][c+0] = color
      self._board[r+1][c+1] = color
      self._board[r+1][c+2] = color
    elif val == 'L':
      self._board[r+0][c+1] = color
      self._board[r+1][c+1] = color
      self._board[r+1][c+2] = color
    elif val == 'J':
      self._board[r+0][c+1] = color
      self._board[r+1][c+1] = color
      self._board[r+1][c+0] = color
    elif val == '7':
      self._board[r+1][c+0] = color
      self._board[r+1][c+1] = color
      self._board[r+2][c+1] = color
    elif val == 'F':
      self._board[r+1][c+1] = color
      self._board[r+1][c+2] = color
      self._board[r+2][c+1] = color
    elif val == '.':
      # Ground
      for x in range(r,r+3):
        for y in range(c,c+3):
          self._board[x][y] = (255,255,255)
    elif val == 'S' or val == '#':
      for x in range(r,r+3):
        for y in range(c,c+3):
          self._board[x][y] = color
    else:
      print(f"Not rendering {val}")

  def render_board(self, board, color=(0,0,0)):
    for r in range(len(board)):
      for c in range(len(board[r])):
        self.render_char(r, c, board[r][c], color)

  def save(self):
    # Flatten pixel values into one long list.
    tmp = []
    if self._save_count % self._sampling_interval == 0:
      filename = self._base_filename + ("-%05d" % self._output_count) + ".png"
      if not os.path.isfile(filename):
        for r in range(len(self._board)):
          tmp.append(list(itertools.chain.from_iterable(self._board[r])))
        png.from_array(tmp, 'RGB').save(filename)
      self._output_count += 1
    self._save_count += 1
