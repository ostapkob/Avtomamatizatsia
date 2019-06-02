#! Create zip-backup
import os
def backupzip(folder):
	folder = os.path.abspath(folder)
	number = 1
	while True and number < 2:
		zipfile = os.path.basename(folder)+'_'+str(number)+'.zip'
		print(zipfile, os.path.exists(zipfile))
		number += 1

name ='C:\BI\IT\Хирьянов - Алгоритмы'
backupzip(name)

for folder, foldern, filen in os.walk(name):
	print(folder)

	# for fn in foldern:
	# 	print(fn)
	for fn in filen:
		i = round(os.path.getsize(folder+'\\'+fn)/2**20)
		print(fn, ':', i, 'Mb')


