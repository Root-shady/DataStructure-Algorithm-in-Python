def dotProduct(a, b):
    """Write a short Python program that takes two arrays a and b of length n
    storing int values, and returns the dot product of a and b. That is, it returns
    an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n− 1.
    
    >>> dotProduct([1,2,3], [2,3,4])
    [2, 6, 12]
    >>> dotProduct([3,2,3], [5,6,8])
    [15, 12, 24]
    >>> dotProduct([1,2,3], [2,1,3])
    [2, 2, 9]
    """
    # Assumption: The length of the array are the same
    return [a[i]*b[i] for i in range(len(a))]

def indexOutOfBound(data):
	"""1.23 Give an example of a Python code fragment that attempts to write an
	element to a list based on an index that may be out of bounds. If that index
	is out of bounds, the program should catch the exception that results, and
	print the following error message:
	“Don’t try buffer overflow attacks in Python!”"""

	import random
	while True:
		try:
			index = random.randrange(0, len(data)+1) # The last number is exlusive
			print(data[index])
		except IndexError as e:
			print("Don't try buffer overflow attacks in Python!")
			break
	
def vowelsCount(data):
	"""1.24 Write a short Python function that counts the number of vowels in a given
	character string.
	
	>>> vowelsCount("you are kidding")
	6
	>>> vowelsCount("you are")
	4
	>>> vowelsCount("good")
	2
	>>> vowelsCount("GOOD")
	2
	"""
	count = 0
	for i in data:
		if i in "aeiouAEIOU":
			count += 1
	return count

def removePunctuation(data):
	"""25 Write a short Python function that takes a string s, representing a
	sentence, and returns a copy of the string with all punctuation removed.
	For example, if given the string "Let s try, Mike.", this function would
	return "Lets try Mike"  
	
	>>> removePunctuation("You should be here, then we can go together.")
	'You should be here then we can go together'
	>>> removePunctuation("You, And, I? Good!")
	'You And I Good'
	"""
	import string
	return ''.join([i for i in data if i not in string.punctuation])
# For more efficient solution: visit http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python

def arithmeticHelper(a, b, c, operators):
	for i in operators:
		try:
			if(i(a, b) == c):
				return True
		except ZeroDivisionError:
			pass
	return False
def arithmeticTest(a, b, c):
	""" 1.26 Write a short program that takes as input three integers, a, b, and c, from
	the console and determines if they can be used in a correct arithmetic
	formula (in the given order), like “a+ b = c,” “a = b− c,” or “a∗ b = c.”
	
	>>> arithmeticTest(3,4,7)
	True
	>>> arithmeticTest(5, 6, 30)
	True
	>>> arithmeticTest(5, 6, 31)
	False
	>>> arithmeticTest(10, 4, 6)
	True
	>>> arithmeticTest(8, 4, 2)
	True
	>>> arithmeticTest(11, 33, 3)
	True
	>>> arithmeticTest(1, 3, 2)
	True
	>>> arithmeticTest(1, 0, 2)
	False
	"""
	from operator import add, sub, mul, truediv
	operators = [add, sub, mul, truediv]
	return arithmeticHelper(a,b,c,operators) or \
		arithmeticHelper(a,c,b, operators) or \
		arithmeticHelper(b,a,c, operators) or \
		arithmeticHelper(b,c,a, operators) or \
		arithmeticHelper(c,a,b, operators) or \
		arithmeticHelper(c,b,a, operators)

# Sklip the 1.27 and 1.28

if __name__ == '__main__':
    import doctest
    doctest.testmod()

