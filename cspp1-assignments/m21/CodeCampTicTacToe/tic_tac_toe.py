def count_val(matrix):
	for i in range(3):
		count_a=0
		count_b=0
		for j in range(3):
			
			if matrix[i][j] == 'o':
				count_a+=1
			elif matrix[i][j] =='x':
				count_b+=1
	return bool(((a<=5 and b<=4) or (a<=4 and b<=5)) and 0>=abs(a-b)<=1 or)
def Winnner_check(matrix):
	# for i in range(3):
	# 	count_aa=0
	# 	count_bb=0
	# 	for j in range(3):
			
	# 		if matrix[i][j] == 'o':
	# 			count_aa+=1
	# 		elif matrix[i][j] =='x':
	# 			count_bb+=1

	if count_val(matrix):

	
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
		
		if count_a==5 and count_b==4 or count_a==4 and count_b==5:
			return 'draw'
	
	return "invalid game"
		
		
	





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
		print(Winnner_check(matrix))

	else:
		print("invalid input")
	




if __name__ == '__main__':
    main()
