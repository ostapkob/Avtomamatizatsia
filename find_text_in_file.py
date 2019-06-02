import os

# name = 'C:\\YandexDisk\\python\\Avtomamatizatsia\\' # Dont chenge DISK
# name = 'C:\\YandexDisk\\Книги\\automate_online-materials\\'
# name = 'C:\\YandexDisk\\python\\'
name = 'Z:\\Диспетчерская порта\\Остапченко\\python\\Avtomamatizatsia\\'
print(os.path.isdir(name))
fnd = 'for'
for folder, folder_name, file_name in os.walk(name):
    for fn in file_name:
        if fn[-2:] == 'py' and fn != 'find_text_in_file.py':
            try:
                path_f = os.path.join(folder, fn)
                with open(path_f, 'r') as f:
                    for line in f:
                        if line.find(fnd) > 0 and len(folder.split('\\'))<12:
                            print(folder)
                            print(fn, '|', line)
                            break # только первая найденная строчка
            except:
                continue
# input()
