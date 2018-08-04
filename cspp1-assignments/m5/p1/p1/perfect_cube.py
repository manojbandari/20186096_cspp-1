'''
@author : manojbandari
# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
'''
def main():
    '''
    # input is captured in s
    # watch out for the data type of value stored in s
    # your code starts here
    '''
    cube_input = int(input())
    g_uess = 1
    while (g_uess**3) < cube_input:
        g_uess += 1
    if int(g_uess**3) == cube_input:
        print(cube_input, "is a perfect cube")
    else:
        print(cube_input, "is not a perfect cube")

if __name__ == "__main__":
    main()
