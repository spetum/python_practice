
## https://www.youtube.com/watch?v=Qu3dThVy6KQ
## Python Tutorial: Itertools Module - Iterator Functions for Efficient Looping
## Author: Corey Schafer
## Publish Date: 2018. 11. 13

## https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Itertools/snippets.txt


## itertools.tee(.. .. ..)로 변경하는 예제일뿐.
## itertools.tee는 unix명령어와 비슷하게 특정 스트림의 영향을 받는 것으로 예상만 한다.

import itertools


letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

def get_state(person):
    return person['state']

def get_city(person):
    return person['city']


person_group_1 = itertools.groupby(people, get_state)
person_group_2 = itertools.groupby(people, get_city)

##person_group_1_1, person_group_1_2, person_group_1_3 = itertools.tee(person_group_1)
# 세개는 안됨.

person_group_1_0, person_group_1_1 = itertools.tee(person_group_1)
person_group_1_2, person_group_1_3 = itertools.tee(person_group_1_0)


person_group_2_0, person_group_2_1 = itertools.tee(person_group_2)
person_group_2_2, person_group_2_3 = itertools.tee(person_group_2_0)

print('itertools.groupby(people, get_state) :(1)')
for item in person_group_1_0:
    print(item)

print('itertools.groupby(people, get_city) :(1)')
for item in person_group_2_0:
    print(item)


print('itertools.groupby(people, get_state) :(2)')
for key, group in person_group_1_1:
    print (key)
    for person in group:
        print (person)
##    print()

print('itertools.groupby(people, get_city) :(2)')
for key, group in person_group_2_1:
    print (key)
    for person in group:
        print (person)    
##    print()


print('itertools.groupby(people, get_state) :(3)')
for key, group in person_group_1_3: ## 전체 실행할 때 person_group_1_2로 하면 결과가 안나옴.
    print (key, len(list(group)))
##    for person in group:
##        print (person)    

print('itertools.groupby(people, get_city) :(3)')
for key, group in person_group_2_3: ## 전체 실행할 때 person_group_2_2로 하면 결과가 안나옴.
    print (key, len(list(group)))
##    for person in group:
##        print (person)    

