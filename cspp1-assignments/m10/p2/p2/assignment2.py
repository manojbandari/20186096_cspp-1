'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord
the user is to guess. This starts up an interactive game of Hangman between
the user and the computer. Be sure you take advantage of the three helper functions,
isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # wordlist: list of strings
    word_list = line.split()
    print("  ", len(word_list), "words loaded.")
    return word_list
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE..
    #if new_list in secret_word:
     #   return "won the game"
    count = 0
    for i in letters_guessed:
        if i not in secret_word:
            count = count+1
        else:
            count = 1
    if count == 1:
        return True
    return False
def get_word_guessed(secret_word, letters_guessed):
    '''
    guess function
    '''
    word = ""
    for i in secret_word:
        if i not in str(letters_guessed):
            word = word + "_"
        else:
            word = word + i
    return word

def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s_new = " "
    string = "abcdefghijklmnopqrstuvwxyz"
    for i in string:
        if i not in letters_guessed:
            s_new = s_new + i
    return s_new

def choose_word(word_list):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
WORD_LIST = load_words()

def hang_man(secret_word):
    '''
    secretWord: string, the secret word to guess

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    guess = 8
    letters_guessed = " "
    print(secret_word)
    while True:
        print("-------------------------------------------------")
        print("You have  " + str(guess) + " guesses left.")
        print(get_available_letters(letters_guessed))
        char = input("please guess a character: ")
        if char in letters_guessed:
            print("Oops! You've already guessed that letter:",
                  get_word_guessed(secret_word, letters_guessed.split()))
            letters_guessed = letters_guessed+""+char
        else:
            letters_guessed = letters_guessed+" "+ char
            if is_word_guessed(secret_word, letters_guessed.split()):
                print("good guess: ", get_word_guessed(secret_word, letters_guessed.split()))
            else:
                print("Oops! That letter is not in my word:",
                      get_word_guessed(secret_word, letters_guessed.split()))
                guess = guess - 1

            if get_word_guessed(secret_word, letters_guessed) == secret_word:
                print("Congratulations, you won!")
                break
            elif guess == 0:
                print("Sorry, you ran out of guesses. The word was ", secret_word, ".")
                break
def main():
    '''
    Main function for the given program
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    # secretWord = chooseWord(wordlist).lower()
    # hangman(secretWord)
    secret_word = choose_word(WORD_LIST).lower()
    hang_man(secret_word)

if __name__ == "__main__":
    main()
