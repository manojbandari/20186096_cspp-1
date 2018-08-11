'''
    @author : manoj bandari
    Assignment-1 Create Social Network
'''

def create_social_network(data_string):
    '''
        The data_string argument passed to the function is a string
        It represents simple social network data_string
        In this social network data_string there are people following other people

        Here is an example social network data_string string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data_string is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''

    # remove the pass below and start writing your code
    data_string=data_string.split("/n")
    dict_convert={}
    for i in range(len(data_string)):
        dict_convert=data_string
    return dict_convert

def main():
    '''
        handling testcase input and printing output
    '''
    string_input = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string_input += input()
        string_input += "/n"

    print(create_social_network(string_input))

if __name__ == "__main__":
    main()
