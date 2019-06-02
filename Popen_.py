import subprocess, time, sys
cal = subprocess.Popen(['C:\\Windows\\system32\\mspaint.exe', 'C:\\YandexDisk\\IMG\\_D_fUvaCOhs.jpg']) #  work in Win and Lin
cal.wait()
n = 0
while n < 10:
	n+=1
	print(cal.poll())
	time.sleep(1)

subprocess.Popen([sys.executable, 'csv_.py']) # sys.executable - path python
subprocess.Popen(['start', 'myFile.txt'], shell=True) #  shell=True


#========COMUNICATE_WITH_PROCES===============
args = ["ping", "www.ya.ru"]
process = subprocess.Popen(args, stdout=subprocess.PIPE)
data = process.communicate()
for line in data:
	print(line)