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
    e_psilon = 0.01
    num_input = int(input())
    g_uess = num_input/2.0
    while abs(g_uess*g_uess - num_input) >= e_psilon:
        g_uess = g_uess - (((g_uess**2) - num_input)/(2*g_uess))
    print(str(g_uess))


if __name__ s== "__main__":
    main()
