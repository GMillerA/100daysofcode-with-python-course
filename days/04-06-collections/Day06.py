# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 12:04:50 2018

@author: Galen Miller
"""

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    names = list(set(NAMES))
    names = [name.title() for name in names]
    return names


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names.sort(key = lambda s: s.split()[1], reverse=True)
    return names


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    return min(names, key= lambda s: s.split()[0]).split()[0]

for name in NAMES:
    NAMES[name].title()