nums = [1, 2, 3]

##for num in nums:
##    print(num)


# print(dir(nums)) # nums가 갖고 있는 속성과 기존 내장 메소드 확인
####['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
####'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
####'__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
####'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
####'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
####'__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
####'__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index',
####'insert', 'pop', 'remove', 'reverse', 'sort']



##print (next(nums))
####Traceback (most recent call last):
####  File "<pyshell#3>", line 1, in <module>
####    print (next(nums))
####TypeError: 'list' object is not an iterator

i_nums = nums.__iter__() 

##print(dir(i_nums)) # i_nums가 갖고 있는 속성과 기존 내장 메소드 확인
#### ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
#### '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
####'__init_subclass__', '__iter__', '__le__', '__length_hint__',
####'__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__',
####'__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__',
####'__subclasshook__']

print (i_nums)
print (i_nums.__next__())
print (next(i_nums))
print (next(i_nums))
##print (next(i_nums)) # i_nums의 원소가 3개뿐인데 다음을 찾으면 당연히 에러 남.
####    print (next(i_nums)) # i_nums의 원소가 3개뿐인데 다음을 찾으면 당연히 에러 남.
####StopIteration

i_nums = nums.__iter__() 
while (True):
    try:
        item = next(i_nums)
        print (item)
    except StopIteration:
        break
    

