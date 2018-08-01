'''
@author : manojbandari
program to print sum of 1 to n integers
'''

N = int(input())
I = 1
SUM = 0
while I <= N:
    SUM += I
    I += 1
print(SUM)
