
def greet_decorator(func):
    def greeting(*args,**kwargs ):
        print("Hello, this is a greeting function.")
        func(*args, **kwargs)  # Call the original function
        print("Goodbye, this is the end of the greeting function.")
    return greeting

@greet_decorator
def hello():
    print("Hello, world!")

@greet_decorator
def add(x, y):
    return x + y

print(add(2, 3))  # This will not be decorated
hello()  # Calling the decorated function