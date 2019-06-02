#! python3
import os, shutil, send2trash

print(os.getcwd())
if not os.path.isdir('new'):
	os.makedirs('new')
# if not os.path.isdir('new'):
# 	raise ('Noooooo folder')
assert os.path.isdir('new'), 'not folder'
print(os.path.join(os.getcwd(), 'new'))
print(os.path.abspath('.'))
path_ = 'C:\\YandexDisk\\python\\Avtomamatizatsia\\new'
print(os.path.isabs(path_))
path_ = 'new'
print(os.path.isabs(path_))
print(os.path.relpath('C:\\Windows', 'C:\\egg\\spam'))
print(os.path.realpath('C:Windows1/jhvjhv\\22222//lll'))
paint = 'C:\\Windows\\system32\\mspaint.exe'
print(os.path.dirname(paint))
print(os.path.basename(paint))
print(os.path.split(paint))
print(os.sep * 20)
print(os.path.getsize(paint))
print(os.listdir('C:'))
print(os.path.exists('C:\\FUCK'))
shutil.copy(paint, 'new\\mspaint.exe')
shutil.move('new\\mspaint.exe', 'mspaint.exe')
os.unlink('mspaint.exe')  # del file
os.rmdir('new')  # del dir
try:
	shutil.rmtree('xkcd')  # del tree
	send2trash.send2trash('xkcd_T')  # del trash
except:
	pass




