#!/bin/env python

"""
Given dictionary d, print out the key-value pairs in alphabetical order by key, separated by commas
eg:
a, 1
b, 2
c, 4
d, 6
"""
d = {"q": 5, "m": 3, "z":2, "a": 10}

def sort_dict(d):
	for key, value in sorted(d.iteritems()):
		print key,',', value

def main(d):
	sort_dict(d)

main(d)