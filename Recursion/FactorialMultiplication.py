__author__ = 'mayaravaleria'

def factorialmul(n):
    if n == 1: #base case
        return n
    else:
        return n * factorialmul(n-1)
print(factorialmul(5))