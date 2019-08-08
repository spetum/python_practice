
## https://www.youtube.com/watch?v=Qu3dThVy6KQ
## Python Tutorial: Itertools Module - Iterator Functions for Efficient Looping
## Author: Corey Schafer
## Publish Date: 2018. 11. 13

## https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Itertools/snippets.txt

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


####person_group_1 = itertools.groupby(people, get_state)
####
####print('itertools.groupby(people, get_state) :(1)')
####for item in person_group_1:
####    print(item)
####
####
####person_group_2 = itertools.groupby(people, get_city)
####
####print('itertools.groupby(people, get_city) :(1)')
####for item in person_group_2:
####    print(item)

####person_group_1 = itertools.groupby(people, get_state)
####
####print('itertools.groupby(people, get_state) :(2)')
####for key, group in person_group_1:
####    print (key)
####    for person in group:
####        print (person)
####    print()
####
####
####person_group_2 = itertools.groupby(people, get_city)
####
####print('itertools.groupby(people, get_city) :(2)')
####for key, group in person_group_2:
####    print (key)
####    for person in group:
####        print (person)    
####    print()

person_group_1 = itertools.groupby(people, get_state)

print('itertools.groupby(people, get_state) :(3)')
for key, group in person_group_1:
    print (key, len(list(group)))
##    for person in group:
##        print (person)    


person_group_2 = itertools.groupby(people, get_city)

print('itertools.groupby(people, get_city) :(3)')
for key, group in person_group_2:
    print (key, len(list(group)))
##    for person in group:
##        print (person)    

