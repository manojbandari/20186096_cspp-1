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
        if i not in string_tokenize and len(i)>0:
            string_tokenize[i] = 1
        elif i in string_tokenize and len(i)>0:
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
    string_words = " "
    string = string.replace('\"', "").strip()
    for i in string:
        if i in "!@#$%^&*()_+<>?:/,.;][":
            string_words = string_words+" "
        else:
            string_words = string_words + i
    print(tokenize(string_words.split(" ")))

if __name__ == '__main__':
    main()
