from music21 import *
import numpy as np

# load in a random monophonic piece from corpus
orig = corpus.search(1, 'numberOfParts')[0].parse()
print("Title: ",orig.metadata.title)


# flatten stream
my_notes = orig.flat.notes

# initialize and fill in frequency matrix
mat = np.zeros((12,12))
for i in range (1, len(my_notes)):
  mat[my_notes[i-1].pitch.pitchClass][my_notes[i].pitch.pitchClass] += 1

print(mat)

# set first note in generated song to first note in original song
song = [my_notes[0].pitch.pitchClass]

# generate song
for i in range (len(my_notes)):
  rand_num = np.random.randint(0,100)
  next_notes = mat[song[i]]
  sum_freq = 0.0
  for j in range(len(next_notes)):
    sum_freq += next_notes[j]
  num = 0.0
  for j in range(len(next_notes)):
    frac = (next_notes[j]/sum_freq)*100
    num += frac
    if (num > rand_num):
      song.append(j)
      break

#print(song)

# convert list to stream
s = stream.Stream()
for i in range(len(song)):
  n = note.Note()
  n.pitch.pitchClass = song[i]
  n.octave = my_notes[0].octave
  n.quarterLength = my_notes[i % len(my_notes)].quarterLength
  s.append(n)

#orig.show('midi')
#orig.write('midi', fp='orig_song_2.mid')
#s.show('midi')
#s.write('midi', fp='gen_song_2.mid')
