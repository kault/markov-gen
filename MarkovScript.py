__author__ = 'kault';

import markov_gen

corpus = open('/Users/kault/Desktop/blog/jeeves.txt');
markov = MarkovGen.Markov(corpus);
print markov.generate_markov_text();