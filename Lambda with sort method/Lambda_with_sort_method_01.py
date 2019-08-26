
## https://www.youtube.com/watch?v=goPKxNtuxWo
## by Real Python

names = ['Alf Zed', 'Mike mo', 'Steve Aardvark', 'James Babe']

names.sort(key=lambda x: x.split()[-1].lower())
print(names)

temp1 = names
temp1.sort(key=lambda x: x.split()[0].lower())

####print(temp1 == names)

input("Press any key to continue...")
people = [ ('steve', 35),('Karen', 28), ( 'Gerald', 58), ('Jo', 72)]
print("Before Sorting")
print(people)

people.sort()

print("After Sorting")
print(people)


print ("After sorting with a second element as a key in Lambda expression")
people.sort(key=lambda x: x[1])
print(people)




