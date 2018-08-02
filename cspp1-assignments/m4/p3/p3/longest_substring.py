'''
@author : manojbandari 
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s
in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem,
we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.
'''
def main():
    '''
    # the input string is in s
    # remove pass and start your code here
    '''
    input_str = input()
    temp_str ="" 
        for i in range(len(input_str)-1):
        sub_str = input_str[i]
        while i + 1 < len(input_str) and input_str[i] <= input_str[i+1]:
            i += 1
            sub_str += input_str[i]
        if len(sub_str) > len(temp_str):
            temp_str = sub_str
    print(temp_str)
if __name__== "__main__":
    main()
