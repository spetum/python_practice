
## https://www.youtube.com/watch?v=Qu3dThVy6KQ
## Python Tutorial: Itertools Module - Iterator Functions for Efficient Looping
## Author: Corey Schafer
## Publish Date: 2018. 11. 13

import itertools

def lt_2(n):
    if n < 2:
        return True
    return False


letters = [ 'a', 'b', 'c', 'd']
numbers = [ 0, 1, 2, 3 ]
names = ['Cohan' , 'Niclaus']

selectors = [True, True, False, True]

result_1 = filter(lt_2 , numbers)

print('filter :')
for item in result_1:
    print(item)


print('itertools.filterfalse :')
result_2 = itertools.filterfalse(lt_2, numbers)
for item in result_2:
    print(item)

numbers_2 = [ 0, 1, 2, 3, 2, 1, 0 ]


print('itertools.dropwhile :')
result_3 = itertools.dropwhile(lt_2, numbers_2)
## result_3 ==> 2, 3, 2, 1, 0

for item in result_3:
    print(item)


print('itertools.takewhile :')
result_4 = itertools.takewhile(lt_2, numbers_2)
## result_4 ==> 0, 1

for item in result_4:
    print(item)




