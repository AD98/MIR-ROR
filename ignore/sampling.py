from scipy.io import wavfile
import numpy as np

def get_context(my_song, max_motif):
  if (len(my_song) < max_motif):
    return my_song
  else:
    return my_song[len(my_song) - max_motif:]

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

def find_key(keys, motif, allowed_error):
  found = False
  for key in m_dict.keys():
    if (len(key) != len(motif)):
      continue
    if (get_error(list(key), motif) < allowed_error):
      return key
  return None

def get_channel(to_flatten, channel):
  ret = []
  for i in range(len(to_flatten)):
    ret.append(to_flatten[i][channel])
  return ret

def get_next_notes(l):
  ret = []
  for elem in l:
    ret.append(elem[1])
  return ret

fs, data = wavfile.read('/Users/anshuldoshi/Downloads/drake_nfw.wav')
data = get_channel(data.tolist(), 0)

sample_len = fs * 3
allowed_error = 65536 * 0.05 * sample_len

m_dict = {}
motif = []
max_motif = 0

print("Starting")

for x in range(int(len(data)/sample_len)):
  sample = data[x*sample_len : (x+1)*sample_len]
  motif += sample
  if (len(motif) > max_motif):
    max_motif = len(motif)
  
  key = find_key(m_dict.keys(), motif, allowed_error)
  if (key == None):
    m_dict[tuple(motif)] = 1
    motif = []
  else:
    m_dict[key] += 1

print('Motif dictionary complete')

c_dict = {}
for key in m_dict.keys():
  prefix = key[:len(key) - sample_len]
  suffix = key[len(key) - sample_len:]
  if (prefix == ()):
    continue
  if (prefix in c_dict):
    c_dict[prefix].append([suffix, m_dict[key]])
  else:
    c_dict[prefix] = [[suffix, m_dict[key]]]

print('Continuation dictionary complete')

for v in c_dict.values():
  sum_probs = 0.0
  for elem in v:
    sum_probs += elem[1]
  for elem in v:
    elem[1] = elem[1]/sum_probs

print('Normalization complete')

cur_samp = 0
context = []
my_song = []

for i in range(50):
  if (len(context) == 0):
    my_song += data[sample_len*cur_samp : sample_len*(cur_samp + 1)]
    context = get_context(my_song, max_motif)
    cur_samp += 1
    print('no motif')
  elif (find_key(c_dict.keys(), context, allowed_error) != None):
    rand_num = np.random.randint(0,100)
    key = find_key(c_dict.keys(), context, allowed_error)
    next_notes = get_next_notes(c_dict[key])
    to_app = c_dict[key][get_note(rand_num, next_notes)][0]
    my_song.append(to_app)
    context = get_context(my_song, max_motif)
  else:
    context = context[sample_len:]

wavfile.write('wave_lz.wav', fs, np.array(my_song))
