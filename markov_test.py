from music21 import *
import numpy as np


def get_note(rand_num, next_notes):
  sum_freq = 0.0
  for j in range(len(next_notes)):
    sum_freq += next_notes[j]
  num = 0.0
  for j in range(len(next_notes)):
    frac = (next_notes[j]/sum_freq)*100
    num += frac
    if (num > rand_num):
      return j

def to_stream(song):
  ret = stream.Stream()
  for i in range(len(song)):
    n = note.Note()
    n.pitch.midi = song[i] % 128
    ql = int(song[i] / 128);
    n.quarterLength = get_dur(ql)
    #n.quarterLength = my_notes[i % len(my_notes)].quarterLength
    ret.append(n)
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
bundle = corpus.search(1, 'numberOfParts')#[0].parse()

mat1 = np.zeros((128*5,128*5))
mat2 = np.zeros((128*5,128*5,128*5))
my_notes = None

for j in range(8):
  orig = bundle[j].parse()
  print("Title: ",orig.metadata.title)

  # flatten stream
  my_notes = orig.flat.notes

  # initialize and fill in frequency matrix
  for i in range (1, len(my_notes)):
    ql_0 = get_ql(my_notes[i])
    ql_1 = get_ql(my_notes[i-1])
    mat1[128*ql_1 + my_notes[i-1].pitch.midi][128*ql_0 + my_notes[i].pitch.midi] += 1
    if (i > 1):
      ql_2 = get_ql(my_notes[i-2])
      mat2[128*ql_2 + my_notes[i-2].pitch.midi][128*ql_1 + my_notes[i-1].pitch.midi][128*ql_0 + my_notes[i].pitch.midi] += 1

#print(mat)

# set first note(s) in generated song to first note in original song
song1 = [128*get_ql(my_notes[0]) + my_notes[0].pitch.midi] 
song2 = [128*get_ql(my_notes[0]) + my_notes[0].pitch.midi, 128*get_ql(my_notes[1]) + my_notes[1].pitch.midi]

# generate song
for i in range (len(my_notes)):
  rand_num = np.random.randint(0,100)
  next_notes = mat1[song1[i]]
  song1.append(get_note(rand_num, next_notes))
  if (i > 0):
    next_notes = mat2[song2[i-1]][song2[i]]
    song2.append(get_note(rand_num, next_notes))

#print(song)

# convert list to stream
stream1 = to_stream(song1)
stream2 = to_stream(song2)


#orig.show()
#orig.write('midi', fp='orig_song_2.mid')
stream1.show('midi')
#s.write('midi', fp='gen_song_2.mid')
stream2.show('midi')
