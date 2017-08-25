#!/bin/env python

"""
Given the list l composed of tuples, 
sort the list by the second item in the tuple
    l = [(1,3), (3,2), (5,1)]
    becomes
    l = [(5,1), (3,2), (1,3)]
"""
l = [(1,2), (3,1), (17, 35), (3, 40), (81,20)]

#loopy version
temp = []
length = 0

while length < len(l):
	for i in range(len(l)-1):
		if l[i][1] > l[i+1][1]:
			temp = l[i]
			l[i] = l[i+1]
			l[i+1] = temp
	length += 1
print l


#short version
print sorted(l, key=lambda x: x[1])