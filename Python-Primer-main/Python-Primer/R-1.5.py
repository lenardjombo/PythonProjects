'''
Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python’s comprehension syntax and the built-in sum function.
'''

def sum_of_squares(n):
    return sum(
        [k * k for k in range(0, n)]
        )


print(sum_of_squares(7))