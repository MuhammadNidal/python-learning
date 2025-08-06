

# single inheritance mean single parent and single child




class Animal:
    def speak(self):
        print("we have some animals")

class Dog(Animal):
    def bark(self):
        return ("dog is also present")

d1=Dog()
d1.speak()
print(d1.bark())



# Mutiple inheritance

class Father:
    def __init__(self,name):
        self.name =name
        
class Mother:
    def __init__(self,age):
        self.age=age

class child(Father,Mother):
    def __init__(self, name,age,personal):
        self.name=name
        self.age=age
        self.personal=personal
        
c1=("nidal",22,"Muhammad Nidal")            
print(c1)
