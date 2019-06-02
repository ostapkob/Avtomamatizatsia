import os 
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zop', 'Tom', 'Simon']
cats.append('You')
shelfFile['cats'] = cats
shelfFile.close()

