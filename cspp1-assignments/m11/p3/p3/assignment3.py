'''
author : manojbandari
# Assignment-3
At this point, we have written code to generate a random hand_dict
and display that hand_dict to the user. We can also ask the user for a word (Python's input)
and score the word (using your getWordScore). However, at this point we have not written any code
to verify that a word given by a player obeys the rules of the game.
A valid word is in the word list;
and it is composed entirely of letters from the current hand_dict.
Implement the isValidWord function.

Testing: Make sure the test_isValidWord tests pass. In addition,
you will want to test your implementation by calling it multiple
times on the same hand_dict - what should the correct behavior be? Additionally,
the empty string ('') is not a valid word - if you code this function correctly,
you shouldn't need an additional check for this condition.

Fill in the code for isValidWord in ps4a.py and be sure you've passed
the appropriate tests in test_ps4a.py before pasting your function definition here.
'''

def is_valid_word(word_input, hand_dict, word_list):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand_dict. Otherwise, returns False.

    Does not mutate hand_dict or wordList.

    word: string
    hand_dict: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    count = 0
    if word_input in word_list:
        for i in word_input:
            if i in hand_dict and hand_dict[i] > 0:
                count += 1
        if count == len(word_list):
            return True
    return False




def main():
    '''
    main function
    '''
    word_input = input()
    n_len = int(input())
    adict_dict = {}
    for i in range(n_len):
        i = input()
        l_list = i.split()
        adict_dict[l_list[0]] = int(l_list[1])
    l2_list = input().split()
    print(is_valid_word(word_input, adict_dict, l2_list))



if __name__ == "__main__":
    main()
