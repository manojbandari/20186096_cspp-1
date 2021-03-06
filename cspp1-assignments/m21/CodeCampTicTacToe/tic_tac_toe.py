'''
@author: manoj bandari
program for tic_tac toe game
'''
def winner_check(matrix):
    '''
    return result of the game
    '''
    if  winner_game(matrix) == 'draw':
        return 'draw'
    if completed_game(matrix) == 'invalid game':
        return 'invalid game'
    c_temp = winner_vertical(matrix)
    if c_temp == 'x':
        return 'x'
    if c_temp == 'o':
        return 'o'
    d_temp = winner_horizontal(matrix)
    if d_temp == 'x':
        return 'x'
    if d_temp == 'o':
        return 'o'
    return 'none'
def winner_game(matrix):
    '''
    checking draw or not
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
    return 'none'
def completed_game(matrix):
    '''
    checking whether who won the game
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
        if a_count == 3 and b_count == 3:
            return 'invalid game'
    return 'none'
def winner_vertical(matrix):
    '''
    checking vertically
    '''
    for i in range(1):
        for j in range(3):
            if matrix[i][j] == 'o' and matrix[i+1][j] == 'o' and matrix[i+2][j] == 'o':
                return 'o'
            if matrix[i][j] == 'x' and matrix[i+1][j] == 'x' and matrix[i+2][j] == 'x':
                return 'x'
    return 'none'
def winner_horizontal(matrix):
    '''
    checking horizontally
    '''
    a_count = 0
    b_count = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] in 'ox.':
                if matrix[i][j] == 'o':
                    a_count += 1
                if matrix[i][j] == 'x':
                    b_count += 1
        if a_count == 3:
            return 'o'
        if b_count == 3:
            return 'x'
    return 'none'
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
    return bool(((a_count <= 5 and b_count <= 4) or
                 (a_count <= 4 and b_count <= 5)) and abs(a_count - b_count) <= 1)

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
            print(winner_check(matrix))
        else:
            print("invalid game")
    else:
        print("invalid input")

if __name__ == '__main__':
    main()
