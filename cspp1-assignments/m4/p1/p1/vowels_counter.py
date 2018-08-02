'''
@author : manojbandari
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
 Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
 For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5
'''
def main():
    '''
    counting the vowels in a string
    '''
    string_input = input()
    # the input string is in s
    # remove pass and start your code here
    count_vowels = 0
    for var in string_input:
        if var in "aeiou":
            count_vowels += 1
    print(count_vowels)

if __name__ == "__main__":
    main()
