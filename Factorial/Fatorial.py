__author__ = 'mayaravaleria'

def fatorial(n):
    if n == 0: #base case
        return 1 #return 1, because 0! = 1
    else:
        return n * fatorial(n-1) #instantiate the recursive call parameter according to base case

