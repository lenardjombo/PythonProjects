'''
Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function.
'''
def sum_of_odd(n):
    return sum(
        [k*k for k in range(0,n) if k & 1 != 0 ]
        )
print(sum_of_odd(4))