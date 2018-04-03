# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 08:45:07 2018

@author: Galen Miller
"""
"""Parse log entries for datetimes and calculate the time
   between two shutdown initializations"""
from datetime import datetime
import os
import urllib.request
from datetime import timedelta
# prep

tempfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', tempfile)

# code
def read_file():
    """Read in tempfile return list of lines"""
    with open(tempfile) as file:
        lines = list([line.strip() for line in file])
    return lines


def convert_to_datetime(line):
    """Given a line extract timestamp and convert to datetime"""
    #line = pd.to_datetime(line.split([1]), infer_datetime_format=True)
    date_line = datetime.strptime(line.split()[1] , '%Y-%m-%dT%H:%M:%S')
    return date_line


def time_between_shutdowns(lines):
    """Extract shutdown init events and calculate timedelta between
       first and last one"""
    shutdown = [line for line in lines if
            'Shutdown' in line]
    last = convert_to_datetime(shutdown[-1])
    first = convert_to_datetime(shutdown[0])
    return last - first