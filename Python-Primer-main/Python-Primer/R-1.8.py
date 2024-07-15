'''
Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for in-
dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?
'''
s = 'HelloWorld!'
n = len(s)
for k in range(-n, 0):
    print(s[k])


for j in range(-n, 0):
    print(s[j + n])