class person:
    name="nidal"
    age=22
    mobileNumber=21212121

    def info(self):
        print(f"this is my information {self.age} and name is{self.name}")


a1=person()
a1.info()        
    


# constructor in python

class studentInformation:
    def __init__(self,name,age):
        self.name = name
        self.age =age
    def info(self):
        print(f"this is {self.name}and{self.age}years old")        
  
a2=studentInformation("nidal",11)  
a2.info()