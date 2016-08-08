__author__ = 'mayaravaleria'

def factorialsum(n):
    if n == 1: #base case
        return 1
    else:
        return n + factorialsum(n-1)
