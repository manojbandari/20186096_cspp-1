'''
@author : manojbandari
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number
 and returns the factorial of given number.

# This function takes in one number and returns one number.
'''
#from sis import *
#sys.setrecursionlimit(10000)
def factorial(fact_n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here

    #if fact_n == 0 or fact_n == 1:
    if fact_n in (0, 1):
        return 1
    return fact_n*factorial(fact_n-1)

def main():
    '''
    main function
    '''
    a_input = input()
    print(factorial(int(a_input)))

if __name__ == "__main__":
    main()
