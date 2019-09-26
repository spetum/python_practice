
# 이제 multiprocessing 대신 concurrent.futures 를 임포트하자.
# import multiprocessing
import concurrent.futures
import time

## do_something()의 수정
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    ## print('Done Sleeping...')
    #return 'Done Sleeping...'
    return f'Done Sleeping...{seconds}'


if __name__ == '__main__':
    start = time.perf_counter()

    ##  ThreadPool 을 이용하는 방법의 실습
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(do_something,sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')

