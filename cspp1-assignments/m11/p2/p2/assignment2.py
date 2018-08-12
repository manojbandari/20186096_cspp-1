'''
author : manojbandari
#Exercise: Assignment-2
#Implement the updateHand function.
Make sure this function has no side effects: i.e.,
it must not mutate the hand passed in. Before pasting your function
definition here, be sure you've passed the appropriate tests in test_ps4a.py.
'''

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    for i in word:
        if i in hand:
            hand[i] -= 1
    return hand
    

def main():
    '''
    main function
    '''
    n_input = input()
    adict_dict = {}
    for i in range(int(n_input)):
        i = input()
        l_list = i.split()
        adict_dict[l_list[0]] = int(l_list[1])
    data1 = input()
    print(update_hand(adict_dict,data1))
        


if __name__== "__main__":
    main()
