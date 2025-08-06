# def add(x, y):
#     return x + y
# def sub(x,y):
#     return x - y
# def mul(x,y):
#     return x * y
# def div(x,y):
#     if y == 0:
#         return "Error! Division by zero."
#     return x / y

# choice = input("enter choice (1: Add, 2: Subtract, 3: Multiply, 4: Divide): ")
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")

# if choice == '1':
#     print("result " + str(add(float(num1), float(num2)))
#           )
#     # choice == "2":
#     # print("result " + str(sub(float(num1), float(num2)))
# elif choice == '2':
#     print("result " + str(sub(float(num1), float(num2))))
# elif choice == '3':
#     print("result " + str(mul(float(num1), float(num2))))
# elif choice == '4':
#     print("result " + str(div(float(num1), float(num2))))

# else:
#     print("Invalid choice")    



import random

def guess_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("🎯 Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("📉 Too low! Try again.")
            elif guess > number_to_guess:
                print("📈 Too high! Try again.")
            else:
                print(f"✅ Correct! You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

guess_game()
