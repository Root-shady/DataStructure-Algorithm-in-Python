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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
