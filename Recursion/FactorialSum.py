__author__ = 'mayaravaleria'

def factorialsum(n):
    if n == 1: #base case
        return n
    else:
        return n + factorialsum(n-1)
print(factorialsum(5))




