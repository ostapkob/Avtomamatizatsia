import os
import zipfile
import send2trash
path = 'D:\YandexDisk'
for fn, sf, fln in os.walk(path):
    print('===========',fn, '============')
    sp = '∟' * (len(fn.split(os.path.sep))-1)
    for s in sf:
        print(sp, 'Folder== ', s)
    for f in fln:

        print(sp, 'File :', f)
new = zipfile.ZipFile(path+'\coin.zip', 'w')
new.write(path+'\coin.xlsx', compress_type=zipfile.ZIP_DEFLATED)
new.close()

send2trash.send2trash('D:\\test.txt')
