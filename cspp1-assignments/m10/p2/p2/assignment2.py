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

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
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
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True
    

def get_word_guessed(secret_word,letters_guessed):
  
    word = ""
    for i in secret_word:
        if i not in letters_guessed:
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
    s_new = ""
    string = "abcdefghijklmnopqrstuvwxyz"
    for i in string:
        if i not in letters_guessed:
            s_new = s_new + i
    return s_new


    

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

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
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    guess = 8
    letters_guessed=" "
    print(secretWord)
    while True:
        print("-------------------------------------------------")
        print("You have"+str(guess)+"guesses left.")
        print(get_available_letters(letters_guessed.split()))
        char=input("please guess a character: ")
        letters_guessed= letters_guessed+" "+ char
        if is_word_guessed(secretWord, letters_guessed.split()):
            print("good guess: ",get_word_guessed(secretWord,letters_guessed.split()))       
        else:
            print("Oops! That letter is not in my word:",get_word_guessed(secretWord,letters_guessed.split()))
            guess = guess - 1 #condition

        if get_word_guessed(secretWord,letters_guessed)==secretWord:
            print("Congratulations, you won!")
            break
        elif guess==0:
            print("Sorry, you ran out of guesses. The word was ",secretWord,".")
            break













































    # print("number of letters the secretWord contains", len(secret_word))
    # limit_guess=0
    # new_list=""
    # pd=0
    # k=0
    # while(limit_guess<=20):
    #     list1= input()
    #     print(is_word_guessed(secret_word, list1))
    #     print(get_word_guessed(secret_word,list1,new_list))
    #     print(get_available_letters(list1))




    #     if limit_guess>=len(secret_word):
    #         for i in range(len(new_list)): 
    #             if new_list[i] in secret_word:
    #                 pd = pd+1
    #         if pd>=len(secret_word):
    #             limit_guess =21
    #     limit_guess=limit_guess +1
        
    # for i in range(len(new_list)): 
    #     if new_list[i] in secret_word:
    #         k=k+1
    # if k>=len(secret_word):
    #     print("you won a game")
    #     print("The secret word is",secret_word)
    # else:
    #     print("you lost the game")
    #     print("The secret word is",secret_word)
        





def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
	and run this file to test! (hint: you might want to pick your own
	secretWord while you're testing)
	'''
	# secretWord = chooseWord(wordlist).lower()
	# hangman(secretWord)
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)

if __name__ == "__main__":
    main()
