'''
@author : manojbandari
# Exercise: square
# Write a Python function, square, that takes in one number and
returns the square of that number.

# This function takes in one number and returns one number.
'''

def square(x_input):
    '''
    x_input: int or float.
    '''
    return x_input*x_input

def main():
    '''
    main function
    '''
    data_input = input()
    data_input = float(data_input)
    temp = str(data_input).split('.')
    if temp[1] == '0':
        print(square(int(float(str(data_input)))))
    else:
        print(square(data_input))

if __name__ == "__main__":
    main()
