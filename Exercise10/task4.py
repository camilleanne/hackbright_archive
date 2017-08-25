#!/bin/env python

"""
Given the string s, split it into two strings, 
s2 and s3, s2 containing the first 5 letters of the string, 
and s3 containing the remaining letters.

eg:
    s1 = "Hello there"
    s2 = "Hello"
    s3 = " there"

"""

s = "Hi there, my name is Slim"

def splitter(s):
#this solution assumes that the 'first five letters' includes spaces.
	# s2 = s[:5]
	# s3 = s[5:]
	# print s2
	# print s3


# this solution assumes that the 'first five letters' does not include spaces or punctuation
	s2 = ''
	s3 = ''
	index = 0
	letter_count = 0
	while letter_count <= 5:
		if s[index] in [',', '.', '!', '?', ';', ':', '-', '\'', '\"']:
			s2 = s2 + s[index]
		else:
			s2 = s2 + s[index]
			letter_count += 1
		index += 1
	for item in s[len(s2):len(s)]:
		s3 = s3 + item
	
	print s2
	print s3

def main(s):
	splitter(s)

main(s)