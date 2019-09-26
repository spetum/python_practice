
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

    # processes = []
    #
    # for _ in range (10) :
    #     # target= 다음에 나오는 함수이름다음에 괄호여부에 따라 결과가 다르다.
    #     # p = multiprocessing.Process(target=do_something())
    #     # p = multiprocessing.Process(target=do_something)
    #
    #     # 이제는 매개변수를 전달해줘야 한다.
    #     p = multiprocessing.Process(target=do_something, args=[1.5])
    #     p.start()
    #     processes.append(p)
    #
    # for process in processes:
    #     process.join()

    ##  ThreadPool 을 이용하는 방법의 실습
    with concurrent.futures.ProcessPoolExecutor () as executor:
        f1 = executor.submit(do_something, 1)
        f2 = executor.submit(do_something, 1)
        print(f1.result())
        print(f2.result())

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')

