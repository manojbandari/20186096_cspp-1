'''
@author : manojbandari
compare the two variables and display the output based on the condtions
'''
VARA = input()
VARB = input()
if(isinstance(VARA, str) or isinstance(VARB, str)):
    print("string involved")
elif VARA > VARB:
    print("bigger")
elif VARA == VARB:
    print("equal")
else:
    print("smaller")
