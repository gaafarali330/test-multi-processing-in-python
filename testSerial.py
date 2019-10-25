import time

#check if the number is oddor zero or even number
def number_test(x):
    if x == 0:
        return "zero ."
    elif x % 2 == 0:
        return "even ."
    else:
        return "odd ."

#The range is specified by the user
sRange=int(input("inter start of range : "))
eRange=int(input("inter end of range : "))

#the start time of execution
startime = time.time()
for i in range(sRange,eRange):
    y = i*i
    time.sleep(1)
    #waiting two seconds after the Multiply operation then excute the next raw
    print('{} squared result = {} , is {} '.format(i,y,number_test(y)))

# calculate excuting time (time now - start time)
print('the task take {} seconds '.format(time.time() - startime))