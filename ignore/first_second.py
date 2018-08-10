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
    n.pitch.pitchClass = song[i]
    n.octave = my_notes[0].octave
    n.quarterLength = my_notes[i % len(my_notes)].quarterLength
    ret.append(n)
  return ret

# load in a random monophonic piece from corpus
bundle = corpus.search(1, 'numberOfParts')#[0].parse()

mat1 = np.zeros((12,12))
mat2 = np.zeros((12,12,12))
my_notes = None
for j in range(8):
  orig = bundle[j].parse()
  print("Title: ",orig.metadata.title)

# flatten stream
  my_notes = orig.flat.notes

# initialize and fill in frequency matrix

  mat1[my_notes[0].pitch.pitchClass][my_notes[1].pitch.pitchClass] += 1
  for i in range (2, len(my_notes)):
    mat1[my_notes[i-1].pitch.pitchClass][my_notes[i].pitch.pitchClass] += 1
    mat2[my_notes[i-2].pitch.pitchClass][my_notes[i-1].pitch.pitchClass][my_notes[i].pitch.pitchClass] += 1

#print(mat)

# set first note in generated song to first note in original song
song1 = [my_notes[0].pitch.pitchClass] 
song2 = [my_notes[0].pitch.pitchClass, my_notes[1].pitch.pitchClass]

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
