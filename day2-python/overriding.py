class A():
    classVar = "Class A welcomes you"
    
    def __init__(self,jhgj,hfjf):
        self.instanceVar1 = "Intance variable 1 of class A welcomes you"
        self.unique = "Its a unique instance variable of class A"
        self.jhgj = jhgj
        self.hfjf = hfjf
        print("Print from A constructor")

class B(A):
    classVar = "Class B welcomes you"
    instanceVar1 = "hello from instance var in class B"
    
    def __init__(self):                                    #Overriding
        self.instanceVar1 = "Hello Mfs"
        self.uniqueB ="Unique from b"
        super().__init__(4325,435)                         #Calling constructor of A
        print("Print from B constroctor")
              
b = B()
print(b.instanceVar1)
print(b.hfjf)
print(b.uniqueB)