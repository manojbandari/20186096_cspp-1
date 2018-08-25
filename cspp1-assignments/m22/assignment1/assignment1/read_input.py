'''
author: manojbandari
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''
    read multiple lines
    '''
    number_of_lines=int(input())
    multiple_lines=" "
    lis=[]
    for i in range(number_of_lines):
        multiple_lines+=input()
        multiple_lines=multiple_lines+"0@"
    lis=multiple_lines.split("0@")
    for i in range(len(lis)):
        print(lis[i].strip())


if __name__ == '__main__':
    main()
