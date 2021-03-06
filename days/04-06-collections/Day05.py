# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 09:14:48 2018

@author: Galen Miller
"""

from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'
urlretrieve(movie_data, movies_csv)

Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director(data=movies_csv):
    """Extracts all movies from csv and stores them in a dictionary
       where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


directors = get_movies_by_director()
directors['Christopher Nolan']
total = 0
for m in directors['Christopher Nolan']:
    #cnt = Counter()
    total += m.score 
print(float(total / len(directors['Christopher Nolan'])))
    
def average_director(director):
    total = 0
    for m in directors[director]:
        total += m.score
    if len(directors[director]) == 0:
        return 0
    else:
        return float(total / len(directors[director]))

test_dict = { name : average_director(name) for name in list(directors) }
    
def get_average_scores(directors):
    '''Filter directors with > MIN_MOVIES and calculate averge score'''
    filtered_dict = {d:m for (d,m) in directors.items() if len(m) > MIN_MOVIES}
    avg_dict = { name : average_director(name) for name in list(filtered_dict) }
    return avg_dict
        
        
        
    #avg_score = float(sum(filtered_dict.score())) / len()
    #return (avg_score)


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    pass


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)