#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
'''8 964-435-46-88
8-984-555-77-33
8(914)356-45-12
8 (924) 365-74-96'''

phoneRe = re.compile(r"""
					([^\d-])  	# не цифра
					(8|\+7)		# 8 или +7
					(-|\(| )?   # и т.д.
					\D?
					(\d{3})
					(-|\)| )?
					\D?
					(\d+)
					\D?
					(\d+)
					\D?
					(\d+) # nnn""", re.VERBOSE)
#phoneRe = re.compile(r"\b\w{3}\b") # 	Слова в точности из трёх букв \b означает границу слова
#phoneRe = re.compile(r"[-+]?\d+") # 	Целое число, например
phoneRe = re.compile(r"([^\d-])(8|\+7)(-|\(| )?\D?(\d{3})(-|\)| )?\D?(\d+)\D?(\d+)\D?(\d+)") # или так

mailRe =  re.compile(r'[a-z.0-9]*@[a-z]*[a-z]')

with open('email_&_tel.txt', 'r') as st: # no access
	for line in st:
		m = mailRe.findall(line)
		print(m if m!=[] else '')
		for groups in phoneRe.findall(line):
			#print(groups)
			a = '8'+groups[3]+ groups[5]+ groups[6]+ groups[7]
			print(f'{a[0]}-{a[1:4]}-{a[4:7]}-{a[7:9]}-{a[9:11]}')


