# Exercise: PowerRecr
# Write a Python function, recurPower(base, exp), that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.


def recur_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if base==0 and exp==0:
        return "not defined"
    elif exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base*recur_power(base,exp-1)
    

def main():
    data = input()
    data = data.split()
    print(recur_power(float(data[0]),int(data[1])))   

if __name__== "__main__":
    main()