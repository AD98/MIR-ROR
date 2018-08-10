from scipy.io import wavfile
import numpy as np
from shared import *



def find_key(keys, motif, allowed_error):
  print('len(motif)',len(motif))
  for key in keys:
    print('len(key)',len(key))
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

fs, data = wavfile.read('/Users/anshuldoshi/WINLAB/mir-ror/drake_nfw.wav')
data = get_channel(data.tolist(), 0)

data = data[:1000]

sample_len = 20#fs * 3
allowed_error = 65536 * 0.80 * sample_len

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

#print(c_dict)

for i in range(50):
  #print('my_song',my_song)
  #print('context',context)
  key = find_key(c_dict.keys(), context, allowed_error)
  if (len(context) == 0):
    my_song += data[sample_len*cur_samp : sample_len*(cur_samp + 1)]
    context = get_context(my_song, max_motif)
    cur_samp += 1
    print('no motif')
  elif ((key is not None)): #and (len(key) < max_motif)):#in c_dict):
    rand_num = np.random.randint(0,100)
    #print('key',key)
    next_notes = get_next_notes(c_dict[key])
    to_app = c_dict[key][get_note(rand_num, next_notes)][0]
    my_song += to_app
    context = get_context(my_song, max_motif)
    print('match')
  else:
    context = context[sample_len:]

arr = np.array(my_song, dtype='int32')
print(arr)
wavfile.write('wave_lz.wav', fs, arr)
