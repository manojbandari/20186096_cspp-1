'''
@author : manojbandari
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
'''

def main():
    '''
    # epsilon and step are initialized
    # don't change these values
    '''
    epsilon = 0.01
    step = 0.1
    num_input = int(input())
    h_igher = num_input
    bi_val = (h_igher + l_ower)/2.0
    while abs(bi_val**2 - num_input) > epsilon:
        if bi_val**2 < num_input:
            l_ower = bi_val
        else:
            h_igher = bi_val
        bi_val = (h_igher + l_ower)/2.0
    print(bi_val)

if __name__== "__main__":
    main()
