'''
@author: manojbandari
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    '''
    clean a string without special characters
    '''
    string_new = ""
    for i in string:
        if i in '!@#$%^&*().\t ':
            pass
        else:
            string_new = string_new+i
    return string_new

def main():
    '''
    read input
    '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
