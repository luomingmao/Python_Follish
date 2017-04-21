#!/usr/bin/python
#File name: continue.py

while True:
	s = input('Enter something:')
	if s == 'quit':
		break
	if len(s) < 3:
		continue
	print('Input is ofsufficient length')