'''
@author : manojbandari
program to print sum of 1 to n integers
'''
#using while loop
# N = int(input())
# I = 1
# SUM = 0
# while I <= N:
#   SUM += I
#  I += 1
# print(SUM)

#using for loop
SUM = 0
N = int(input())
for I in range(1, N + 1):
    SUM += I
print(SUM)
