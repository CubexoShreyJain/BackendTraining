class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self, data = 0):
       self.head = Node(data)
       self.tail = self.head
       
    def setNext(self, data):
        newNode = Node(data)
        self.tail.next  = newNode
        self.tail = newNode
        
    def display(self):
        temp = self.head
        while temp.next != None:
            print(temp.data)
            temp = temp.next
        
        
if __name__ == '__main__':
    l = LinkedList(99)
    l.setNext(100)
    l.setNext(101)
    l.setNext(102)
    l.setNext(103)
    l.display()