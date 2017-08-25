import os
import shutil
import os.path

def create_directories():

	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	i = 0
	for item in alphabet:
		os.mkdir('./sorted/'+alphabet[i])
		i += 1

def sort_files():
	file_list = os.listdir('./original_files/')	
	for item in file_list:
		#source = os.path.join('./original_files/',item)
		#destination = os.path.join('./sorted/',item[0])
		# print destination
		# print source
		shutil.move('./original_files/'+item, './sorted/'+item[0])

def main():
	create_directories()
	sort_files()

main()