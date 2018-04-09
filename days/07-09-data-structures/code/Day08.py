# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 08:31:24 2018

@author: Galen Miller
"""
import re

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    return ", ".join(cars['Jeep'] )


l = []
for k in cars:
    l.append(cars[k][0])
def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    l = []
    for k in cars:
        l.append(cars[k][0])
    return l 

l = []
for k in cars.keys():
    for v in range(len(cars[k])):
        if re.search('trail', cars[k][v], re.IGNORECASE) != None:
            l.append(cars[k][v])
        #print(re.search('trail', cars['Jeep'][v], re.IGNORECASE).group())
def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    l = []
    for k in cars.keys():
        for v in range(len(cars[k])):
            if re.search(grep, cars[k][v], re.IGNORECASE) != None:
                l.append(cars[k][v])
    l.sort()
    return l


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    for k in cars.keys():
        cars[k].sort()
    return cars
