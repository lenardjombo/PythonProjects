'''
1.Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
'''
n = int(input('Enter value of n '))
m = int(input('Enter value of m ')) 
def is_multiple(n,m): 
    if n%m == 0: #Checking if n is a multiple of m
        return True
    else:
        return False
    
check_mulitple = is_multiple(n,m)
print(check_mulitple)

