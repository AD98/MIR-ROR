import numpy as np
from .shared import *

def getFirst(next_notes, num):
    max_idxs = []

    for i in range(num):
        max_val = max(next_notes)
        if (max_val == 0):
            break
        max_idxs.append(next_notes.index(max_val))
        next_notes[max_idxs[-1]] = 0
    
    return max_idxs


class First_markov:
    def __init__(self, data, note_range=128):
        self.data = data
        self.mat = np.zeros((note_range, note_range))
        for i in range(1, len(data)):
            self.mat[data[i-1]][data[i]] += 1
    
    def getBestNotes(self, note, num):
        next_notes = list(self.mat[note]).copy()
        return getFirst(next_notes, num)
    
    def getBestThree(self, note):
        return self.getBestNotes(note, 3)



class Sec_markov:
    def __init__(self, data, note_range=128):
        self.data = data
        self.mat = np.zeros((note_range, note_range, note_range))
        for i in range(2, len(data)):
            self.mat[data[i-2]][data[i-1]][data[i]] += 1

    def getBestNotes(self, notes, num):
        next_notes = list(self.mat[notes[0]][notes[1]]).copy()
        return getFirst(next_notes, num)

    def getBestThree(self, notes):
        return self.getBestNotes(notes, 3)
