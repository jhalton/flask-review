# def named(**kwargs):
#     print(kwargs)


# named(name="Freya", age=7)

# def named(name, age):
#     print(name, age)

# details = {"name": "Freya", "age": 7}

# named(**details)


def named(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, val in kwargs.items():
        print(f"{arg}: {val}")

print(print_nicely(name="Freya", age=7))


def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Freya", age=25)
