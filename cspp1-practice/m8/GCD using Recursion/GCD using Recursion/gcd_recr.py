# Exercise: GCDRecr
# Write a Python function, gcdRecur(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a%b==0:
    	return b
    elif b%a==0:
    	return a
    elif a>b:
    	return gcdRecur(b,a%b)
    else:
    	return gcdRecur(a,b%a)
    


def main():
    data = input()
    data = data.split()
    print(gcdRecur(int(data[0]),int(data[1])))

if __name__== "__main__":
    main()