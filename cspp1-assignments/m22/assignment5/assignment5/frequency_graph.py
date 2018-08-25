'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    '''
    frequency graph function
    '''
     for key in sorted(dictionary):
        for i in range(20):
            if dictionary[key] == i:
                dictionary[key] = i*'#'
        print(key, "-", dictionary[key])

def main():
    '''
    main function
    '''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
