string = "Mares eat oats and does eat oats and little lambs eat ivy"
str_list = string.split()
sec_list = ['but', 'a', 'kid', 'will', 'eat', 'ivy', 'too', 'does', "wouldn't", 'you']
tuple_list = [(32, 4), (2, 42), (6, 7), (78, 84), (32, 4)]

 # function that takes an iterable 
 # (something you can loop through, ie: string, list, or tuple)
 # and produces a dictionary with all distinct elements as the keys, 
 # and the number of each element as the value
def count_unique(some_iterable):
    counted_dict = {}
    #not quite necessary, could also do a list of single characters. 
    # Makes sure that the dictionary is created with distinct 'words' if it has them.
    if type(some_iterable) == str:
        working_list = some_iterable.split()
    else:
        working_list = list(some_iterable)

    while working_list != []:
        popped = working_list.pop()
        counted_dict[popped] = counted_dict.get(popped, 0) + 1
    return counted_dict

# print count_unique(tuple_list)
    
# Given two lists, 
# (without using the keyword 'in' or the method 'index') 
# return a list of all common items shared between both lists
def common_items(list1, list2):
    working_list = []
    while list1 != []:
        popped = list1.pop()
        i = len(working_list)-1
        is_in_list = False
        while i > 0:
            if popped == working_list[i]:
                is_in_list = True
            i -= 1
        if not is_in_list:
            i = len(list2)-1
            while i > 0:
                if popped == list2[i]:
                    working_list.append(popped)
                i -= 1
    return working_list
    
# 'cheating' way with sets
# def common_items3(list1, list2):
#     list1 = set(list1)
#     list2 = set(list2)
#     return list1 & list2

# print common_items(str_list, sec_list)


# Given two lists, 
# (without using the keyword 'in' or the method 'index') 
# return a list of all common items shared between both lists. 
# This time, use a dictionary as part of your solution.
def common_items2(list1, list2):
    counted_dict = {}
    common_words = []
    i = len(list1)-1
    while i > 0:
        if counted_dict.get(list1[i], False):
            counted_dict[list1[i]][0] += 1
        else:
            counted_dict[list1[i]] = [1, 0]
        i -= 1
    
    i = len(list2)-1
    while i > 0:
        if counted_dict.get(list2[i], False):
            counted_dict[list2[i]][1] += 1
        else:
            counted_dict[list2[i]] = [0, 1]
        i -= 1

    while counted_dict:
        key, value = counted_dict.popitem()
        if value[0] > 0 and value[1] > 0:
            common_words.append(key)

    return common_words

print common_items2(str_list, sec_list)


