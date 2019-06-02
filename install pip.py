import os
import time
with open('requirement.txt', 'r') as f:
    for line in f:
        mod = line.split('==')[0]
        print('instal mod: ', mod)
        os.system('pip install '+mod)