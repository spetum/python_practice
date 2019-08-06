## is and ==(identity and Equality)


l1 = [1,2,3,4,5]
l2 = l1
l3 = [1,2,3,4,5]
print (id(l1)) # 2664305731208
print (id(l2)) # 2664305731208
print (id(l3)) # 2664305730440

print(l1 is l2) # True
print(l1 == l2) # True

print(l1 is l3) # False
print(l1 == l3) # True
