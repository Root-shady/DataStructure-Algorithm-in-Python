# -*- coding: utf-8 -*-
# Chapter 2 Object Oriented Programming

"""R-2.4 Write a Python class, Flower, that has three instance variables of type 
str, int, and float, that respectively represent the name of the flower, its
number of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type."""

class Flower:
	def __init__(self, name, petals, price):
		self._name = name
		self._petals = petals
		self._price = price
	
	def get_flower_name(self):
		return self._name

	def get_flower_petals(self):
		return self._petals 

	def get_flower_price(self):
		return self._price

	def set_flower_name(self, name):
		self._name = name

	def set_flower_petals(self, petals):
		self._petals = petals

	def set_flower_price(self, price):
		self._price = price

# The basic CreditCard Class
class CreditCard:
	def __init__(self, customer, bank, acnt, limit):
		self._customer = customer
		self._bank = bank
		self._account = acnt
		self._limit = limit
		self._balance = 0
	
	def get_customer(self):
		return self._customer
	
	def get_bank(self):
		return self._bank
	
	def get_account(self):
		return self._account
	
	def get_limit(self):
		return self._limit
	
	def get_balance(self):
		return self._balance

	def charge(self, price):
		if price + self._balance > self._limit:
			return False
		else:
			self._balance += price
			return True

	def make_payment(self, amount):
		self._balance -= amount
"""R-2.5 Use the techniques of Section 1.7 to revise the charge and make payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter

In Python3:
	
	if not isinstance(parameter, (int,float)):
		raise ValueError
In Python2, you may need to add the (long) type into the list
The classical Python ,metality, though, is that it's easier to ask forgiveness
than permission.
	try:
		self._balance -= parameter:
	except TypeError:
		# do something else
"""

"""R-2.7 The CreditCard class of Section 2.3 initializes the balance of a new
account to zero. Modify that class so that a new account can be given a
nonzero balance using an optional fifth parameter to the constructor. The
four-parameter constructor syntax should continue to produce an account
with zero balance.

	In the class definition: 
		def __init__(self, customer, bank, acnt, limit, balance=0):
			self._balance = balance
"""

"""In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
Explain how the Vector class definition can be revised so that this syntax
generates a new vector."""

class Vector:
	def __init__(self, n, data=[]):
		if data: # data is empty or not
			if n != len(data):
				raise ValueError
			else:
				self._seq = data
		else:
			self._seq = [0] * n
		self._length = n
	
	def __len__(self):
		return self._length

	def __getitem__(self, k):
		return self._seq[k]

	def __setitem__(self, k, val):
		self._seq[k] = val

	def _valid_check(self, other):
		if not isinstance(other, Vector) or self._length != len(other):
			raise ValueError
	
	def _operation(self, other, operator):
		result = Vector(self._length)
		for i in range(self._length):
			result[i] = operator(self[i], other[i])
		return result
	
	def __add__(self, other):
		from operator import add
		self._valid_check(other)
		return self._operation(other, add)

	def __sub__(self, other):
		from operator import sub
		self._valid_check(other)
		return self._operation(other, sub)

	def __mul__(self, other):
		"""Dot product of the vectors"""
		from operator import mul
		self._valid_check(other)
		return self._operation(other, mul)


	
	def __str__(self):
		return '[' +  ' '.join( [str(i) for i in self._seq] ) +']'

"""In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
Explain how the Vector class definition can be revised so that this syntax
generates a new vector.
	
	# The [5, 2, 10, -2 ,1] will fail the _valid_check method.
	
	Add the __radd__() function, will work this out.
	def __radd__(self, other):
		return self + other

"""

"""R-2.12 Implement the mul method for the Vector class of Section 2.3.3, so
that the expression v 3 returns a new vector with coordinates that are 3
times the respective coordinates of v.
	
	def __mul__(self, n):
		if isinstance(n, int):
			raise ValueError
		return Vector(self._length * n, self._seq * n)
"""



if __name__ == '__main__':
	a = Vector(5)
	b = Vector(5, [2,3,4,5,6])
	c = Vector(5, [6,5,4,3,2])
	print(a)
	print(b)
	print(a+b)
	print(b+c)
	print(a-b)
	print(b-c)
	print(a * b)
# ======================================================
"""What are some potential efficiency disadvantages of having very deep inheritance 
trees, that is, a large set of classes, A, B, C, and so on, such that B extends 
A, C extends B, D extends C, etc.?

My Answer: The dynamic dispatch takes more time to determine the identifier and 
its associated value. Also, you need to keep a large amount of key-value pair,
which is not memory efficient.
	(1). Deep inheritance results in a very tight bingding between a superclass 
	and its subclasses
	(2). Removing or swapping out a superclass may break subclasses. 
	(3). Deep inheritance is too complicated, which make the code hard to read.
"""

"""
What are some potential efficiency disadvantages of having very shallow
inheritance trees, that is, a large set of classes, A, B, C, and so on, such
that all of these classes extend a single class, Z?

If A, B, C are not related in real word, then there i nothing wrong.
Inheritance should be used when the classes form a strict hierarchy, where
subclasses are their parent classes in every sense of the word.
In that way, keep a shallow inheritance trees may cause code redundance. 
And also hard to maintained.
"""

