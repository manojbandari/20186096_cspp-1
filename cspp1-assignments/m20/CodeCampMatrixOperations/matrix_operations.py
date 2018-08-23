
# def loop(count):
#     a=0
#     for j in range(len(m2)):
#         a+=int(m1[i][j])*int(m2[j][0]) 
#             mul_1m.append(a)
# def loop(mul_1m,count):
#     a=0
#     for j in range(len(m2)):
#         a+=int(m1[i][j])*int(m2[j][count]) 
#             mul_1m.append(a)


def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    mul_2m=[]
    try:
        if len(m1[0])==len(m2[1]):
            for i in range(len(m1)):
                mul_1m=[]
                a=0
                count=0
                for j in range(len(m2)):
                    a+=int(m1[i][j])*int(m2[j][0])
                mul_1m.append(a)
                if len(m2)>=2:
                    a=0
                    for k in range(len(m2)):
                        a+=int(m1[i][k])*int(m2[k][1])
                        count+=1
                    mul_1m.append(a)
                if len(m2)>=3:
                    a=0
                    for n in range(len(m2)):
                        a+=int(m1[i][n])*int(m2[n][2])
                        count+=1
                       
                    mul_1m.append(a)
                if len(m2)>=4:
                    a=0
                    for m in range(len(m2)):
                        a+=int(m1[i][m])*int(m2[m][3])
               
                    mul_1m.append(a)
                    
                    

                mul_2m.append(mul_1m)
        else:
            print("Error: Matrix shapes invalid for mult")
            return None
    except:
        return "Error: Invalid input for the matrix"
    return mul_2m

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    
    
    add_2m=[]

    try:
        if len(m1[1])==len(m2[0]):
            for i in range(len(m1)):
                add_m = []
                for j in range(len(m2[0])):
                    add_m.append(int(m1[i][j])+int(m2[i][j]))
            #add_m.append(add_m)
                add_2m.append(add_m)
        else:
            print("Error: Matrix shapes invalid for addition")
            return None
    except:
            return "Error: Invalid input for the matrix"
    

        # add_m[i][1]=m1[i][1]+m2[i][1]
        # add_m[i][2]=m1[i][2]+m2[i][2]
    

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
    m1=read_matrix()
    m2=read_matrix()
    # read matrix 2
    # print(m1)
    # print(m2)
    # print(m1)
    # print(m2)
    add_result = add_matrix(m1, m2)
    
    # # add matrix 1 and matrix 2
    mult_result=mult_matrix(m1, m2)
    if add_result==mult_result:
        print(add_result)
    else:
        print(add_result)
        print(mult_result)
    # multiply matrix 1 and matrix 2

if __name__ == '__main__':
    main()
