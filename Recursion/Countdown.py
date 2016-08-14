__author__ = 'mayaravaleria'

def countdown(n):
    if n == 0: #base case
        return 0
    else:
        print(n)
        return countdown(n-1)
print(countdown(5))

