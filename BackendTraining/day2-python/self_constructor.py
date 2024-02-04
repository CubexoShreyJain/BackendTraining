class Employee():                    #Yaha pe apan koi parameters set nai krte fir bhi vo constructor ke parameters ko leta h
    
    address = "Ghanta Ghar"                      #Class variable kisko use toh saare objects kr skte h pr chuu koi nai skta
    
    def __init__(self,name,salary):             #Bs iss chutiya si cheez ko bolte h constructor 
        super().__init__()                      #
        self.name = name
        self.salary = salary
        
    def printmf(self):
        print(self.__dict__)
        
    @classmethod                         ##Class method : These are used to play with whole class
    def change_address(cls,new_add):     ## jaise,normal function toh saare objects ke liye alag alag hote h
        cls.address = new_add            ## Aur koi bhi object class variable ko change nai kr skta, toh tb 
                                         ## Kaam aati h ye class method Aur hn decorator toh yaad hi hoga
        
rohan = Employee("Rohan",1000)
rohan.salary = 10000
# rohan.address = "afdsafs"
rohan.printmf()
print(rohan.address)

shrey = Employee("Shrey",1000000000)
shrey.printmf()

print("Shrey address ",shrey.address)
shrey.change_address("Rungta Compound")         #Changes whole variable, address. For everyone
print("Shrey address ",shrey.address)
print(rohan.address)
