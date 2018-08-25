'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    string_new=""
    for i in range(len(string)):
        if string[i] in '!@#$%^&*()\t ':
            pass
        else:
            string_new= string_new+string[i]
    return string_new

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
