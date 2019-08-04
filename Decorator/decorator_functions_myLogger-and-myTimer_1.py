# Practical Example


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.1.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args,kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer (orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print ('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


import time

# decorator하는 순서가 바뀌면 호출 순서도 바뀌게 된다.
@my_timer
@my_logger
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))


# display_info('John', 25)
# display_info('Hank', 33)
display_info('Juan', 21)
# display()