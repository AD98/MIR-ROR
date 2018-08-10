from .shared import *

class Lz:
  def __init__(self, data, rotations=1, sample_len=1, allowed_error=0):
    self.data = data
    self.rotations = rotations
    self.sample_len = sample_len
    self.sample = sample_len > 1
    self.allowed_error = allowed_error
    self.__build_mdict()
    self.__build_cdict()

  def __build_mdict(self):
    m_dict = {}
    max_motif = 0
    temp_data = self.data.copy()

    for i in range(self.rotations):
      motif = []
      for elem in temp_data:
        if (self.sample): #(isinstance(elem),list)
          motif += elem
        else:
          motif.append(elem)
        if (len(motif) > max_motif):
          max_motif = len(motif)
        if (tuple(motif) in m_dict):
          m_dict[tuple(motif)] += 1
        else:
          m_dict[tuple(motif)] = 1
          motif = []

      temp_data = temp_data[self.sample_len:] + temp_data[:self.sample_len]

    self.max_motif = max_motif
    self.m_dict = m_dict

  def __build_cdict(self):
    c_dict = {}
    for k in self.m_dict.keys():
      prefix = k[:len(k) - self.sample_len]
      suffix = list(k[len(k) - self.sample_len:])
      if (prefix == ()):
        continue
      if (prefix in c_dict):
        c_dict[prefix].append([suffix, self.m_dict[k]])
      else:
        c_dict[prefix] = [[suffix, self.m_dict[k]]]
    self.c_dict = self.__normalize(c_dict)

  def __normalize(self, c_dict):
    for v in c_dict.values():
      sum_probs = 0.0
      for elem in v:
        sum_probs += elem[1]
      for elem in v:
        elem[1] = elem[1]/sum_probs
    return c_dict

  def find_key(self, motif):
    if (self.sample):
      return self.__find_key_sample(motif)
    else:
      return self.__find_key_notes(motif)
  
  def __find_key_sample(self, motif):
    print('len(motif)',len(motif))
    for key in self.c_dict.keys():
      print('len(key)',len(key))
      if (len(key) != len(motif)):
        continue
      if (get_error(list(key), motif) < self.allowed_error):
        return key
    return None

  def __find_key_notes(self, context):
    if (tuple(context) in self.c_dict):
      return tuple(context)
    return None

  def gen_motifs(self, cur_song, num_motifs):
    new_song = cur_song.copy()
    for i in range(num_motifs):
      context = get_context(new_song, self.max_motif)
      while (1):
        key = self.find_key(context)
        if (len(context) == 0):
          print(i,'motifs found')
          print('original song:', cur_song)
          print('new song:', new_song)
          return new_song
        elif (key is not None):
          rand_num = np.random.randint(0,100)
          next_notes = get_next_notes(self.c_dict[key])
          to_app = self.c_dict[key][get_note(rand_num, next_notes)][0]
          new_song += to_app
          #else:
           # new_song.append(to_app)
          print('motif found')
          break
        else:
          context = context[self.sample_len:]

    print(num_motifs, 'motifs found')
    print('original song:', cur_song)
    print('new song:', new_song)
    return new_song
