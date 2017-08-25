l = [1, 2, 3, 4, 5]


# Multiply all the elements in a list
def multiply_list(l):
    if len(l) == 1:
        return l[0]
    return l[0] * multiply_list(l[1:])

#print multiply_list(l)


#Find the factorial of a number
def factorial(l):
    if l == 1 or l == 0:
        return 1
    return l * factorial(l-1)

#print factorial(5)


# Count the number of elements in the list l
def count_list(l):
    if l == []:
        return 0
    return 1 + count_list(l[1:])
#print count_list(l)

# Sum all of the elements in a list
def sum_list(l):
    if l == []:
        return 0
    return l[0] + sum_list(l[1:])

#print sum_list(l)

# Reverse a list without slicing or loops
def reverse(l):
    if l == []:
        return []
    temp = l.pop(0)
    return reverse(l) + [temp]

#print reverse(l)

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
 
#print fibonacci(10)

# Finds the index of item i in the list l.... RECURSIVELY
def find(l, i):
    if l[0] == i:
        return 0
    return 1 + find(l[1:], i)

#print find(l, 4)

# Determines if a string is a palindrome
def palindrome(some_string):
    if len(some_string) == 1 or len(some_string) == 0:
        return True
    return (some_string[0] == some_string[-1]) and palindrome(some_string[1:-1])
    # elif some_string[0] != some_string[-1]: 
    #      return False
    # return palindrome(some_string[1:-1])

#print palindrome("kayak")

# Given the width and height of a sheet of paper, and the number of times to fold it, 
#return the final dimensions of the sheet as a tuple. 
#Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    width = float(width)
    height = float(height)
    if width == 0 or height == 0:
        return (0, 0)
    elif folds == 0:
        return (width, height)
    elif folds >= 7:
        return "Material science forbids this."
    elif width >= height:
        return fold_paper(width/2, height, folds - 1)
    elif width < height:
        return fold_paper(width, height/2, folds - 1)
# print fold_paper(8, 11, 7)

# Count up
# Print all the numbers from n to target
def count_up(target, n):
    if target == n:
        return target
    print n
    return count_up(target, n+1)

print count_up(21, 6)

