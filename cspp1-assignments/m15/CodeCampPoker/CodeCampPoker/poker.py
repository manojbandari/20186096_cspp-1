'''
author : manojbandari
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''

dic_new = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
           '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    # lis=[]
    # lis1=[]
    # count=0
    # for i in range(len(hand)):
    #     lis1.append(hand[i][1])
    #     lis.append(dic_new[hand[i][0]])
    # lis.sort()

    # for i in range(len(lis)-1):
    #     if lis[i+1]-lis[i]!=1:
    #         return False
    # return True
    
    card_values = set('--23456789TJQKA'.index(c) for c, s in hand)
    return len(card_values) == 5 and (max(card_values) - min(card_values) == 4)

    if all(True if c in '2345A' else False for c, s in hand):
        return True
def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    # count2 = 0
    # flag = ord(hand[0])
    # for i in range(1,len(hand)):
    #     if flag == ord(hand[i]):
    #         count2 += 1
    # if count2 == len(hand):
    #     return True
    # else:
    #     return False
    suit = hand[0]
    for h_suit in hand:
        if suit[1] != h_suit[1]:
            return False
    return True

def is_full_house(hand):
    '''
    full house
    '''
    for i in range(len(hand)):
        if hand[0][i]==hand[0][i+1]==hand[0][i+2] and hand[0][i+3]==hand[0][i+4]:
            return True
        elif hand[0][i]==hand[0][i+1] and hand[0][i+2]==hand[0][i+3]==hand[0][i+4]:
            return True
        else:
            return False


def is_four_of_a_kind(hand):
    '''
        four of a kind or not
    '''
    # count = 0
    # for i in range(len(hand)):
    #     lis.append(dic_new[hand[i][0]])
    # lis.sort()
    # flag = lis[0]
    # if lis[0] != lis[1]:
    #     for i in range(1,len(lis)-1):
    #         if lis[i] == lis[i+1]:
    #             count+=1
    #     return bool(count==3)
    # else:
    #     for i in range(1,len(lis)):
    #         if flag==lis[i]
    #             count+=1
    #         return bool(count==3)
    card_values = set('--23456789TJQKA'.index(c) for c, s in hand)
    return len(card_values) == 2


def is_three_of_a_kind(hand):
    '''
    three of a kind
    '''
    card_values = set('--23456789TJQKA'.index(c) for c, s in hand)
    return len(card_values) == 3

def is_two_pair(hand):
    lis=[]
    for i in range(len(hand)):
        lis.append(dic_new[hand[i][0]])
    lis.sort()
    for i in range(len(lis)):
        if hand[i] == hand[i+1]:
            if hand[i+2] == hand[i+3] or hand[i+3] == hand[i+4]:
                return True
            else:
                return False
        else:
            if hand[i+1] == hand[i+2] and hand[i+3] == hand[i+4]:
                return True
            else:
                return False



def is_one_pair(hand):
    '''
    two pair
    '''
    card_values = set('--23456789TJQKA'.index(c) for c, s in hand)
    return len(card_values) == 4

def is_high_card(hand):
    '''
    high card
    '''
    card_values = set('--23456789TJQKA'.index(c) for c, s in hand)
    return len(card_values) == 5




def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    c_rank = 0
    maxi=[]
    lis=[]
    if is_straight(hand) and is_flush(hand):
        c_rank = 9
    elif is_four_of_a_kind(hand):
        c_rank = 8
    elif is_full_house(hand):
        c_rank = 7

    elif is_flush(hand):
        c_rank = 6
    elif is_straight(hand):
        c_rank = 5
    elif is_three_of_a_kind(hand):
        c_rank = 4
    elif is_two_pair(hand):
        c_rank = 3
    elif is_one_pair(hand):
        c_rank = 2
    elif is_high_card(hand):
        for k in range(len(hand)):
            lis.append(dic_new[hand[k][0]])
        maxi=sum(lis)
        if maxi>1:
            for i in range(len(maxi)):
                if maxi[i+1]>max[i]:
                    c_rank = 1.1
                else:
                    c_rank = 1

    return c_rank



    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best han
    #print(hands)

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''
    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)

    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
