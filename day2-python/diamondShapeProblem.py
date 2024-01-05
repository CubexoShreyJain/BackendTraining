class A:
    classVar = "class variable of A"
class B(A):
    # classVar = "class variable of B"
    whfd= 234                                         #Now according to inheritance rule if variable not found in B it must see in A
   
class C(A):
    # classVar = "class variable of C"                  #But instead of going to A it first came in C then goes to A
    pass
class D(B,C):
    pass                                                #/this confusion is known as dimond shape problem
    # classVar = "class variable of D"
    
d = D()
print (d.classVar)