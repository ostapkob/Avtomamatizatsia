def print_lists(list_of_list, round_digit=2):
	mm = 0
	for i in list_of_list:
		mm= max(mm, len(i))
	maxl = [0]*mm
	for i in list_of_list:
		for n, j in enumerate(i):
			if type(j) == int or type(j) == float:
				j = round(j, round_digit)	
			maxl[n] = max(maxl[n], len(str(j)))

	for i in list_of_list:
		for n,j in enumerate(i):
			if type(j) == int or type(j) == float:
				j = round(j, round_digit)	
			print(str(j).ljust(maxl[n]), end=' | ')
		print()	

