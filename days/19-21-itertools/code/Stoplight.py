import itertools
import sys
from time import sleep
import random

def sleep_timer():
    return random.randint(3,7)
def stoplight():
    """Stoplight that cycles through colors"""
    colors = 'Red Green Yellow'.split()
    symbols = itertools.cycle(colors)
    for color in symbols:
        if color == "Red":
            print('STOP! The color is {}!'.format(color))
            sleep(sleep_timer())
        elif color == "Green":
            print('GO! The color is {}'.format(color))
            sleep(sleep_timer())
        else:
            print('SLOW! The color is {}'.format(color))
            sleep(3)


if __name__ == "__main__":
    stoplight()