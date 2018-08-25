'''
author: manojbandari
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''
    read multiple lines
    '''
    number_of_lines = int(input())
    multiple_lines = " "
    lis_output = []
    for i in range(number_of_lines):
        multiple_lines += input()
        multiple_lines = multiple_lines+"0@"
    lis_output = multiple_lines.split("0@")
    for i in enumerate(lis_output):
        print(lis[i].strip())


if __name__ == '__main__':
    main()
