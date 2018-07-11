from music21 import *
import numpy as np


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

def to_stream(song):
  ret = stream.Stream()
  for i in range(len(song)):
    new_note = note.Note()
    new_note.pitch.midi = song[i] % 128
    ql = int(song[i] / 128);
    new_note.quarterLength = get_dur(ql)
    ret.append(new_note)
  return ret

def get_ql(n):
  if (n.quarterLength >= 4):
    return 0
  elif (n.quarterLength >= 2):
    return 1
  elif (n.quarterLength >= 1):
    return 2
  elif (n.quarterLength >= 0.5):
    return 3
  return 4

def get_dur(num):
  if (num == 0):
    return 4
  elif (num == 1):
    return 2
  elif (num == 2):
    return 1
  elif (num == 3):
    return 0.5
  return 0.25


# load in a random monophonic piece from corpus
# bundle = corpus.search(1, 'numberOfParts')
#bundle = corpus.search('bach','composer')

mat2 = np.zeros((640, 640, 640*640))
my_notes = None

knaan = converter.parse('/Users/anshuldoshi/Desktop/hbd.mid')
#waka = converter.parse('/Users/anshuldoshi/Desktop/waka_waka.mid')
fourfive = converter.parse('/Users/anshuldoshi/Desktop/twinkle.mid')
#wire = converter.parse('/Users/anshuldoshi/Desktop/wire.mid')
# songs = [knaan, waka, fourfive, wire]
songs = [knaan, fourfive]

#for j in range(8):
 # orig = bundle[j].parse()
  #print("Title: ",orig.metadata.title)
for orig in songs:

  # flatten stream
  my_notes = orig.flat.notes

  # initialize and fill in frequency matrix ********* fix this to fill in matrix of 640^2 instead of 640
  for i in range (1, len(my_notes) - 1):
    if (my_notes[i+1].pitch is None) or (my_notes[i].pitch is None) or (my_notes[i-1].pitch is None) or (my_notes[i-2].pitch is None):
      continue
    ql_neg1 = get_ql(my_notes[i+1])
    ql_0 = get_ql(my_notes[i])
    ql_1 = get_ql(my_notes[i-1])
    ql_2 = get_ql(my_notes[i-2])
    mat2[128*ql_2 + my_notes[i-2].pitch.midi][128*ql_1 + my_notes[i-1].pitch.midi][(128*ql_0 + my_notes[i].pitch.midi)*640 + (128*ql_neg1 + my_notes[i+1].pitch.midi)] += 1

# set first note(s) in generated song to first note in original song
song2 = [128*get_ql(my_notes[0]) + my_notes[0].pitch.midi, 128*get_ql(my_notes[1]) + my_notes[1].pitch.midi]

# generate song
for i in range (1, len(my_notes)):
  rand_num = np.random.randint(0,100)
  next_notes = mat2[song2[i-1]][song2[i]]
  double_note = get_note(rand_num, next_notes)
  if double_note is None:
    continue
  song2.append(int(double_note/640))
  song2.append(double_note % 640)

# convert list to stream
stream2 = to_stream(song2)


# orig.show()
# orig.write('midi', fp='orig_song_2.mid')
# stream1.show('midi')
stream2.show()
# stream2.write('midi', fp='gen2_song_2.mid')
