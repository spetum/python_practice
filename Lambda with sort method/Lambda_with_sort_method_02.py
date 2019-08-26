
## https://www.youtube.com/watch?v=goPKxNtuxWo
## by Real Python

## Sorting a list of objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name}: {self.age}'

alex = Person('Alex', 16)
mabel = Person('Mabel', 15)
eddie = Person('Eddie', 12)

p = [alex, mabel, eddie]

print (p)
p.sort(key=lambda x: x.age)
print (p)

p.sort(key=lambda x: x.name)
print (p)
