'''
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
'''

def reversed_list(list1):
    reversed_list = [] #Defining an empty list
    for i in range(0,len(list1)): #Accessing items in the list
        reversed_list.append(list1[len(list1)-i-1])
    return reversed_list
print(reversed_list([1,2,3,4,5,6]))
