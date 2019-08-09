
l1 = [1,2,3,1,2,3]
l2 = set (l1)
print(l2)
l2 = list(set (l1))
print(l2)


##

employees = ['Cohan', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']
gym_members = ['April', 'John', 'Cohan']
developers = ['Judy', 'Cohan', 'Steven', 'Jane' , 'April']

result_1 = set(gym_members).intersection(developers)
print ( f'Type of \'result_1\' : {type(result_1)}')
print (result_1)

result_2 = set(employees).difference(gym_members, developers)
print ( f'Type of \'result_2\' : {type(result_2)}')
print (result_2)


if 'Cohan' in developers:
    print ('found!')
    
# Big_O(n) for list
# Big_o(1) for a set
