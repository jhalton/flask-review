from operator import itemgetter

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
# print(result)


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

friends = [
    {"name": "Jude St. Francis", "age": 34},
    {"name": "Willem Ragnarsson", "age": 36},
    {"name": "Malcom Irvine", "age": 36},
]

def get_friend_name(friend):
    return friend["name"]

# print(search(friends, "Malcom Irvine", get_friend_name))

# #can also write as lambda function
# print(search(friends, "Jude St. Francis", lambda friend: friend["name"]))

# print(search(friends, "JB", get_friend_name))
print(search(friends, "Willem Ragnarsson", itemgetter("name")))
