
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current



nums = MyRange (1 , 10)
##for num in nums:
##    print(num)

print(next(nums))
print(next(nums))
print(next(nums))

def my_range(start, end):
    current  = start
    while current < end:
        yield current
        current += 1

my_nums = my_range(11,20)
##print(next(my_nums))
##print(next(my_nums))
##print(next(my_nums))
print ('my_range(11,20)')
for num in my_nums:
    print(num)
    
