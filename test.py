from lz_class import *

#example of how to use lz class

data = ['a','b','a','b','a','b','c','a','b','d','a','b','c','d','a','b','c','e']
lz = Lz(data, 2)
print(lz.m_dict)
print(lz.c_dict)
cur_song = ['b','a']
new_song = lz.gen_motifs(cur_song, 2)
