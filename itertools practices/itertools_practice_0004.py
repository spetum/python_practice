
## https://www.youtube.com/watch?v=Qu3dThVy6KQ
## Python Tutorial: Itertools Module - Iterator Functions for Efficient Looping
## Author: Corey Schafer
## Publish Date: 2018. 11. 13

import itertools


letters = [ 'a', 'b', 'c', 'd']
numbers = [ 0, 1, 2, 3 ]
names = ['Cohan' , 'Niclaus']

selectors = [True, True, False, True]

result_1 = itertools.compress(letters, selectors)
## result_1 ==> a , b , d

for item in result_1:
    print(item)

