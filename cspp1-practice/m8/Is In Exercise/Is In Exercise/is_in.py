'''
author : manojbandari

# Exercise: Is In
# Write a Python function, isIn(char, aStr),
that takes in two arguments a character and String and 
returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.
'''
def isIn(char, astr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if char in astr:
        return True
    elif len(astr) == 1:
        return False
    else:
        return isIn(char,astr[1:])
   

def main():
    '''
    main function
    '''
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))


if __name__== "__main__":
    main()