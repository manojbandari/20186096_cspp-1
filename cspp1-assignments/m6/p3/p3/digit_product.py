'''
Given a  number int_input, find the product of all the digits
example: 
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    i = int_input
    prod = 1
    Flag = 0
    if i < 0:
        Flag = 1
        i = abs(i)
    if i =0:
        prod = 0
    while i > 0:
        temp = i % 10
        prod = prod * temp
        i = i // 10
    if flag = 1
        prod = -(prod)
    print(prod)
if __name__ == "__main__":
    main()
