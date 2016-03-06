# -*- coding: utf-8 -*-
# The Project Part

def stringCombination():
	"""1.29 Write a Python program that outputs all possible strings formed by
	using the characters c , a , t , d , o , and g exactly once."""
	data = 'catdog'
	for i in range(len(data)):
		print(allCombination(data, i))

def allCombination(data, i):
	if len(data) == 1:
		return data
	else:
		return data[i] + allCombination(data[:i]+data[i+1:], 1)
	

def dividedByTwo(n):
	""" 1.30 Write a Python program that can take a positive integer greater than 2 as
	input and write out the number of times one must repeatedly divide this
	number by 2 before getting a value less than 2.
	
	>>> dividedByTwo(8)
	3
	>>> dividedByTwo(9)
	3
	>>> dividedByTwo(16)
	4
	>>> dividedByTwo(32)
	5
	>>> dividedByTwo(30)
	4
	"""
	import math 
	return int(math.log(n, 2))

def divideTwo(n):
	""" Using recursion to solve the problem.
	
	>>> divideTwo(8)
	3
	>>> divideTwo(7)
	2
	>>> divideTwo(2)
	1
	>>> divideTwo(10)
	3
	>>> divideTwo(16)
	4
	>>> divideTwo(32)
	5
	"""
	if n < 2:
		return 0
	else:
		return 1 + divideTwo(n/2)

"""Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible."""


if __name__ == '__main__':
	import doctest
	doctest.testmod()

