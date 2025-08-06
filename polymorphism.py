class cat:
    def speak(self):
        return "meow"
    
class Dog:
    def speak(self):
        return " bark"

for animal in (cat(),Dog()):
    print(animal.speak()) 


    


# Method overriding
class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        # super().start()  # Calls parent class method
        print("Car is ready to go")

e1 = Car()
e1.start()





class Greet:
    def say_hello(self, name=None):
        if name:
            print(f"Hello, {name}!")
        else:
            print("Hello!")

g = Greet()
g.say_hello()          # Output: Hello!
g.say_hello("Nidal")   # Output: Hello, Nidal!

       