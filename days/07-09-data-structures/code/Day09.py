# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 07:45:46 2018

@author: Galen Miller
"""
#Github Data
url = 'https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/07-09-data-structures/code/data.py'

#Print out 10th item in each 
print('Here is 10th item in list: {}'.format(states_list[10]))
print('\n')
print('Here is 10th item in dicitionary: {}'.format(list(us_state_abbrev.keys())[10]))

#Print out 45th key in dictionary
print('45th key in dictionary: \n')
print('{}'.format(list(us_state_abbrev.keys())[45]))

#Print out 27th value in dictionary
print('27th value in dictionary: \n')
print('{}'.format(us_state_abbrev[list(us_state_abbrev.keys())[27]]))

#Replace 15th key in dictionary with 28th item in list
print('15th key in dictionary: {}'.format(list(us_state_abbrev.keys())[15]))

print('28th item in list: {}'.format(states_list[28]))

print('Replace 15th key in dictionary with 28th item in list \n')

#d['test2'] = d.pop('test')
us_state_abbrev[states_list[28]] = us_state_abbrev.pop('{}'.format(list(us_state_abbrev.keys())[15]))

print('New key is: {}'.format(list(us_state_abbrev.keys())[15]))
