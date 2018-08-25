'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    '''
    tokenize the string
    '''
    string_tokenize = {}
    for i in string:
        if i not in string_tokenize:
            string_tokenize[i] = 1
        else:
            string_tokenize[i] += 1
    return string_tokenize
            
def main():
    '''
    main function
    read inputs
    '''
    string=" "
    number_of_lines = int(input())
    for i in range(number_of_lines):
        string+=input()
    print(string)
    string_new = ""
    for i in string:
        if i in '!@#$%.^&*;"\t().,':
            string_new = string_new + i
        else:
            string_new = string_new+i
    string.replace('\t"'," ")
    print(tokenize(string_new.split(" ")))

if __name__ == '__main__':
    main()
