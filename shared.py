import numpy as np

def get_context(my_song, max_motif):
  if (len(my_song) < max_motif):
    return my_song
  else:
    return my_song[len(my_song) - max_motif:]

def get_next_notes(l):
  ret = []
  for elem in l:
    ret.append(elem[1])
  return ret

def get_note(rand_num, next_notes):
  sum_freq = 0.0
  for j in range(len(next_notes)):
    sum_freq += next_notes[j]
  if (sum_freq == 0):
    return None
  num = 0.0
  for j in range(len(next_notes)):
    frac = (next_notes[j]/sum_freq)*100
    num += frac
    if (num > rand_num):
      return j

def get_error(list1, list2):
  ret = 0
  for i in range(len(list1)):
    ret += abs(list1[i] - list2[i])
  return ret
