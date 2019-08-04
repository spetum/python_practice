# Practical Examples


from functools import wraps
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.3.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args,kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer (orig_func):
    import time

    @wraps(orig_func)
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

# wrapper.*.log가 출력되는지 이해가 될지도.
# 어떤 순서로 해도 wrapper가 아닌 원래 호출한 함수를 출력하기 위해
# 소스에서 from functools import wraps 를 이용한다.
# display_info = my_timer(display_info)
# print(display_info.__name__)

## decorator 하는 순서에 따라 영향을 받지 않으려면 다음과 같이 해보자.
#display_info = my_logger(my_timer(display_info))

# display_info('John', 25)
# display_info('Hank', 33)
# display_info('Juan', 21)
display_info('Tom', 22)
# display()
