from music21 import *
import numpy as np

markov_order = 1
elements = 129 # all possible midi notes +1 for rests
durations = 1 # all durations we are considering (whole, half, quarter, eighth, sixteenth)
all_elem = elements*durations
num_parts = 2 # number of parts in the songs (different instruments)
all_possible = np.power(all_elem, num_parts) # all possible states

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

  for i in range(num_parts):
    ret.append(stream.Part())

  for i in range(len(song)):
    num = song[i]
    for j in range(num_parts):
      ret[j].append(to_note(num % all_elements))
      num = int(num/all_elements)
  return ret

def to_note(num):
  if (num % elements == elements-1):
    new_note = note.Rest()
  else:
    new_note = note.Note()
    new_note.pitch.midi = num % elements

  new_note.quarterLength = get_dur(int(num / elements))
  return new_note

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

def note_to_num(song_notes):
  ret = []
  for n in song_notes:
    if (isinstance(n, note.Note)):
      ret.append(elements*get_ql(n) + n.pitch.midi)
    elif (isinstance(n, chord.Chord)):
      if (len(n.pitches) == 0):
        ret.append(elements*get_ql(n.duration) + elements-1)
        continue
      new_note = note.Note()
      new_note.pitch = n.pitches[0]
      ret.append(elements*get_ql(n.duration) + new_note.pitch.midi)
    elif (isinstance(n, note.Rest)):
      ret.append(elements*get_ql(n.duration) + elements-1)
    else:
      print("My error: ",type(n))
  return ret

def merge_parts(my_parts):
  ret = []
  for i in range(len(my_parts[0])):
    to_app = 0
    for j in range(num_parts):
      to_app += np.power(all_elem,j) * my_parts[j][i]
    ret.append(to_app)
  return ret

# load in a random monophonic piece from corpus
bundle = corpus.search(num_parts, 'numberOfParts')

mat2 = np.zeros((all_possible, all_possible, np.power(all_possible, markov_order)))
my_notes = None

count = 0
stop = 50
for corp_song in bundle:
  count += 1
  if (count == stop):
    print("trained on ", stop, " songs")
    break
  #print(count,": ",orig.metadata.title)
  
  orig = corp_song.parse()

  parts = orig.getElementsByClass('Part')
  my_parts = []
  for p in parts:
    my_parts.append(note_to_num(p.flat.notesAndRests))
  
  my_notes = merge_parts(my_parts)

  for i in range (2, len(my_notes) - 1):
    mat2[my_notes[i-2]][my_notes[i-1]][my_notes[i]*all_possible + my_notes[i+1]] += 1 #*****************************

# set first note(s) in generated song to first note in original song
song2 = [my_notes[0], my_notes[1]]

# generate song
for i in range (1, len(my_notes)):
  rand_num = np.random.randint(0,100)
  next_notes = mat2[song2[i-1]][song2[i]]
  double_note = get_note(rand_num, next_notes)
  if double_note is None:
    continue
  song2.append(int(double_note/all_possible))
  song2.append(double_note % all_possible)

# convert list to stream
stream2 = to_stream(song2)


# orig.show()
# orig.write('midi', fp='orig_song_2.mid')
# stream1.show('midi')
stream2.show()
# stream2.write('midi', fp='gen2_song_2.mid')
