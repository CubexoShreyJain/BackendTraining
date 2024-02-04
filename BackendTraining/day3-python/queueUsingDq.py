from collections import deque 

class Queue():
    def __init__(self):
        self.queue = deque()
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        self.queue.popleft()
    def top(self):
        return self.queue[0]
    def isEmpty(self):
        return not (bool(len(self.queue)))



if __name__ == '__main__':
    myqueue  = Queue()
    print("is Empty before: ", myqueue.isEmpty())
    myqueue.enqueue(5)
    myqueue.enqueue(43)
    myqueue.enqueue(645)
    myqueue.enqueue(436)
    print("Is empty: ", myqueue.isEmpty())
    print("Top of queue: ", myqueue.top())
    x = input("Enter number to enqueue: ") 
    myqueue.enqueue(x)
    print("Top now: ", myqueue.top())
    myqueue.dequeue()
    myqueue.dequeue()
    print("Top after dequeueing: ", myqueue.top())
    