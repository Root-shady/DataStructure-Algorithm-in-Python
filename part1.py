 # -*- coding: utf-8 -*-
def is_mulltiple(n, m):
    """1. Write a short Python function, is multiple(n, m), that takes two integer
    values and returns True if n is a multiple of m, that is, n = mi for some
    integer i, and False otherwise

    >>> is_mulltiple(8,4)
    True
    >>> is_mulltiple(8,5)
    False
    >>> is_mulltiple(8,2)
    True
    """

    try:
        result = True if n % m == 0 else False
    except ZeroDivisionError:
        result = False
    finally:
        return result

# Below should have the unit test


def is_even(k):
    """2. Write a short Python function, is even(k), that takes an integer value and
    returns True if k is even, and False otherwise. However, your function
    cannot use the multiplication, modulo, or division operators.
    
    >>> is_even(8)
    True
    >>> is_even(3)
    False
    >>> is_even(5)
    False
    """
    return True if (-1)**k == 1 else False

# There should be a blank in the printed tuple pair, otherwise the doctest won't pass
def minmax(data):
    """3. Write a short Python function, minmax(data), that takes a sequence of
    one or more numbers, and returns the smallest and largest numbers, in the
    form of a tuple of length two. Do not use the built-in functions min or
    max in implementing your solution
    
    >>> minmax([3,4,5,6,7])
    (3, 7)
    >>> minmax([7,6,5,4,3])
    (3, 7)
    >>> minmax([5,4,6,8,7])
    (4, 8)
    >>> minmax([2,4,9,0,7])
    (0, 9)
    """
    minNum, maxNum = data[0], data[0]
    for num in data:
        if minNum > num:
            minNum = num
        if maxNum < num:
            maxNum = num
    return minNum, maxNum  #Auto packing here

def sumSquare(n):
    """1.4 Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the positive integers smaller than n.

    >>> sumSquare(3)
    5
    >>> sumSquare(4)
    14
    >>> sumSquare(6)
    55
    """
    total = 0
    for i in range(n):
        total += i * i;
    return total


def sumSquare2(n):
    """1.5 Give a single command that computes the sum from Exercise R-1.4, 
    relying on Python’s comprehension syntax and the built-in sum function.

    >>> sumSquare2(3)
    5
    >>> sumSquare2(4)
    14
    >>> sumSquare2(6)
    55
    """
    return sum([i*i for i in range(n)])

def oddSumSquare(n):
    """1.7 Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the odd positive integers smaller than n.

    >>> oddSumSquare(3)
    1
    >>> oddSumSquare(5)
    10
    >>> oddSumSquare(9)
    84
    >>> oddSumSquare(11)
    165
    """
    return sum(i*i for i in range(n) if i%2 != 0)

"""1.8 Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?
Answer:  j = len(s) + n 
"""

"""1.9 What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
Answer:  range(50, 90, 10)"""

"""1.10 What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
Answer:  range(8, -10, -2)
"""
"""Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
Answer: [2*i for i in range(9)]
"""

def choice(data):
    """1.11 Python’s random module includes a function choice(data) that returns
    a random element from a non-empty sequence. The random module includes a more 
    basic function randrange, with parameterization similar to the built-in range 
    function, that return a random choice from the given range. Using only the 
    randrange function, implement your own version of the choice function
    """
    import random
    return data[random.randrange(len(data))]

def reverse(data):
    """Write a pseudo-code description of a function that reverses a list of n
    integers, so that the numbers are listed in the opposite order than they

    >>> example = [2,3,4,5,6,7]
    >>> reverse(example)
    >>> example
    [7, 6, 5, 4, 3, 2]
    >>> reverse(example)
    >>> example
    [2, 3, 4, 5, 6, 7]
    >>> example = [2,3,4,5,6,7,8]
    >>> reverse(example)
    >>> example
    [8, 7, 6, 5, 4, 3, 2]
    >>> reverse(example)
    >>> example
    [2, 3, 4, 5, 6, 7, 8]
    """
    for i in range(len(data)//2):
        data[i], data[len(data)-i-1] = data[len(data)-i-1], data[i]

def oddPair(data):
    """Write a short Python function that takes a sequence of integer values and
    determines if there is a distinct pair of numbers in the sequence whose
    product is odd.
    
    >>> oddPair([3,4,5,6,7])
    True
    >>> oddPair([2,4,6,6,8])
    False
    >>> oddPair([2,5,4,5,6])
    False
    >>> oddPair([4,5,5,6,6,7,7])
    True
    """
    firstOne = False
    for i in data:
        if i%2 != 0:
            if firstOne and first != i:
                return True
            else:
                firstOne = True
                first =i
    return False

# Performance Isssue, there should be a better way to do this, instead of using 
# the built-in sort function
def distinctSequence(data):
    """ 1.15 Write a Python function that takes a sequence of numbers and determines
    if all the numbers are different from each other (that is, they are distinct).
    
    >>> distinctSequence([3,2,4,1,6])
    True
    >>> distinctSequence([3,2,4,1,6,9,12,3,4])
    False
    >>> distinctSequence([3,2,4,1,6,8,9,0,23,45])
    True
    >>> distinctSequence([3,2,4,1,3])
    False
    """

 # Notice that this will change the parameter data. 
 # You can use the sorted() function instead.
    data.sort()
    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            return False
    return True

"""Had we implemented the scale function (page 25) as follows, does it work
properly?
def scale(data, factor):
    for val in data:
        val = factor
        Explain why or why not.
Answer: This won't work, it will not change the parameter data. 
In every iteration, the val is a (shadow) copy of the element in data, so the 
change on val dose nothing to the data's element.
"""

"""1.18 Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
Answer: [i * (i+1) for i in range(9)] """

"""1.19 Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z  ], but without having to type all 26 such
characters literally
Answer: [chr(i) for i in range(97, 123)]"""

def shuffle(data):
    """ 1.20 Python’s random module includes a function shuffle(data) that accepts a
    list of elements and randomly reorders the elements so that each possible 
    order occurs with equal probability. The random module includes a more basic
    function randint(a, b) that returns a uniformly random integer from a to b 
    (including both endpoints). Using only the randint function, implement your 
    own version of the shuffle function."""

    import random
    for i in range(len(data)-1, 0, -1):
        position = random.randint(0, i) # The i is inclusive here
        data[position], data[i] = data[i], data[position]

def readLines():
	""" 1.21 Write a Python program that repeatedly reads lines from standard input
    until an EOFError is raised, and then outputs those lines in reverse order
    (a user can indicate end of input by typing ctrl-D). Saved it in the file """

	filename = input("Enter the file to be created:")
	fp = open(filename, "w", encoding='utf-8')
	while True:
	    try:
	        line = input("Enter a line:(Use the Ctrl-D to exit): \n")
	        fp.write(line+'\n')
	    except EOFError as e:
	        print("Exist the program")
	        break
	fp.close()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
