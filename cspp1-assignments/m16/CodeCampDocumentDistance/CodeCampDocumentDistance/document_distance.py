'''
    Document Distance - A detailed description is given in the PDF
'''
def remove_special(dict1):
    s = ""
    for i in dict1:
        if i in "!@#$%^&*()_+<>?:>.,\"-=1234567890'":
            s = s + ''
        else:
            s = s + i
    return s
def calculate_simialrity(dictionary):
    numerator = sum([k[0] * key[1] for key in dictionary])
    denominator_one = math.sqrt(sum([key[0]**2 for key in dictionary.values()]))
    denominator_two = math.sqrt(sum([key[1]**2 for key in dictionary.values()]))
    return numerator / (denominator_one*denominator_two) 
def combine_list(lis, lis1):
    dictionary = {}
    dictionary1 = {}
    dictionary2 = {}
    for word in lis:
        if word not in lis and len(word) > 0:
            dictionary1[word] = 1
        else:
            dictionary1[word] += 1
    for word in lis1:
        if word not in lis1 and len(word) > 0:
            dictionary2[word] = 1
        else:
            dictionary2[word] += 1


    for word in dictionary1:
        dictionary[word] = [dictionary1[word], dictionary2[word]]
    for word in dictionary1:
        if word not in dictionary:
            dictionary[word] = [dictionary1[word], 0]
    for word in lis1:
        if word not in dictionary:
            dictionary[word] = [0, dictionary2[word]]

    return dictionary

def word_list(dict1, new_dict):
    lis = []
    for i in dict1:
        if i not in new_dict:
            lis.append(i)
    return lis
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    new_dict1 = {}
    word_freq = {}
    freq = []
    dict1 = remove_special(dict1).strip().lower().split(" ")
    dict2 = remove_special(dict2).strip().lower().split(" ")
    new_dict = load_stopwords("stopwords.txt")
    dictionary =combine_list(word_list(dict1,new_dict),word_list(dict2,new_dict))
    return calculate_simialrity(dictionary)

    
    # k=0
    # for m in lis:
    #   if m in word_freq:
    #       word_freq[0]=word_freq+1
    #   else:
    #       word_freq=m
    # print(word_freq)

     # for m in lis:
    #   count=0
    #   if m in lis:
    #       count+=1
    #   lis.append(count)
    # print(lis)


        # count=0
        # for n in lis1:
        #   if m==n:
        #       count+=1
        #   else:
        #       word_freq[m]=count
        #       word_freq[n]=count
        # word_freq[m]=count

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
