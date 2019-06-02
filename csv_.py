import csv
from pprint import pprint
import logging
logging.basicConfig(level=logging.NOTSET) #,filename="sample.log", filemode=”w”, format='%(asctime)s - %(levelname)s - %(message)s')
# NOTSET → DEBUG → INFO → WARNING → ERROR → CRITICAL

#===========READER==============
file = open('example.csv')
fReader = csv.reader(file)
# data = list(fReader)  #загрузить весь файл
# pprint(data)

print('-' * 100)
for row in fReader:
    logging.info(row)
   
#===========WRITER==============
a = 'NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
b = range(10)
c = 'Hellow, world', 'Ostap, Potap'
newCSV = open('newCSV.csv', 'w', newline='') #  ,newline='' вроде как бывают пустые строки без этого
fWriter = csv.writer(newCSV) # delimiter = ',' , lineterminator ='\n\n'
fWriter.writerow(a)
fWriter.writerow(b)
fWriter.writerow(c)
newCSV.close()
print('-'*50)

with open('newCSV.csv', 'r') as f:
    for line in f:
        print(line)
