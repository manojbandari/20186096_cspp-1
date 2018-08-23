
# def loop(count):
#     a=0
#     for j in range(len(m2_matrix)):
#         a+=int(m1_matrix[i][j])*int(m2_matrix[j][0]) 
#             mul_1m.append(a)
# def loop(mul_1m,i,m1_matrix,m2_matrix,count):
#     count+=1
#     if len(m2_matrix[0])>=count:
#         a=0
#         j=0
#         for j in range(len(m2_matrix)):
#             a+=int(m1_matrix[i][j])*int(m2_matrix[j][count-1]) 
#         mul_1m.append(a)

#     return mul_1m
def mult_matrix(m1_matrix, m2_matrix):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    #print(len(m1_matrix[0]),len(m2_matrix))
    mul_2m=[]
    try:
        if len(m1_matrix[0])==len(m2_matrix):
            for i in range(len(m1_matrix[0])):
                mul_1m=[]
                count=0
               # loop(mul_1m,i,j,m1_matrix,m2_matrix,count)
                #loop(loop(loop(loop(mul_1m,i,j,m1_matrix,m2_matrix,count),i,j,m1_matrix,m2_matrix,count),i,j,m1_matrix,m2_matrix,count),i,j,m1_matrix,m2_matrix,count)
                # loop(mul_1m,i,j,m1_matrix,m2_matrix,count)
                #loop(mul_1m,i,j,m1_matrix,m2_matrix,count)
                if len(m2_matrix[0])>=1:
                    a=0
                    for j in range(len(m2_matrix)):
                        a+=int(m1_matrix[i][j])*int(m2_matrix[j][0])
                    mul_1m.append(a)

                if len(m2_matrix[0])>=2:
                    a=0
                    for k in range(len(m2_matrix)):
                        a+=int(m1_matrix[i][k])*int(m2_matrix[k][1])  
                    mul_1m.append(a)
                
                if len(m2_matrix[0])>=3:
                    a=0
                    count+=1
                    for n in range(len(m2_matrix)):
                        a+=int(m1_matrix[i][n])*int(m2_matrix[n][2])   
                    mul_1m.append(a)
                if len(m2_matrix[0])>=4:
                    a=0
                    for m in range(len(m2_matrix)):
                        a+=int(m1_matrix[i][m])*int(m2_matrix[m][3])
                    mul_1m.append(a)
                    

                mul_2m.append(mul_1m)
        else:
            print("Error: Matrix shapes invalid for mult")
            return None
    except:
        return "Error: Invalid input for the matrix"

    return mul_2m

def add_matrix(m1_matrix, m2_matrix):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    
    
    add_2m=[]

    try:
        if len(m1_matrix[1])==len(m2_matrix[0]):
            for i in range(len(m1_matrix)):
                add_m = []
                for j in range(len(m2_matrix[0])):
                    add_m.append(int(m1_matrix[i][j])+int(m2_matrix[i][j]))
            #add_m.append(add_m)
                add_2m.append(add_m)
        else:
            print("Error: Matrix shapes invalid for addition")
            return None
    except:
            return "Error: Invalid input for the matrix"
    

        # add_m[i][1]=m1_matrix[i][1]+m2_matrix[i][1]
        # add_m[i][2]=m1_matrix[i][2]+m2_matrix[i][2]
    

    return add_2m
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix=[]
    matrix_size = input().split(",")
    for i in range(int(matrix_size[0])): 
        matrix.append(input().split(" "))
    return matrix


def main():
    
    

    # read matrix 1
    m1_matrix=read_matrix()
    m2_matrix=read_matrix()
    # read matrix 2
    # print(m1_matrix)
    # print(m2_matrix)
    # print(m1_matrix)
    # print(m2_matrix)
    # if add_matrix(m1_matrix, m2_matrix)==mult_matrix(m1_matrix, m2_matrix):
    #     print(mult_matrix(m1_matrix, m2_matrix))
    
    # else:
    a_add=add_matrix(m1_matrix, m2_matrix)
    print(a)
    b_mult=mult_matrix(m1_matrix,m2_matrix)
    if a_add==b_mult:
        c_temp=0
    else:
        print(b_mult)    
    # multiply matrix 1 and matrix 2

if __name__ == '__main__':
    main()
