# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 09:02:01 2018

@author: Galen Miller
"""

####Pomodoro Timer
# =============================================================================
# from datetime import datetime
# from datetime import timedelta
# =============================================================================
import time

def pom_timer(work_time = 25):
    counter = work_time
    while True:
        if counter > 0:
            print('{} minutes until break'.format(counter))
            counter = counter - 1
            time.sleep(60)
        else:
            print("Time's Up!")
            break
        
        