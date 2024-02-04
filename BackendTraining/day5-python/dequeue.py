from collections import deque

de = deque() #Empty queu
print("size of queu: ", len(de))
de.extend([12,3, 4,234,234,23,4,23,4])
print(de)
de.append(101)
de.appendleft(-1)
print("Append: ", de)
print("size of: ", len(de))

de.pop() 
print("After poping: ", de)

print("popingleft : ", de.popleft())

de2 = deque([x for x in range(10)])

print("new que: ", de2)
print("size of que: ", len(de2))

de2.insert(8, 5)
print("insertion: ", de2)
print("count: ", de2.count(5))
print("index of 5: ", de2.index(5))
print("index of 5 from to : ", de2.index(5, 6, 14))

de2.remove(5)
print("Removal: ", de2)
de2.reverse()
print("Reverse: ", de2)
de2.rotate(2)
print("Rotate by 2: ", de2)
de2.rotate(-3)
print("Rotate by -3: ", de2)

print("head: ", de2[0])
print("tail: ", de2[-1])
