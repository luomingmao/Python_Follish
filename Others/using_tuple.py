#!/usr/bin/python
#File name: using_tuple.py

zoo = ('wolf', 'elphant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = ('monky', 'dolphin', zoo)
print('Number of animals in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brougth from old zoo is', new_zoo[2][2])