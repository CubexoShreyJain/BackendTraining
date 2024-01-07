from collections import deque

class Stack():
    def __init__(self):
        self.stack = deque()
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        self.stack.pop()
    def top(self):
        return self.stack[-1]
    def isEmpty(self):
        return not (bool(len(self.stack)))

if __name__ == '__main__':
    myStack  = Stack()
    print("is Empty before: ", myStack.isEmpty())
    myStack.push(5)
    myStack.push(43)
    myStack.push(645)
    myStack.push(436)
    print("Is empty: ", myStack.isEmpty())
    print("Top of stack: ", myStack.top())
    x = input("Enter number to push: ") 
    myStack.push(x)
    print("Top now: ", myStack.top())
    myStack.pop()
    myStack.pop()
    print("Top after poping: ", myStack.top())