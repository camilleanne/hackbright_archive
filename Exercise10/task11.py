#!/bin/env python

"""
Write a function with the following signature:
    title(str) -> str

It should take a string and capitalize it according to book title rules
    eg:
    title("a tale of two cities")
        => A Tale of Two Cities
"""
#lots of loops version
def title(my_title):
	words = my_title.split()
	lower_words = ['of', 'at', 'the', 'for', 'is', 'a']
	cap_title = []
	for i in range(len(words)):
		if i == 0:
			cap_title.append(words[0].capitalize())
		elif words[i] in lower_words:
			cap_title.append(words[i])
		else:
			cap_title.append(words[i].capitalize())
	return " ".join(cap_title)

#list comprehension version
def title2(string):
	lower_words = ['of', 'at', 'the', 'for', 'is', 'a']
	my_title = [word.capitalize() if word not in lower_words else word for word in string.split()]
	my_title[0] = my_title[0].capitalize()
	return " ".join(my_title)


print title3("a tale of two cities")