class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
        
    def __str__ (self):
        return f'Color of car is {self.color} and has {self.mileage} miles.'.format(slef=self)
    

if __name__ == '__main__' :
    my_car = Car('red', 3213)
    print(my_car)
