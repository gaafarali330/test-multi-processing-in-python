import time
import multiprocessing

def number_test(x):
    if x == 0 :
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

    starttime=time.time()
    pool = multiprocessing.Pool()
    pool.map(multiprocessing_test_fun,range(sRange,eRange))
    pool.close()

    print('the task take {} seconds '.format(time.time() - starttime))
