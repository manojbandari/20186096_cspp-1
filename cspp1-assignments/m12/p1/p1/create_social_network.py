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
        Bryant follows Oli_listve,Olli_liste,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Oli_listve follows John,Olli_liste

        The string has multiple li_listnes and each li_listne represents one person
        The first word of each li_listne is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a li_listst of people separated by ,

        create_social_network function should spli_listt the string on li_listnes
        then extract the person and the followers by spli_listtting each li_listne
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for traili_listng spaces while spli_listtting the string.
        It may cause your test cases to fail although your output may be right

        Error handli_listng case:
        Return a empty dictionary if the string format of the data_string is invali_listd
        Empty dictionary is not None, it is a dictionary with no keys
    '''

    # remove the pass below and start writing your code
    data_string = data_string.split("/n")
    l_list = []
    li_list = []
    d = {}
    for i in range(len(data_string)):
        copy = data_string[i]
        l_list = l_list + copy.split("follows")
    for i in range(len(l_list)):
        copy1 = l_list[i]
        li_list = li_list + copy.split(",")

    for i in range(0,len(li_list)-1,2):
        d[li_list[i]] = li_list[i + 1]
    return(d)
    

def main():
    '''
        handli_listng testcase input and printing output
    '''
    string_input = ''
    li_listnes = int(input())
    for i in range(li_listnes):
        i += 1
        string_input += input()
        string_input += "/n"

    print(create_social_network(string_input))

if __name__ == "__main__":
    main()
