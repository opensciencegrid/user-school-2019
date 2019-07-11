#!/bin/env python

"""
Anagramic Squares (Euler problem 98): https://projecteuler.net/problem=98

This script takes a list of space-separated words as arguments and finds
the largest anagramic number, if any
"""

import io
import random
import sys


def usage(args, err_msg):
    '''Print error message and usage instructions'''
    msg = "ERROR: %s\nUsage: %s %s" % (err_msg, sys.argv[0], args)
    sys.exit(msg)


def set_len(iterable):
    '''Return the number of unique elements in an iterable'''
    return len(set(iterable))


# Randomly use up an additional 100MB of memory. Surprise!
if random.randint(0, 1):
    f = io.BytesIO()
    f.write(' '*10**8)

usage_args = '<list of anagrams>'
if len(sys.argv) < 3:
    usage('<list of anagrams>', 'Anagram list must contain at least two words')

words = [x.upper() for x in sys.argv[1:]]
words_len = set([len(x) for x in words])

if len(words_len) != 1:
    usage(usage_args, 'Words must be the same length')

num_digits = words_len.pop()

# construct lits of potential squares
x = 1
sq = x**2
squares = []
sq_digits = len(str(sq))
while sq_digits <= num_digits:
    if sq_digits == num_digits:
        squares.append(sq)
    x += 1
    sq = x**2
    sq_digits = len(str(sq))

ana_squares = set()
idx_word = list(words.pop())
for sq in squares:
    str_sq = list(str(sq))
    if set_len(idx_word) != set_len(str_sq):
        continue  # Letter->number mapping must be unique
    idx = dict(zip(idx_word, str_sq))
    for wrd in words:
        letters = []
        for char in list(wrd):
            letters.append(idx[char])
        indexed_num = int(''.join(letters))

        if indexed_num in squares:
            ana_squares = ana_squares.union(set([sq, indexed_num]))

try:
    print max(ana_squares)
except ValueError:
    sys.stderr.write("Could not find square anagrams for the following words: %s\n" % ', '.join(words))
