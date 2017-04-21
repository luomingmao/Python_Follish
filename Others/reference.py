#!/usr/bin/python
#File name: reference.py

print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist	#my list is just another name of pointing to the same object!

del shoplist[0]

print('shop list is', shoplist)
print('my list is', mylist)
#notice that both shop list and my list both print the same list without
#the 'apple' confirming that they point to the same object.

print('Copy by makeing a full slice')
mylist = shoplist[:]	#make a copy by doing a full slice
del mylist[0]	#remove over first item

print('shop list is', shoplist)
print('my list is', mylist)
#notice that now the two lists are different