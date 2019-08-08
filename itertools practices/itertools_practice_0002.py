
## https://www.youtube.com/watch?v=Qu3dThVy6KQ
## Python Tutorial: Itertools Module - Iterator Functions for Efficient Looping
## Author: Corey Schafer
## Publish Date: 2018. 11. 13

import itertools

letters = [ 'a','b','c','d']
numbers = [0, 1, 2, 3]
names = ['Cohan' , 'Niclaus']

##combined = letters + numbers + names 
##print ( combined )


combined_1 = itertools.chain(letters, numbers, names)

##count = 0
##for item in combined_1:
##    count += 1 
##    print (f"{count} : {item}")


result_2 = itertools.islice(range(10),5) ## 0에서 (1씩 증가하여) 5를 넘지 않는 정수 범

print('itertools.islice(range(10),5) : ')
count = 0
for item in result_2:
    count += 1 
    print (f"{count} : {item}")


print('itertools.islice(range(10),1,5) : ')
result_3 =itertools.islice(range(10),1,5) ## 1에서 (1씩 증가하여) 5를 넘지 않는 정수 범위

count = 0
for item in result_3:
    count += 1 
    print (f"{count} : {item}")


print('itertools.islice(range(10)1,5,2) : ')
result_4 =itertools.islice(range(10),1,5,2) ## 1에서 2씩 증가하여 5를 넘지않는 정수 범위 

count = 0
for item in result_4:
    count += 1 
    print (f"{count} : {item}")

