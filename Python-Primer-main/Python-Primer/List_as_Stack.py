stack = []
limit = int(input("Enter Limit "))

def push():
  if len(stack) == limit:
    print("Stack is Full! ")
  else:
    element = input("Enter element ")
    stack.append(element)
    print(stack)

def pop():
  if len(stack) == 0:
    print("Cannot pop from an empty stack..Stack is empty ")
  else:
    popped = stack.pop()
    print("Element popped from stack, " ,popped)
    print(stack)

active = True
while active:
  print("Select operation 1.push 2.pop 3.quit")
  choice = int(input("Enter selected operation \t")
  if choice == 1:
    push()
  elif  choice  ==  2:
    pop()
  elif  choice  ==  3:
      break
  else  :
        print("Please enter a valid operation ")
print("The above program implements use of lists in python to implement user-defined data structures in python")
      
