'''
@author : manojbandari
#Guess My Number Exercise
'''
def main():
    '''
    guess the number
    '''
    low_num = 0
    high_num = 100
    print("Please think of a number between 0 and 100!")
    print("Enter 'yes' if guess done, or 'h' if that (number > your guess ) else 'l' ")
    user_guess = 'low_num'
    while user_guess != 'yes':
        print("Is your secret number ", int((low_num+high_num)//2), "?")
        user_guess = input()
        if user_guess == 'l':
            low_num = ((low_num+high_num)//2)
        elif user_guess == 'h':
            high_num = ((low_num+high_num)//2)
    print(user_guess)


if __name__ == "__main__":
    main()
