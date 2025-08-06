# # Variables and Data Types

# Name = "Muhammad nidal"
# age = 20
# hobbies = ["reading", "coding", "gaming"]
# height = 2.1

# print(f"Name: {Name}")
# print(f"Age: {age}")

# # Comments
# # single line comment
# """   
# This is a multi-line comment
# You can write multiple lines here      
# """

# # . Basic Operators


# a=30
# b=10


# c=a*b
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)
# print(a%b)




# # Comparison Operators:

# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

# """
# x == y  # Equal to
# x != y  # Not equal to
# x > y   # Greater than
# x < y   # Less than
# x >= y  # Greater than or equal to
# x <= y  # Less than or equal to  

# """

# # Logical Operators

# a=100
# b=200
# print(a<b and a<b)
# print(a>b or a<b)
# print( not a>b)

# # Control Flow (if, else, elif)
# age = 18

# if age >20:
#    print("you are adult not yet")
# elif age < 20:
#    print("you are adult")
# else:
#    print("you are elgible")   


# vote ="you are good"
# if vote == "you are 111good":
#    print("you are correct")
# elif vote == "you are not good":
#    print ("you are wrong")
# else:
#    print("you are totally incorrct")     


 
# # Input and Output
# name  = input("Enter your name: ")
# age =  int(input("Enter your age: "))
# # print( "your name is", name, "and your age is ",age)
# # print(f"{name} is {age} years old.")
# print("Hello, {}! You are {} years old.".format(name, age))



# # Functions

# def nationality(name):
#    print("country belong")
#    print(f"{name} is from Pakistan")
# nationality("ali")

# def add_number(a,b):
#    return a+b
# print(add_number(11,11))



# # loops
# fruits = ["apple","banna","manog","orange"]
# for wish in fruits:
#   print(wish)
# for i in range(10):
#   print(i)

# # while loop

# count =12
# while count <20:
#    print(count)
#    count+=2

# name ="nidal"

# while name == ["nidal","kamran","khan"]:
#    print(name)
# else :
#    print("you are wrong")




   # list and Tuples

      # Lists  are mutable, meaning you can change their content.
# my_list = [1, 2, 3, 4, 5, "apple" , "banana ","orange"]
# print(my_list) 
# 🔷 1. List Slicing

# Edit
# my_list = [10, 20, 30, 40, 50]

# print(my_list[1:4])   # [20, 30, 40]
# print(my_list[:3])    # [10, 20, 30]
# print(my_list[-2:])   # [40, 50]
# # properties of list
# my_list.append("grape")
# print(my_list)

# my_list.remove("banana ")
# print(my_list)

# my_list.insert(2, "kiwi")
# print(my_list) 

# my_list.sort()
# 
# print(my_list) 

# my_list.reverse()   
# print(my_list) 

# # del my_list[3]
# print(my_list)

# my_list.pop(2)
# print(my_list) 

# print(len(my_list))  # Length of the list

# print(len(my_list))  # Length of the list


# # shallow copy vs deep copy

# # shallow copy
# x : list[str] = ['a','b','c']
# y = x # shallow copy
# print(id(x))
# print(id(y))
     

# x.append('d')
# print("x: ",x)
# print("y: ",y)
     
     
# characters = ['a','z','b']
# characters.reverse()
# print(characters)

# y.append('e')
# print(x)
# print(y)
     

# # deep copy
# x: list[str] = ['a', 'b', 'c']
# y = x.copy()        # Deep copy by copy() method
# x.append('d')
# print("x:", x)
# print("y:", y)

# print(id(x), id(y))
     

# x.append('e')
# print("x:", x)
# print("y:", y)
     

# z = x[:] # another way of Deep copy by slice
     

# print(id(x))
# print(id(z))
     

# z.append('e')
# print(z)
# print(x)
     

# # create new list
# x : list[str] = ['a','b','c']
# print(id(x))
# x = ['d','e','f']
# print(id(x))
# # print(x)
     
# # extend()
# # Supply the List to be extended


# arr1: list[int] = [1,2,3]
# a : list[int] = [4,5,6]
# arr1.extend(a)
# print(arr1)# 6 items
# print(a)# 3
# # print(id(a))
     
# # clear()

# a.clear()
# print(a)
# # print(id(a))
     
# # Time to Ask


# students = ["Ahmad", "Ali", "Kashif"]

# # Using clear()
# print(id(students))  # Same ID?, list cleared in place. Before
# students.clear()
# print(id(students))  # Same ID?, list cleared in place. After
# students.append("Usman")
# print(id(students))

# # Reassigning to empty list
# students = ["Ahmad", "Ali", "Kashif"]
# # print(id(students))
# students= []
# # print(id(students))




