__author__ = 'kault';

import random

#last two words are current state
#next word depends on last two words only, or on present state only
#next word is randomly chosen from a statistical model of the corpus
 
class Markov(object):
     
    # Initializer 
    def __init__(self, corpus_file):
        self.index = {}
        self.corpus_file = corpus_file
        self.words = self.corpus_split()
        self.word_count = len(self.words)
        self.create_index()
         
    # Reads entire file (i.e. corpus) and splits words
    def corpus_split(self):
        self.corpus_file.seek(0)
        data = self.corpus_file.read()
        return data.split()
             
    # Generates triples from the given data string
    def triples(self):                
        if len(self.words) < 3: return
          
        for i in range(len(self.words) - 2):
            yield (self.words[i], self.words[i + 1], self.words[i + 2])
    
    # Checks if the double is already in the index             
    def create_index(self):
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.index:
                self.index[key].append(w3)
            else:
                self.index[key] = [w3]
                          
    def generate_markov_text(self, size = 25):
        seed = random.randint(0, self.word_count - 3)
        seed_word, next_word = self.words[seed], self.words[seed + 1]
        w1, w2 = seed_word, next_word
        gen_words = []

        for i in xrange(size):
            gen_words.append(w1)
            w1, w2 = w2, random.choice(self.index[(w1, w2)])

        gen_words.append(w2)
        return ' '.join(gen_words)