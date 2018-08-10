from music21 import *
import numpy as np

elements = 129
durations = 5
all_elem = elements*durations

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
    new_note = None
    if (song[i] % elements == elements-1):
      new_note = note.Rest()
    else:
      new_note = note.Note()
      new_note.pitch.midi = song[i] % elements

    new_note.quarterLength = get_dur(int(song[i] / elements))
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
bundle = corpus.search(1, 'numberOfParts')

mat2 = np.zeros((all_elem, all_elem, all_elem*all_elem))
my_notes = None

count = 0
stop = 50
for corp_song in bundle:
  orig = corp_song.parse()
  count += 1

  if (count == stop):
    print("trained on ",stop," songs")
    break
  #print(count,": ",orig.metadata.title)

  # flatten stream
  song_notes = orig.flat.notesAndRests

  # initialize and fill in frequency matrix ********* fix this to fill in matrix of 640^2 instead of 640
  my_notes = []
  for n in song_notes:
    if (isinstance(n, note.Note)):
      my_notes.append(elements*get_ql(n) + n.pitch.midi)
    elif (isinstance(n, chord.Chord)):
      if (len(n.pitches) == 0):
        my_notes.append(elements*get_ql(n.duration) + elements-1)
        continue
      new_note = note.Note()
      new_note.pitch = n.pitches[0]
      my_notes.append(elements*get_ql(n.duration) + new_note.pitch.midi)
    elif (isinstance(n, note.Rest)):
      my_notes.append(elements*get_ql(n.duration) + elements-1)
    else:
      print("My error: ",type(n))

  for i in range (2, len(my_notes) - 1):
    mat2[my_notes[i-2]][my_notes[i-1]][my_notes[i]*all_elem + my_notes[i+1]] += 1

# set first note(s) in generated song to first note in original song
song2 = [my_notes[0], my_notes[1]]

# generate song
for i in range (1, len(my_notes)):
  rand_num = np.random.randint(0,100)
  next_notes = mat2[song2[i-1]][song2[i]]
  double_note = get_note(rand_num, next_notes)
  if double_note is None:
    continue
  song2.append(int(double_note/all_elem))
  song2.append(double_note % all_elem)

# convert list to stream
stream2 = to_stream(song2)


# orig.show()
# orig.write('midi', fp='orig_song_2.mid')
# stream1.show('midi')
stream2.show()
# stream2.write('midi', fp='gen2_song_2.mid')
