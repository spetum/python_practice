##from collections import Counter

import random

##a = [0,1,1,1,2,3,7,7,23]

def count_element(seq) -> dict:
    hist = {}
    for i in seq:
        hist[i] = hist.get(i,0) + 1
    return hist

##counted = count_element(a)
##print(counted)

##recounted = Counter(a)
##print(recounted)
##
##print(recounted.items() == counted.items())

def ascii_histogram(seq) -> None:
    counted = count_element(seq)
    for k in sorted(counted):
##        print(f'{k} {"*" * counted[k]}')
        print(f'\'{k}\': {"*" * counted[k]} \t({counted[k]})')
random.seed(1)
vals = [1, 3, 4, 6, 8, 9, 10]
freq = [random.randint(5,15) for _ in vals]

data = []
for f, v in zip (freq, vals):
    data.extend([v]*f)

ascii_histogram(data)

