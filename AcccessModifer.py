# public

class Modifer:
    def __init__(self):
        self.name= "ndial"
        


a=Modifer()
print(a.name)



# private 
# only accessible in python
class Modifer:
    def __init__(self):
        self.__name= "ndial"
        


a=Modifer()
# print(a.__name)
print(a._Modifer__name)



class MyClass:
    def __init__(self):
        self.name = "Public Variable"  # Public

    def public_method(self):
        return "This is a public method"


obj = MyClass()
print(obj.name)           # Accessible
print(obj.public_method())  # Accessible









class MyClass:
    def __init__(self):
        self._data = "Protected Variable"  # Protected

    def _protected_method(self):
        return "This is a protected method"


obj = MyClass()
print(obj._data)              # Accessible, but discouraged
print(obj._protected_method())  # Accessible, but discouraged





class MyClass:
    def __init__(self):
        self.__secret = "Private Variable"  # Private

    def __private_method(self):
        return "This is a private method"


obj = MyClass()

# print(obj.__secret)  # Error: AttributeError

# Access through name mangling
print(obj._MyClass__secret)           # Accessible (but not recommended)
print(obj._MyClass__private_method()) # Accessible (but not recommended)




