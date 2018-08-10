from lz_class import *
from markov_class import *
#example of how to use lz class

data = ['a','b','a','b','a','b','c','a','b','d','a','b','c','d','a','b','c','e']
lz = Lz(data, 2)
#print(lz.m_dict)
#print(lz.c_dict)
cur_song = ['b','a']
#new_song = lz.gen_motifs(cur_song, 2)

data1 = [1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,5]
m1 = first_markov(data1, 128)
#print(m1.getBestThree(1))
#print(m1.getBestNotes(1,4))

data2 = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,4,1,2,4,1,2,4,1,2,5,1,2,5,1,2,6]
m2 = sec_markov(data2, 128)
print(m2.getBestThree([1,2]))
print(m2.getBestNotes([1,2],4))

