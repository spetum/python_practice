
import multiprocessing
import time

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')


##do_something()
##do_something()

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)


if __name__ == '__main__':
    start = time.perf_counter()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')

