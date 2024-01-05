class Student :
    No_of_leaves = 10
    x= "BEST"
    
    def __init__(self, name, std, sec ):
        self.name = name
        self.std = std
        self.sec = sec
    
    def detail(self):
        return "Student's name is {}, studies in standard {}, in section {}".format(self.name, self.std, self.sec)
    
    @classmethod
    def insert(cls, all):
        return cls(*all.strip().split())        
    
    @staticmethod
    def warning():                                        #Since it doesn't depend on object and class and will remain same, 
        print("Warning : Fees will not be refunded.")            #no matter what, that's why its called static method
    
        
class Literature:
    No_of_leaves = 15
    dance = "Mcihal jackson"
    music = "ta rururu.."
    
    def __init__(self, dance, music ):
        self.music = music
        self.dance = dance
    
    def skills(self):
        return "Dances: {}\nMusic: {}".format(self.dance, self.music)
        
        
        
class Sport(Student):                                                      #Single inheritance
    No_of_leaves = 9
    # x= "Bad"
    
    def __init__(self, name, std, sec, sport):                
        super().__init__(name, std, sec)                  #Copies Parent constructor
        self.sport = sport
    
    def sportDetail(self):                                #Parent Class can't access this method while this class can access all the 
        return "Sports {} of class {} knows are {}".format(self.name, self.std, self.sport)                        #methods of class
        
    def printTest(self):
        print(f"X is a {self.x} boy.")
    
    
class AllRounder(Sport, Literature):                 #Multiple inheritance And also  multilevel inheritance as Student is parent class of Sport
        # x = "good"
        
        
        def coolBuddy(self):
            return f"{self.name} is a all rounder student which can dance {self.dance} on music {self.music} and also knows sports like {self.sport}"
    
    
# Shrey = Student.insert("Shrey 12 Sci")
# Rohan = Sport.insert("Rohan 12 Comm TT")
# print(Shrey.detail())
# print(Rohan.sportDetail())

Shrey = AllRounder.insert("Shrey 12 Sci TT")
print(Shrey.coolBuddy())

Shrey.printTest()