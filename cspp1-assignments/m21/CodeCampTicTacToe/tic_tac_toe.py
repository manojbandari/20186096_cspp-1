def Winnner_check(matrix):
	a=0
	b=0
	for i in range(3):
		
		for j in range(3):
			if matrix[i][j] in 'ox.':
				if matrix[i][j] == 'o':
					a+=1
				elif matrix[i][j] =='x':
					b+=1
		if a==3 and b==3:
			return 'draw'


	for i in range(1):
			for j in range(3):
				if matrix[i][j]=='o' and matrix[i+1][j]=='o' and matrix[i+2][j]=='o':
					return 'o'
				elif matrix[i][j]=='x' and matrix[i+1][j]=='x' and matrix[i+2][j]=='x':
					return 'x'



def valid_game(matrix):
	a=0
	b=0
	for i in range(3):
		
		for j in range(3):
			if matrix[i][j] in 'ox.':
				if matrix[i][j] == 'o':
					a+=1
				elif matrix[i][j] =='x':
					b+=1


	return bool(((a<=5 and b<=4) or (a<=4 and b<=5)) and abs(a-b)<=1)



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
