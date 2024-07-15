'''

Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.

'''
def sum_of_squares_of_postive_integers_odd(n):
    n-=1
    total = 0
    while n>0:
        if n & 1 == 1: #checking if n is odd
            total += n*n
        n-=1
    return total

print(sum_of_squares_of_postive_integers_odd(4))