# Decorators in kwargs

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper executed this before \'{}\''.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print ('display function ran')

# @decorator_function
# def display():
# 이렇게 한 거는 display = decorator_function(display) 한 것과 동일하다.

display()

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 24) 
