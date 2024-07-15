'''
2.Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
'''

def is_even(k):
    '''
    In binary representation, the least significant bit (LSB) of an even number is 0.
    If k & 1 equals 0, then k is even (k ends in 0 in binary).
    If k & 1 equals 1, then k is odd (k ends in 1 in binary).
    '''
    if k & 1 == 0:
        return True
    else:
        return False
    
print(is_even(10))