'''
@author: manoj bandari
program for tic_tac toe game
'''
def Winnner_check(matrix):
    '''
    return result of the game
    '''
    a_count = 0
    b_count = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] in 'ox.':
                if matrix[i][j] == 'o':
                    a_count += 1
                elif matrix[i][j] == 'x':
                    b_count += 1
        if (a_count == 5 and b_count == 4) or (a_count == 4 and b_count == 5):
            return 'draw'
    a_count = 0
    b_count = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] in 'ox.':
                if matrix[i][j] == 'o':
                    a_count += 1
                elif matrix[i][j] == 'x':
                    b_count += 1
        if a_count == 3 and b_count == 3:
            return 'invalid game'

    for i in range(1):
        for j in range(3):
            if matrix[i][j] == 'o' and matrix[i+1][j] == 'o' and matrix[i+2][j] == 'o':
                return 'o'
            elif matrix[i][j] == 'x' and matrix[i+1][j] == 'x' and matrix[i+2][j] == 'x':
                return 'x'
    a_count = 0
    b_count = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] in 'ox.':
                if matrix[i][j] == 'o':
                    a_count += 1
                elif matrix[i][j] == 'x':
                    b_count += 1
        if a_count == 3:
            return 'o'
        elif b_count == 3:
            return 'x'

def valid_game(matrix):
    '''
    checking the game is valid or not
    return boolean values
    '''
    a_count = 0
    b_count = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] in 'ox.':
                if matrix[i][j] == 'o':
                    a_count += 1
                elif matrix[i][j] == 'x':
                    b_count += 1
    return bool(((a_count <= 5 and b_count <= 4) or (a_count <= 4 and b_count <= 5)) and abs(a_count - b_count) <= 1)

def is_valid(matrix):
    '''
    checking whether the input is right or wrong
    return boolean values
    '''
    for i in range(3):
        for j in range(3):
            if matrix[i][j] not in 'ox.':
                return False
    return True
def read_input():
    '''
    Taking the inputs from the user for matrix
    return matrix
    '''
    matrix = []
    for _ in range(3):
        matrix.append(input().split(" "))
    return matrix
def main():
    '''
    main function
    printing who is the winner
    invalid input if the input is wrong
    invalid game if the input entered is wrong
    '''
    matrix = read_input()
    if is_valid(matrix):
        if valid_game(matrix):
            print(Winnner_check(matrix))
        else:
            print("invalid game")
    else:
        print("invalid input")

if __name__ == '__main__':
    main()
