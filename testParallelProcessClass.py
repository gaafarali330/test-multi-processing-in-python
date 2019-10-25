import multiprocessing
import time

def number_test(x):
    if x == 0:
        return 'zero .'
    elif x%2 == 0:
        return 'even .'
    else:
        return 'odd .'

def multiprocessing_test_fun(x):
    y = x*x
    time.sleep(1)
    print('{} squared result = {} , is {} '.format(x,y,number_test(y)))

if __name__ == '__main__':
    sRange = int(input("inter start of range : "))
    eRange = int(input("inter end of range : "))
    startime = time.time()
    processes = []
    for i in range(sRange,eRange):
        p = multiprocessing.Process(target=multiprocessing_test_fun, args=(i,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    print('the task take {} seconds '.format(time.time() - startime))