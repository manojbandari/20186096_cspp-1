'''
@author : manojbandari
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl',
then your program should print

Number of times bob occurs is: 2'''

def main():
    '''
    # the input string is in s
    # remove pass and start your code here
    '''
    str_input = input()
    sub_str = "bob"
    bob_c= 0
    for var in range(len(str_input)-2):
        com = 0
        temp = var
        check = 0
        while(com < 3 and str_input[temp] == sub_str[com]):
            check += 1
            temp += 1
            com += 1
        if check == 3:
            bob_c += 1
    print(bob_c)

if __name__  == "__main__":
    main()
