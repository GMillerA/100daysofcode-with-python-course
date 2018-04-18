# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Importing the libraries
from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

#####First List Comprehension
###Output each name with title case and reverse first and last name
new_names = [name.title() for name in NAMES]

def reverse_name(name):
    first, last = name.split()
    n = ''.join([last, " ", first])
    return n

new_names2 = [reverse_name(name) for name in new_names]

####Generator
def gen_pairs(l):
    for i in range(10):
        yield print('{} teams up with {}!'.format(l[i], l[i+1]))

    
pairs = gen_pairs(new_names)
        
for _ in range(10):
    next(pairs)
    

def gen_pairs():
    # again a list comprehension is great here to get the first names
    # and title case them in just 1 line of code (this comment took 2)
    first_names = [name.split()[0].title() for name in NAMES]
    while True:
        
        # added this when I saw Julian teaming up with Julian (always test your code!)
        first, second = None, None
        while first == second: 
            first, second = random.sample(first_names, 2)
        
        yield print('{} teams up with {}'.format(first, second))
        
pairs = gen_pairs()

for _ in range(10):
    next(pairs)
        
        
        