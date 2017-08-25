#!/bin/env python

"""
Given list l1 and list l2, produce list l3 that contains the contents of both lists, removing duplicates
eg:
    l1 = [1,2,3]
    l2 = [2,3,4]
    
    l3 = [1,2,3,4]
"""
l1 = [1, 3, 4, 6, 8, 10, 20 , 31]
l2 = [93, 2, 23, 20]

def list_smush(l1, l2):
	# the easy 'cheat' way
	# l3 = list(set(l1+l2))		
	l3 = []
	for i1 in l1:
		l3.append(i1)
	for i2 in l2:
		if i2 not in l1:
			l3.append(i2)

	return l3

def main(l1, l2):
	print list_smush(l1, l2)

main(l1, l2)

