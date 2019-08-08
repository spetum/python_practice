

names = [ 'Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = [ 'Spiderman', 'Superman', 'Deadpool', 'Batman']

identities = zip (names, heroes)

print (type(identities))
print (identities)
## Python 2와 Python 3의 실행결과가 다르다.
## Python 2에서는
##'''
##[('Peter Parker', 'Spiderman'), ('Clark Kent', 'Superman'),
##('Wade Wilson', 'Deadpool'), ('Bruce Wayne', 'Batman')]
##'''
## python 3에서는
## <zip object at 0x000001FA3473DE48> 같은 형식으로 출력된다.


print (list(identities))
## 위에 list(identities)를 하게 되면 아래의 identities는 남는 것이 없게 된다.

for identity in identities:
    print('{} is actually {}!'.format(identity[0], identity[1])) 


## 이런 경우를 막기 위해

identity_list = list(zip(names, heroes))
print (type(identity_list))
print (identity_list)

for identity in identity_list:
    print('ID:{} is actually {}!'.format(identity[0], identity[1])) 
