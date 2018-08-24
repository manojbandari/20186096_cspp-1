def Winnner_check(matrix):
	for i in matrix:
		for j in i:
			if j == 'o':
				count_a+=1
			if j =='x':
				count_b+=1

		if count_a==count_b:
			print(draw)
		elif count_a==3:
			print('o')

		elif count_b==3:
			print('x')


def valid_game(matrix):
	a=0
	b=0
	for i in range(3):
		
		for j in range(3):
			if matrix[i][j] == 'o':
				a+=1
			elif matrix[i][j] =='x':
				b+=1


	return bool(((a<=5 and b<=4) or (a<=4 and b<=5)) and 0>=abs(a-b)<=1)



def is_valid(matrix):
	
	for i in range(3):
		for j in range(3):
			if matrix[i][j] not in 'ox.':
				return False
	return True
 
	
def read_input():
	matrix = []

	for _ in range(3):
		matrix.append(input().split(" "))
	return matrix

def main():
	matrix=read_input()
	if is_valid(matrix):
		if valid_game(matrix):
			print(Winnner_check(matrix))
		else:
			print("invalid game")
	else:
		print("invalid input")
	




if __name__ == '__main__':
    main()
