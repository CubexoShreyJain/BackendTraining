from queue import Queue

q = Queue(maxsize=5) # By default, max size is 0
print("is empty?: ", q.empty()) # Total size
print("Size: ", q.qsize()) # Current size
print("MAx Size: ", q.maxsize)
# print("len: ", len(q)) # dosen't work
q.put(5)
q.put(10)
q.put(12)
print("is full?: ",  q.full())
q.put(13)
q.put(14)
print("isempty?: ", q.empty())
print("is full?: ",  q.full())
# q.put(50) #Will wait till queue get's some space
# q.put_nowait(50) #Raise full error
print("Element on top: " , q.get()) # simultaniously remove element
print("Element on top: " , q.get()) # Won't throw error if empty, instead, wait till it receives
print("Element on top: " , q.get()) # Won't throw error if empty, instead, wait till it receives
print("Element on top: " , q.get()) # Won't throw error if empty, instead, wait till it receives
# print("Element on top: " , q.get()) # Won't throw error if empty, instead, wait till it receives
# print("Element on top: " , q.get()) # Won't throw error if empty, instead, wait till it receives
# q.put(101) # Won't run if above line is uncommented as, it would wait till an element to arrive in terminal only.
print("Element on top: " , q.get_nowait()) #Remove element but will throw empty error, if no element inside
# print("Element on top: " , q.get_nowait())
# print("Element on top: " , q.get_nowait())


