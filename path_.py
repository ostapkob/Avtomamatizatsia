# https://pythonworld.ru/moduli/modul-os-path.html

import os
# os.chdir('C:\Windows\System')
print(os.path.join('C', 'dfir', 'ppp'))
# os.makedirs('Y:\\Остапченко\\python\\Avtomamatizatsia\\dir')
print(os.path.abspath('.')) # C:\YandexDisk\python\Avtomamatizatsia
print(os.path.isabs('.'))  # False
print(os.path.isabs(os.path.abspath('.')))  # True
os.path.relpath('C:/Windows', 'C://')
print(os.getcwd())  # C:\YandexDisk\python\Avtomamatizatsia

calc = 'C:/Windows/System32/calc.exe'
print(os.getcwd().split(os.path.sep))  # ['C:', 'YandexDisk', 'python', 'Avtomamatizatsia']
print(os.path.getsize(calc))  # 27648
print(os.path.dirname(calc))  # C:\Windows\System32
print(os.path.basename(calc))  # calc.exe
print(os.path.isfile(calc))  # True

print(os.path.normpath(calc), '-------')# возвращает True, если path указывает на существующий путь или дескриптор открытого файла.
print(os.path.exists('Y:\\')) # False
