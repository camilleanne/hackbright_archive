def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return float(num1) / float(num2)

def square(num1):
    return num1 * num1

def cube(num1):
    return num1 * num1 * num1

def power(num1, num2):
    # Easy power function result = num1 ** num2
    i = 0
    result = 1
    while i < num2:
        result = result * num1
        i += 1
    return result

def mod(num1, num2):
    return num1 % num2