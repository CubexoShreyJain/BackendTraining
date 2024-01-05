class Employee():                    #Yaha pe apan koi parameters set nai krte fir bhi vo constructor ke parameters ko leta h
    
    address = "Ghanta Ghar"                      #Class variable kisko use toh saare objects kr skte h pr chuu koi nai skta
    
    def __init__(self,name,salary):             #Bs iss chutiya si cheez ko bolte h constructor 
        super().__init__()                      
        self.name = name
        self.salary = salary
        
    def printmf(self):
        print(self.__dict__)
        
    @classmethod                         ##Class method : These are used to play with whole class
    def change_address(cls,new_add):     ## jaise,normal function toh saare objects ke liye alag alag hote h
        cls.address = new_add            ## Aur koi bhi object class variable ko change nai kr skta, toh tb 
                                         ## Kaam aati h ye class method Aur hn decorator toh yaad hi hoga
        
         
    @classmethod                             #ye hota h alternative constructor
    def creating_new_object(cls,string):     #cls is mandetory
        # l = string.split("/")
        # return cls(l[0],l[1])
        
        return cls(*string.split())    ###Yemst cheez h yaad rakhna uper ki 2 line km kr di issne
        
    @staticmethod
    def hello(string):         #string is not mandetory
        print(f"HEllo my name is {string}")
        

rohan = Employee("Rohan",1000)

shrey = Employee("Shrey",1000000000)

rudra  = Employee.creating_new_object("RUDRA 2000")          #Creating new object with new method

shrey.hello("SHREY")