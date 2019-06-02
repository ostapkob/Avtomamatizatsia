import random, pprint, json
def Verify_two_list(a_zip, b_zip):
	a = list(map(lambda x: x[1], a_zip))
	b = list(map(lambda x: x[1], b_zip))
	verify = list(zip(a,b))
	# print(verify)
	for a,b in verify:
		if a==b:
			return False
	return True

mans = ['Bob', 'Oleg', 'Tanya', 'Yulia', 'Alex']
tasks = ['sent', 'write', 'read', 'count', 'paint']
random.shuffle(tasks)

tmp = [('Bob', 'read'), ('Oleg', 'paint'), ('Tanya', 'write'), ('Yulia', 'sent'), ('Alex', 'count')]
tasks_mens = []

ls = list(zip(mans, tasks))
for i in range(1, 6):
	flag = True
	while flag:
		if  Verify_two_list(tmp, ls):
			for man, task in ls:
				tasks_mens.append({'date':i, 'man': man, 'task' : task})

			tmp = ls
			ls = list(zip(mans, tasks))
			flag = False
		else:		
			random.shuffle(tasks)
			ls = list(zip(mans, tasks))

with open('choise.json', 'w') as outfile:
    json.dump(tasks_mens, outfile)

pprint.pprint(tasks_mens)
