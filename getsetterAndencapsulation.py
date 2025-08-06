

# # get and set method in python



# class Student:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):  # getter
#         return self._name

#     @name.setter
#     def name(self, value):  # setter
#         if len(value) < 3:
#             print("Name must have at least 3 characters")
#         else:
#             self._name = value


# # Usage
# s = Student("Ali")

# print(s.name)     # Uses getter
# s.name = "Mo"     # Uses setter (fails validation)
# s.name = "Ahmad"  # Uses setter (valid)
# print(s.name)
# # 

# inheritance

class Employee:
    def __init__(self,name,mobileNumber):
        self.name = name
        self.mobileNumber=mobileNumber

    def showDetails(self):
        print(f"the personal information is {self.name} and mobile number is {self.mobileNumber}")

class Manager(Employee):
    def nidal(self):
        print("you are also good man")


e1=Employee("nidal","21211212")
e1.showDetails()    
e2=Manager("nidal","121212")
e2.nidal()                
        