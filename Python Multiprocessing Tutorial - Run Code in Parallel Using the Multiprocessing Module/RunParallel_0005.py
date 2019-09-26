
# 이제 multiprocessing 대신 concurrent.futures 를 임포트하자.
# import multiprocessing
import concurrent.futures
import time

## do_something()의 수정
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    # print('Done Sleeping...')
    return 'Done Sleeping...'


if __name__ == '__main__':
    start = time.perf_counter()

    # with concurrent.futures.ProcessPoolExecutor () as executor:
    #     f1 = executor.submit(do_something, 1)
    #     f2 = executor.submit(do_something, 1)
    #     print(f1.result())
    #     print(f2.result())

    ##  ThreadPool 을 이용하는 방법의 실습
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(do_something,1) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')

