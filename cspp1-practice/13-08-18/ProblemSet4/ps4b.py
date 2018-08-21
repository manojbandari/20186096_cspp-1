'''
@author : manojbandari
'''
from ps4a import *
import time


#
#
# Computer chooses a word
#
#
def comp_choose_word(hand, word_list, n_hand_size):
    """
    Given a hand and a word_list, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the word_list.

    If no words in the word_list can be made from the hand, return None.

    hand: dictionary (string -> int)
    word_list: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    best_score = 0
    # Create a new variable to store the best word seen so far (initially None)
    best_word = None
    # For each word in the word_list
    for word in word_list:
        # If you can construct the word from your hand
        if is_valid_word(word, hand, word_list):
            # find out how much making that word is worth
            score = get_word_score(word, n_hand_size)
            # If the score for that word is higher than your best score
            if score > best_score:
                # update your best score, and best word accordingly
                best_score = score
                best_word = word
    # return the best word you found.
    return best_word

#
# Computer plays a hand
#
def comp_play_hand(hand, word_list, n_hand_size):
    """
    Allows the computer to play the given hand, following the same procedure
    as play_hand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. comp_choose_word returns None).

    hand: dictionary (string -> int)
    word_list: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    print('wait for a while till the computer game completes')
    total_score = 0
    n = 7
    # As long as there are still letters left in the hand:
    while calculate_hand_len(hand) > 0:
        # Display the hand
        print("Current Hand: ", end=' ')
        display_hand(hand)
        # computer's word
        word = comp_choose_word(hand, word_list, n_hand_size)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not is_valid_word(word, hand, word_list):
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score
                score = get_word_score(word, n)
                total_score += score
                print('"' + word + '" earned ' + str(score) +
                      ' points. Total: ' + str(total_score) + ' points')
                # Update hand and show the updated hand to the user
                hand = update_hand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(total_score) + ' points.')

# Problem #6: Playing a game
#
#
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using play_hand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using comp_play_hand.

    4) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    hand = {}
    while True:
        user_input = input("Enter a input n(for new hand) or r(to play last hand) or e(exit the game) \n ")
        if user_input == 'n':
            while True:
                input1 = input("Enter a input u(for user game) or c(computer game) \n")
                if input1 == 'u':
                    hand = deal_hand(HAND_SIZE)
                    play_hand(hand, word_list, HAND_SIZE)
                    break
                elif input1 == 'c':
                    hand = deal_hand(HAND_SIZE)
                    comp_play_hand(hand, word_list, HAND_SIZE)
                    break

        elif user_input == 'r':
            while True:
                input1 = input("Enter a input u(for user game) or c(computer game) \n")
                if input1 == 'u':
                    play_hand(hand, word_list, HAND_SIZE)
                    break
                elif input1 == 'c':
                    comp_play_hand(hand, word_list, HAND_SIZE)
                    break
        elif user_input == 'e':
            print("game over")
            break
        else:
            print("Input is invalid")
# Build data structures used for entire session and play game
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
