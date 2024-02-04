class First_Class():
    pass

a = First_Class()
a.id = 234
b = First_Class()
b.id = "asdf"
print(a.id,b.id) 
