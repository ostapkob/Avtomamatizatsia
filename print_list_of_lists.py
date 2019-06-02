import pprint
def print_lists(list_of_list):
	mm = 0
	for i in list_of_list:
		mm= max(mm, len(i))
	print (mm)
	maxl = [0]*mm
	for i in list_of_list:
		for n, j in enumerate(i):
			maxl[n] = max(maxl[n], len(j))

	for i in list_of_list:
		for n,j in enumerate(i):
			print(j.ljust(maxl[n]), end=' | ')
		print()	



td =   [['collections', 'import', 'hhhhhhhhkkkkkkkk','OrderedDict', 'Counter'],
		['def', 'global','variable', 'changed', 'llllrrro'],
		['from', 'contextlib', 'import', 'contextmanager1', 'max'],
		['1', '2', '3', '4', '5', '6', '7iii' ],
		['gfhgggg', 'ggggggggt', 'fghfghf', 'vghjfhfgh']]




print_lists(td)

