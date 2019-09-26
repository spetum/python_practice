
import multiprocessing
import time


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')


if __name__ == '__main__':
    start = time.perf_counter()

    processes = []

    for _ in range (10) :
        # target= 다음에 나오는 함수이름다음에 괄호여부에 따라 결과가 다르다.
        # p = multiprocessing.Process(target=do_something())
        p = multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    for process in processes:
        process.join()
    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')

