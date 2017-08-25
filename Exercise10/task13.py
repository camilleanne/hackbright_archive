'''

'''
def round_up(rat_num):
    base = int(rat_num)
    if rat_num - base >= 0.5:
        return base+1
    else:
        return base

    
def line_count(string):
    if not inp:
        return 0
    count = 1
    for char in string:
        if char == "\n":
           count  += 1    
    return count

def pythagorean_theorum(a, b):
    c = a * a + b * b
    return Math.sqrt(c)
    

def reverse(input_list):
    size = len(input_list)
    for i in range(len(input_list)/2):
        temp = input_list[i]
        input_list[i] = input_list[size-i-1]
        input_list[size-i-1] = temp
    return input_list

    
def count_of_words():
    f = open("sample_input.txt")
    word_list = f.split()
    word_count = dict()
    for word in word_list:
        num = word_count.get(word, 0)
        num += 1
        word_count[word] = num

    for key, value in word_count.iteritems():
        print "%s:\t%d"%(key, value)

def sort(input_list):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(input_list)-1):
            if input_list[i] > input_list[i+1]:
                temp = input_list[i]
                input_list[i] = input_list[i+1]
                input_list[i+1] = temp
                swapped = True
    return input_list
