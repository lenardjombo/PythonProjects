'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
'''

def sum_of_squares(n):
    n -= 1
    total = 0
    while n>0:
        total += n*n
        n -=1
    return total
n = int(input('Enter value of n \t'))
print(f'Sum of squares less than {n} is {sum_of_squares(n)}')