'''
@author : manojbandari
Replace all the special characters(!, @, #, $, %, ^, &, *)
in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    str_out = ""
    for i in str_input:
        if i >= '0' and i <= '9':
            str_out = str_out + i
        elif i >= 'a' and i <= 'z':
            str_out = str_out + i
        elif i >= 'A' and i <= 'Z': 
            str_out = str_out + i
        else:
            str_out = str_out + " "
    print(str_out)


if __name__ == "__main__":
    main()
