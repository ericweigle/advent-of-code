#!/usr/bin/python3

import os

def yield_frames():
  #    0-1345 pipe finding
  for in_frame in range(0, 1345, 18):
    yield in_frame
  # 1346-1897 background
  for in_frame in range(1346, 1897, 7):
    yield in_frame
  # 1898-5604 flood fill
  for in_frame in range(1898, 5604, 49):
    yield in_frame
  # 5605-5642 insideness
  for in_frame in range(5605, 5643, 1):
    yield in_frame

out_frame = 0
for in_frame in yield_frames():
  infile = "/mnt/sda1/space/frames/orig/frame_%04d.png" % in_frame
  outfile = "/mnt/sda1/space/frames/frame_%04d.png" % out_frame
  os.system(f"cp {infile} {outfile}")
  out_frame += 1
for i in range(30):
  infile = "/mnt/sda1/space/frames/orig/frame_5642.png"
  outfile = "/mnt/sda1/space/frames/frame_%04d.png" % out_frame
  os.system(f"cp {infile} {outfile}")
  out_frame += 1

# ffmpeg -framerate 30 -i frames/frame_%04d.png out-fast.gif
