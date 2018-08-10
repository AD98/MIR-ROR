from music21 import *
import numpy as np
from shared import *

durations = 5
elements = 12
all_elems = durations*elements
qls = [4,2,1,0.5,0.25]

def get_ql(n):
  num = 0
  for i in range(durations):
    num = i
    if (n.quarterLength >= qls[i]):
      return i
  return num

def to_stream(l):
  ret = stream.Stream()
  for elem in l:
    n = note.Note()
    n.pitch.pitchClass = elem % elements
    n.quarterLength = qls[int(elem / elements)]
    ret.append(n)
  return ret

#bundle = corpus.search(1, 'numberOfParts')
bundle = corpus.search('mozart', 'composer')

orig = bundle[0].parse()
m_dict = {}
motif = []
max_motif = 0
count = 0
stop = 10
for corp_song in bundle:
  count += 1
  if (count == stop):
    break

  #orig_notes = corp_song.parse().flat.notes
  orig_notes = corp_song.parse().getElementsByClass('Part')[0].flat.notes

  for n in orig_notes:
    if (isinstance(n, chord.Chord)):
      continue
    motif.append(n.pitch.pitchClass + elements*get_ql(n))
    if (len(motif) > max_motif):
      max_motif = len(motif)

    if (tuple(motif) in m_dict):
      m_dict[tuple(motif)] += 1
    else:
      m_dict[tuple(motif)] = 1
      motif = []

print('Motif dictionary complete')

c_dict = {}
for k in m_dict.keys():
  k_to_search = k[:len(k)-1]
  if (k_to_search == ()):
    continue
  if (k_to_search in c_dict):
    c_dict[k_to_search].append([k[len(k)-1], m_dict[k]])
  else:
    c_dict[k_to_search] = [[k[len(k)-1],m_dict[k]]]

print('Continuation dictionary complete')

# normalize c_dict
for v in c_dict.values():
  sum_probs = 0.0
  for elem in v:
    sum_probs += elem[1]
  for elem in v:
    elem[1] = elem[1]/sum_probs

print('Normalization complete Continuation dictionary: ')

my_notes = [orig_notes[0].pitch.pitchClass + elements*get_ql(orig_notes[0])]
context = []

for i in range(50):
  context.append(my_notes[i])
  while (1):
    if (len(context) == 0):
      my_notes.append(np.random.randint(0,all_elems))
      context = my_notes[len(my_notes)-1:]
      print("rand")
      break
    elif (tuple(context) in c_dict):
      rand_num = np.random.randint(0,100)
      next_notes = get_next_notes(c_dict[tuple(context)])
      to_app = c_dict[tuple(context)][get_note(rand_num, next_notes)][0]
      my_notes.append(to_app)
      context.append(to_app)
      break
    else:
      context = context[1:]


#print('My Notes: ',my_notes)

my_song = to_stream(my_notes)
#my_song.write('midi',fp='lz_song_2.mid')
my_song.show()
