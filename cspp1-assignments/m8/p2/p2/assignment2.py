'''
@author : manojbandari
# Exercise: Assignment-2
# Write a Python function, sumofdigits,
that takes in one number
and returns the sum of digits of given number.

# This function takes in one number and returns one number.
'''

def sumofdigits(cum_n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if sum_n == 0:
        return 0
    return (sum_n % 10) + sumofdigits(sum_n // 10)


def main():
    '''
    main functon
    '''
    a_input = input()
    print(sumofdigits(int(a_input)))  

if __name__ == "__main__":
    main()
