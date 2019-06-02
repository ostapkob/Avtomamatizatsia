import threading, time
def wekeUp(n):
    time.sleep(n)
    print('Weke up Neo')



print('start')
thObj = threading.Thread(target=wekeUp, args=[2])
thObj.start()

thObj2 = threading.Thread(target=print, args=['aaa', 'bbb', 'ccc'], kwargs={'sep' : " & ", 'end' : '\n\n'})
thObj2.start()
time.sleep(1)

print(print('finish'))
input()


