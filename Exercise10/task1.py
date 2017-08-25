#!/bin/env python

"""
Given list l, sort it in reverse order
ie: 10, 9, 8, 7, 6
"""
l = [5,2,1,5,9,10,11]


def reverse_sort(l):
	temp = []
	length = 1
	while length < len(l):	
		for i in range(len(l)-1):
			if l[i] < l[i+1]:
				temp = l[i]
				l[i] = l[i+1]
	 			l[i+1] = temp
		length += 1
 	return l

print reverse_sort(l)