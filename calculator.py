def add(x, y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

choice = input("enter choice (1: Add, 2: Subtract, 3: Multiply, 4: Divide): ")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

if choice == '1':
    print("result " + str(add(float(num1), float(num2)))
          )
    # choice == "2":
    # print("result " + str(sub(float(num1), float(num2)))
elif choice == '2':
    print("result " + str(sub(float(num1), float(num2))))
elif choice == '3':
    print("result " + str(mul(float(num1), float(num2))))
elif choice == '4':
    print("result " + str(div(float(num1), float(num2))))

else:
    print("Invalid choice")    