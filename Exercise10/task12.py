#!/bin/env python

"""
Write the following two functions
    c_to_f(float) -> float
    f_to_c(float) -> float

c_to_f should convert a temperature in celsius to fahrenheit, 
and f_to_c should do the opposite
"""
def c_to_f(celsius):
	return (celsius * 1.8) + 32

def f_to_c(fahrenheit):
	return (((fahrenheit - 32) * 5.0) / 9.0)

print c_to_f(32)
print f_to_c(90)