import time, datetime

def long_f(a, b):
    for c in range(1, b):
        a = a*a 
    return a    


start = time.time()
startD = datetime.datetime.now()
dt = datetime.timedelta(days = 21)
print(dt*10)

print(startD.strftime('%Y %B %d %H:%M:%S %p'))
print(datetime.datetime.strptime('Oct of 3 in 2018', '%b of %d in %Y'))


a = 17
stop = 19
i=0
ex = False
while i < stop:
    try:
        i+=1
        print(i, time.time() - start)
        a = long_f(a, 4)
        if time.time() - start > 1:
            # print()
            ans = input('Do You wont stop program ')
            if ans == 'y':
                ex = KeyboardInterrupt
    except KeyboardInterrupt:
        print('\nDone.')
        break
print(i, ex)