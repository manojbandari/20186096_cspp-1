'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''

# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    string_words = " "
    text = text.lower().replace("\'", "").strip()
    for i in text:
        if i in "!@#$%^&*()_+<>?:/,.;][1234567890":
            string_words = string_words+" "
        else:
            string_words = string_words + i
    return string_words.split(" ")

def clean_word(tup):
    '''
    to clean the words which are present in file
    '''
    dictionary = {}
    stop_words = load_stopwords("stopwords.txt")
    for word in tup:
        word = word.strip()
        if word not in stop_words and len(word) > 0:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    return dictionary

def frequency(tup, dictionary):
    '''
    combining two dictionaries
    '''
    for word in tup[1]:
        if word in tup[1] and word in dictionary:
            count_words = tup[0], tup[1][word]
            dictionary[word].append(count_words)

        if word not in dictionary:
            dictionary[word] = [(tup[0], tup[1][word])]

    return dictionary



def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''
    search_index = {}
    for i in enumerate(docs):
    # initialize a search index (an empty dictionary)
    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop
        search_index.update(frequency((i[0], clean_word(word_list(i[1]))), search_index))
    # print(tup)
    # for i in range(len(tup)):
        #search_index.update(frequency(tup[i]))
        # clean up doc and tokenize to words list
       # tup=tup+(i[0],clean_word(i[1]))
        # add or update the words of the doc to the search index
    return search_index
    # return search index

# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files

def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
