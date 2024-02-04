l = [i for i in range(10) if i%2 ==0] # all in once, consume more memory
g = (i for i in range(10) if i%2 ==0) # next element on demand, consume less memory

print(l)
print(g)
for j in g:
    print(j)