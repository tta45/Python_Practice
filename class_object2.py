class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def myfunc(self):
        print(self.firstname, self.lastname)
        
class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
     
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "For completing your graduation in", self.graduationyear)   
        
mehedi = student("Mehedi", "Hasan", 2024)
m2 = person("Mehedi", "Hasan")
m2.myfunc()
mehedi.welcome()
