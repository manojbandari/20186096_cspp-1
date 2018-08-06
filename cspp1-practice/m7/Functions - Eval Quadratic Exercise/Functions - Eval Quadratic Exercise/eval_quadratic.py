'''
@author : manojbandari
# Exercise: eval quadratic

# Write a Python function, eval_quadratic(a, b, c, x_input),
that returns the value of the quadratic a . x_input 2 + b . x_input + c

# This function takes in four numbers and returns a single number.
'''

def eval_quadratic(a_n, b_n, c_n, x_input):
    '''
    print the quadratic expression
    '''
    return a_n*(x_input**2)+(b_n*x_input+c_n)

def main():
    '''
    take the integer input
    call the function
    '''
    data_input = input()
    data_input = data_input.split(' ')
    data_input = list(map(float, data_input))
    # print(data_input)
    for x_input in range(len(data_input)):
        temp = str(data_input[x_input]).split('.')
        if temp[1] == '0':
            data_input[x_input] = int(float(str(data_input[x_input])))
        else:
            data_input[x_input] = data_input[x_input]
    print(eval_quadratic(data_input[0], data_input[1], data_input[2], data_input[3]))

if __name__ == "__main__":
    main()
