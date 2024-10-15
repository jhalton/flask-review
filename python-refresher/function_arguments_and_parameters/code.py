#variables passed when defining a function are called parameters. variables passed when calling a function are called arguments

def add(x,y):
    res = x + y
    print(res)

# add(5, 3)

def say_hello(name):
    print(f"Hello {name}")

# say_hello("Clarice")

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend/divisor)
    else:
        print("You fool!")

divide(dividend=10, divisor=0) #use keyword arguments wherever possible unless it's super obvious which thing is which
