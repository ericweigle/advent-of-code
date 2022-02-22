#!/usr/bin/python3

import collections

import re
import sys
import math
import pprint
import copy
sys.path.insert(1, '/home/eric_weigle_gmail_com/advent-of-code/library/')
import aoc

def alg_to_dict(alg):
  alg = alg.strip()
  assert len(alg) == 512
  d = []
  for i in range(512):
    if alg[i] == '#':
      d.append('1')
    elif alg[i] == '.':
      d.append('0')
    else:
      print("Corrupt")
  assert len(d)==512
  return d

def pad1(img, padding):
  img_size = len(img)
  result = []
  result.append([padding]*(img_size+2))
  for line in img:
    result.append([padding] + line + [padding])
  result.append([padding]*(img_size+2))
  return result


def pad2(img, padding):
  img_size = len(img)
  result = []
  result.append([padding]*(img_size+4))
  result.append([padding]*(img_size+4))
  for line in img:
    result.append([padding]*2 + line + [padding]*2)
  result.append([padding]*(img_size+4))
  result.append([padding]*(img_size+4))
  return result

def pad3(img, padding):
  img_size = len(img)
  result = []
  result.append([padding]*(img_size+6))
  result.append([padding]*(img_size+6))
  result.append([padding]*(img_size+6))
  for line in img:
    result.append([padding]*3 + line + [padding]*3)
  result.append([padding]*(img_size+6))
  result.append([padding]*(img_size+6))
  result.append([padding]*(img_size+6))
  return result


def dump(img):
  for row in img:
    s = ''.join(row)
    print(re.sub("1","#",re.sub("0",".",s)))

def enhance_pix(r, c, img, alg):
  bits = []
  bits.append(img[r-1][c-1])
  bits.append(img[r-1][c])
  bits.append(img[r-1][c+1])
  bits.append(img[r][c-1])
  bits.append(img[r][c])
  bits.append(img[r][c+1])
  bits.append(img[r+1][c-1])
  bits.append(img[r+1][c])
  bits.append(img[r+1][c+1])
  #print(bits)
  bits = int(''.join(bits),2)
  #print(bits)
  return alg[bits]

def blanks(imgsize):
  result = []
  for r in range(imgsize):
    result.append(['0']*imgsize)
  return result

def enhance(img, alg):
  #output = copy.deepcopy(img)
  output = blanks(len(img))
  for r in range(1,len(img)-1):
    for c in range(1,len(img)-1):
      output[r][c] = enhance_pix(r, c, img, alg)
  return output

def img_to_array(img):
  #print('img',img)
  img = re.sub('#','1',img)
  img = re.sub('\.','0',img)
  img = img.splitlines()
  #print('split',img)
  result = []
  for line in img:
    result.append([x for x in line])
  return result

def lit(img):
  count = 0
  for row in img:
    for val in row:
      if val == '1':
        count+=1
  return count

def strip1(img):
  output = []
  for row in img[1:-1]:
    output.append(row[1:-1])
  return output

def mymain(filename):
  alg, img = open(filename, "r").read().split("\n\n")
  alg = alg_to_dict(alg)
  img = img_to_array(img)

  dump(img)
  img = pad3(img, '0')
  print("---- PADDED INPUT--- ---")
  dump(img)

  for enhancements in range(50):
    img = enhance(img,alg)
    img = strip1(img)
    #print("\n\n---- ENHANCE 1 ---")
    #dump(img)

    # For example, it's always 0. For real data, it flip-flops.
    img = pad3(img, '1' if (enhancements%2) == 0 else '0')
    #img = enhance(img,alg)
    #print("\n\n---- ENHANCE 2 ---")
    #dump(img)

  count=lit(img)
  print("\n\nLit:",count)

aoc.run(mymain)
# 5231 -- correct0
# 14279 -- part 2
