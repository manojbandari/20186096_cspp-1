'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
def remove_special(dict1):
    # s = ""
    # for i in dict1:
    #     if i in "!@#$%^&*()_+<>?:>.,-=1234567890":
    #         s = s + ' '
    #     else:
    #         s = s + i
    # return s
    words = dict1.lower().strip().replace("\'","")
    regex = re.compile('[^a-z]')
    words = regex.sub(" ", words).split(" ")
    return words

def calculate_simialrity(dictionary):
    numerator = sum([k[0] * k[1] for k in dictionary.values()])
    denominator_one = math.sqrt(sum([k[0]**2 for k in dictionary.values()]))
    denominator_two = math.sqrt(sum([k[1]**2 for k in dictionary.values()]))
    return numerator / (denominator_one*denominator_two) 
def combine_list(dictionary1, dictionary2):
    
    dictionary={}
    for word in dictionary1:
        dictionary[word] = [dictionary1[word], dictionary2[word]]
    for word in dictionary1:
        if word not in dictionary:
            dictionary[word] = [dictionary1[word], 0]
    for word in dictionary2:
        if word not in dictionary:
            dictionary[word] = [0, dictionary2[word]]

    return dictionary

def word_list(dict_list):
    dictionary = {}
    new_dict = load_stopwords("stopwords.txt")
    for word in dict_list:
        word = word.strip()
        if word not in new_dict and len(word) > 0:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    return dictionary
    # lis = []
    # for i in dict1:
    #     if i not in new_dict:
    #         lis.append(i)
    # print(lis)
    # return lis
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1 = remove_special(dict1)
    dict2 = remove_special(dict2)
    
    dictionary =combine_list(word_list(dict1),word_list(dict2))
    return calculate_simialrity(dictionary)

    
    

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
