s = set((234, 23423, 4, 23, 41))
s.add(100)
s.add("set1")

s2 = {"shrey", 99, True}
s2.add("abc")
try:
    s2.remove(100)
except:
    print("element not found")

print("S2: ", s2)
print("\ns: ", s)
s.pop()
print("s: ", s)

s2.discard("shreyJAin")
print("s2: ", s2)

l = [23,4,23,5]
s.update(l)
print("s: ", s)