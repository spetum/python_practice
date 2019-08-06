## https://github.com/CoreyMSchafer/code_snippets/tree/master/Generators

##import mem_profile
import random
import time

import sys

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

## print ('Memory (before): {} MB'.format(mem_profile.memory_useage_resource()))

def people_list(num_people):
    result = []
    for i in range(num_people):        
        person= {
            'id' : i,
            'name' : random.choice(names),
            'major' : random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id' : i,
            'name' : random.choice(names),
            'major' : random.choice(majors)
        }
    yield person


'''
Warning (from warnings module):
  File "D:/myWorks/python/generators/names_and_majors_generators.py", line 31
    t1 = time.clock()
DeprecationWarning: time.clock has been deprecated in Python 3.3 and
will be removed from Python 3.8: use time.perf_counter or time.process_time instead

Warning (from warnings module):
  File "D:/myWorks/python/generators/names_and_majors_generators.py", line 33
    t2 = time.clock()
DeprecationWarning: time.clock has been deprecated in Python 3.3 and
will be removed from Python 3.8: use time.perf_counter or time.process_time instead
'''
##t1 = time.clock()
##people = people_generator(10000000)
##t2 = time.clock()

t1 = time.perf_counter()
people = people_generator(1000000)
t2 = time.perf_counter()

##print 'Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil())
print ('Took {} Seconds'.format(t2-t1))
print (sys.getsizeof(people))

t3 = time.perf_counter()
people_list = people_list(1000000)
t4 = time.perf_counter()

##print 'Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil())
print ('Took {} Seconds'.format(t4-t3))
print (sys.getsizeof(people_list))
