'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    number_of_lines=int(input())
    multiple_lines=" "
    for i in range(number_of_lines):
        multiple_lines+=input()
        multiple_lines=multiple_lines+","
    for i in range(len(multiple_lines)):
        if multiple_lines[i]==",":
            print(multiple_lines[:i])
            break


if __name__ == '__main__':
    main()
