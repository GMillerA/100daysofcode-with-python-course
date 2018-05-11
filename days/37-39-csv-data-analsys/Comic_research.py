import os
import csv
import collections
from typing import List

data = []

Superhero = collections.namedtuple(
    'Superhero',
    'page_id,name,urlslug,ID,ALIGN,EYE,HAIR,SEX,GSM,ALIVE,APPEARANCES,FIRST_APPEARANCE,Year'
)


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'marvel-wikia-data.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record = parse_row(row)
            data.append(record)


def parse_row(row):
    row['page_id'] = int(row['page_id'])
    if row['APPEARANCES'] != '':
        row['APPEARANCES'] = int(row['APPEARANCES'])
    else:
        row['APPEARANCES'] = 0
    if row['Year'] != '':
        row['Year'] = int(row['Year'])
    else:
        row['Year'] = 9999

    superhero = Superhero(
        **row

    )

    return superhero


# def get_align() -> List[Superhero]:
#     #return sorted(data, key=lambda r: -r.actual_max_temp)
#     cnt = collections.Counter()
#     for row in Superhero:
#         cnt['ALIGN'] += 1
#     return cnt


def most_appearances() -> List[Superhero]:
    return sorted(data, key=lambda r: -r.APPEARANCES)

def first_appearances() -> List[Superhero]:
    return sorted(data, key=lambda r: r.Year)