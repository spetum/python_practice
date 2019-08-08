
## https://www.youtube.com/watch?v=Qu3dThVy6KQ
## Python Tutorial: Itertools Module - Iterator Functions for Efficient Looping
## Author: Corey Schafer
## Publish Date: 2018. 11. 13

import itertools

letters = [ 'a','b','c','d']
numbers = [0, 1, 2, 3]
names = ['Cohan' , 'Niclaus']

print("permutation: ")
result_1 = itertools.permutations(letters, 2)

count = 0 
##for item in result_1:
##    count += 1
##    print(f"{count}-time: {item}")

print("product: ")
result_2 = itertools.product(numbers, repeat=3)

count = 0 
##for item in result_2:
##    count += 1
##    print(f"{count}-time: {item}")


print("combination: ")
result_3 = itertools.combinations(letters, 2)

count = 0 
##for item in result_3:
##    count += 1
##    print(f"{count}-time: {item}")

 
print("combination_with_replacement: ")
result_3 = itertools.combinations_with_replacement(numbers, 4)

count = 0 
for item in result_3:
    count += 1
    print(f"{count}-time: {item}")

