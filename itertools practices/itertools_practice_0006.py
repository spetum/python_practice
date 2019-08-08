
## https://www.youtube.com/watch?v=Qu3dThVy6KQ
## Python Tutorial: Itertools Module - Iterator Functions for Efficient Looping
## Author: Corey Schafer
## Publish Date: 2018. 11. 13

import itertools


letters = [ 'a', 'b', 'c', 'd']
numbers = [ 0, 1, 2, 3 ]
names = ['Cohan' , 'Niclaus']

selectors = [True, True, False, True]
numbers_2 = [ 0, 1, 2, 3, 2, 1, 0 ]
numbers_3 = [ 1, 2, 3, 2, 1, 0 ]


result_1 = itertools.accumulate(numbers_2)

print('itertools.accumulate(numbers_2) :')
for item in result_1:
    print (item)
    
import operator

result_2 = itertools.accumulate(numbers_2, operator.mul)

print('itertools.accumulate(numbers_2, operator.mul) :')
for item in result_2:
    print (item)

##numbers_3 = [ 1, 2, 3, 2, 1, 0 ]

result_3 = itertools.accumulate(numbers_3, operator.mul)

print('itertools.accumulate(numbers_3, operator.mul) :')
for item in result_3:
    print (item)
