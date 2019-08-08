
## https://www.youtube.com/watch?v=Qu3dThVy6KQ
## Python Tutorial: Itertools Module - Iterator Functions for Efficient Looping
## Author: Corey Schafer
## Publish Date: 2018. 11. 13

import itertools

with open ('itertools_practice_0003.log', 'r') as f:
    header = itertools.islice(f,3)

    for line in header:
        print(line, end='')
