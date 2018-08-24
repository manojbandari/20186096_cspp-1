def Winnner_check(matrix):
	for i in range(3):
		count_a=0
		count_b=0
		for j in range(3):
			
			if matrix[i][j] == 'o':
				count_a+=1
			elif matrix[i][j] =='x':
				count_b+=1
		if count_a==3 and count_b==3:
			if count_a==3:
	for i in range(1):
		for j in range(3):
			if matrix[i][j]=='o' and matrix[i+1][j]=='o' and matrix[i+2][j]=='o':
				return 'o'
			elif matrix[i][j]=='x' and matrix[i+1][j]=='x' and matrix[i+2][j]=='x':
				return 'x'
		
	for i in range(3):
		count_a=0
		count_b=0
		for j in range(3):
			
			if matrix[i][j] == 'o':
				count_a+=1
			elif matrix[i][j] =='x':
				count_b+=1
			if count_a==3:
				return 'o'
			elif count_b==3:
				return 'x'
			return "invalid game"
		

	
		
	if count_a==5 and count_b==4 or count_a==4 and count_b==5:
		return 'draw'
	
	
		
		
	





def is_valid(matrix):
	
	a=0
	b=0
	c=0
	for i in range(3):
		for j in range(3):
			if matrix[i][j] in 'ox.':
				if matrix[i][j]=='o':
					a+=1
				elif matrix[i][j]=='x':
					b+=1
				else:
					c+=1
			else:
				return "invalid input"


	return bool(((a<=5 and b<=4) or (a<=4 and b<=5)) and a-b<=1)
	
def read_input():
	matrix = []

	for _ in range(3):
		matrix.append(input().split(" "))
	return matrix

def main():
	matrix=read_input()
	if is_valid(matrix):
		print(Winnner_check(matrix))

	else:
		print("invalid game")
	




if __name__ == '__main__':
    main()
