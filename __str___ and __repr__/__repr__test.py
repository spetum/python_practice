class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
        
    def __str__ (self):
        return f'Color of car is {self.color} and has {self.mileage} miles.'.format(slef=self)

    def __repr__ (self):
        return '__repr__ for car'

if __name__ == '__main__' :
    my_car = Car('red', 3213)
    print(my_car)
    # in shell just      >>> my_car    .
    # output is          __repr__ for car 
    
