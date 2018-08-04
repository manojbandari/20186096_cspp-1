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
    while(i>0):
    	temp = i % 10
    	prod = prod * temp
    	i = i // 10
    print(prod)
if __name__ == "__main__":
    main()
