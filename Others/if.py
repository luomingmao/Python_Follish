#!/usr/bin/python
#File name: if.py

number = 23
guess = int(input('Enter an integer:'))

if guess == number:
	print ('Congurations, you guessed it.')
	print ('But you do not win any prizes!')
elif guess < number:
	print ('No, it is a litter higher than that')
else:
	print ('No, it is a litter lower than that')
	
print ('Done')