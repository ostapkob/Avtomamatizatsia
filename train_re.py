import re


# rr = re.compile(r'\d{3}-\d{3}-\d{4}')
rr = re.compile(r'\s\d{3}\.\d')
rr = re.compile(r'>\w+<')


with open('myfile.txt') as f:
	for line in f:
		# print(line)
		pat = rr.search(line)
		if pat:
			print(pat.group())#, line)



