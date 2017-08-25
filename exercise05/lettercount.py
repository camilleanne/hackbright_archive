from sys import argv

script, filename = argv

text = open(filename)

def main():
	firstletter = text.read()
	lower_case = firstletter.lower()

	alphabet_count = [0 for i in range(0,26)]

	for char in lower_case:
	    if ord(char) <= 122 and ord(char) >= 97:
	        alphabet_count[ord(char)-97] += 1

	for item in alphabet_count:
		print item

main ()