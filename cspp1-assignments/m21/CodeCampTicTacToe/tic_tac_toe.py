def Winnner_check():
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
				return False
	return bool(((a<=5 and b<=4) or (a<=4 and b<=5)) and a-b<=1)
	
def read_input():
	matrix = []

	for _ in range(3):
		matrix.append(input().split(" "))
	return matrix

def main():
	if is_valid(read_input()):
		Winnner_check(matrix)

	else:
		print("invalid game")
	




if __name__ == '__main__':
    main()