# # My tuple

# my_tuple = (1,2,3,4,2,2,2,3,5, "apple", "banana", "orange")
# print(my_tuple)

# # Properties of tuple
# print(my_tuple[1])
# print(my_tuple[2:5])  # Slicing the tuple
# print(my_tuple.count(2))  # Count occurrences of an element
# print(my_tuple.index("banana"))  # Find the index of an element
# another_tuple= (6, 7, 8)
# combined_tuple = my_tuple + another_tuple
# print(combined_tuple)  # Concatenating tuples




# # dir([object])
# x=[1, 2, 3, 4, 5]
# print(dir(x))  # List of methods and attributes for the list object

# x=(1, 2, 3, 4, 5)
# print(dir(x))







# # match case
# x = 11
# match x:
#       case 1:
#             print("x is 1")         
#       case 2:
#             print("x is 2")
#       case 3:
#             print("x is 3")            
#       case _:
#             print("x is something else")        
# # This is a simple match case example


# # Ternary operator

# wheather = input("enter value")
# message = "go for the walk"if wheather == "sunny" else "read a book"
# print(message)


# value = input("enter value 2")
# value1="if value is 100 then show wrong" if value == 100 else "you are good"
# print(value1)



# # Advanced Techniques
# # Nested Conditional Statements
# # Nest conditions for more complex decision-making.


# is_member = True
# purchase_amount = 200

# if is_member:
#     if purchase_amount > 200:
#         print("You qualify for a 10% discount!")
#     else:
#         print("Spend more to qualify.")
# else:
#     print("Join as a member for discounts!")



# # Key Differences Between == and is
# # == compares the values of two objects to see if they are equal.
# # is compares the identities of two objects to see if they refer to the same object in memory.
# # Example:

# x = [1, 2, 3]
# y = [1, 2, 3]
# print(id(x))
# print(id(y))
     
# 132799432089280
# 132799444105600

# print(x == y)  # Output: True (values are equal)
# print(x is y)  # Output: False (different objects in memory)
     
# True
# # False



# # f string in python


# name = "nidal"
# age = 20
# print(f"My name is {name}{age}")

# txt= "Hello, my name is {name} and I am {age} years old."
# print(txt.format(name=name, age=age))



# # Doc string in python

# def greet(name):
#       """
#       This function greets the person with the provided name.
#       :param name: str - The name of the person to greet.
#       :return: None
#       """
#       print(f"Hello, {name}!") 
# greet("Nidal")     
# print(greet.__doc__)  # Accessing the docstring of the function




# # Set in python
# my_set = {1, 1,2,3,2, 3, 4, 5, "apple", "banana", "orange"}
# print(my_set)

# print(type(my_set))  # Output: <class 'set'>

# set1 = {}
# print(type(set1))  # Output: <class 'dict'> (empty dictionary, not a set)


# # Set Operations
# set_a = {1, 2, 3,4,5,6,7}
# set_b = {3, 4, 5}
# print(set_a.union(set_b))  # Union: {1, 2, 3, 4, 5}
# print(set_a.intersection(set_b))  # Intersection: {3, 4, 5}
# print(set_a.symmetric_difference(set_b))  # Symmetric Difference: {1, 2, 6, 7}
# print(set_a.difference(set_b))  # Difference: {1, 2, 6, 7}
# print(set_b.issubset(set_a))  # Check if set_b is a subset of set_a: True
# print(set_a.issuperset(set_b))  # Check if set_a is a superset of set_b: True

# # Set Comprehension
# c = set_a.add(8)  # Adding an element
# print(c)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}   
# # Removing an element
# set_a.remove(8)
# print(set_a)  # Output: {1, 2, 3, 4, 5, 6, 7}
# # Adding multiple elements
# set_a.update([9, 10])
# print(set_a)  # Output: {1, 2, 3, 4, 5, 6, 7, 9, 10}  
# # Checking if an element exists
# print(5 in set_a)
# # Output: True    
# # Iterating through a set
# set_a.clear()
# print(set_a)  # Output: set() (empty set after clearing)
# del set_a  # Deleting the set




# Decorators

# def greet(name):
#     return f"hello , {name}"

# greet_fuc =greet("nidal")
# print(greet_fuc)

# def greet1(name):
#     return f"hello,{name}"








# import

# import math

# print(math.sqrt(16))  # Returns the square root of 16

# from math import sqrt,pi
# print(sqrt(25))  # Returns the square root of 25
# print(pi)  # Returns the value of pi

# print(dir(math))  # Lists all the attributes and methods of the math module

# from calculator import add, sub, mul, div




print(int("123ac"))
