#!/usr/bin/python
#File name: using_dict.py

#'ab' is short for 'a'ddress 'b'ook

ab = {	'Swarrop'	: 'swaroopch@byteofpython.inf',
		'Larry'		: 'larry@wall.org',
		'Matsumoto'	: 'matz@ruby-lang.org',
		'Spammer'	: 'spammer@hotmail.com'
	}
print('Swarrop\'s address is %s'%ab['Swarrop'])

#Adding a key/value pair
ab['Guido'] = 'guido@python.org'

#Deleting a key/value pair
del ab['Spammer']

print('\nThere are %d contacts in the address-book\n'%len(ab))
for name, address in ab.items():
	print('Contact %s at %s'%(name,address))
	
if 'Guido' in ab: #OR ab.has_key('Guido')
	print('\nGuido\'s address is %s'%ab['Guido'])