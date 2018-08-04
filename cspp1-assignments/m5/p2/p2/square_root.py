
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
    s_tep = 0.1
    s_quare = int(input())
    g_uess = 0.0
    while g_uess <= s_quare:
        if abs(g_uess**2-s_quare) < e_psilon:
            break
        else:
            g_uess += s_tep
    print(str(g_uess))
if __name__ == "__main__":
    main()
