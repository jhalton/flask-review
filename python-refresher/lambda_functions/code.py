#almost exclusively used to take in inputs and return outputs. they are not used to perform actions
#they are often used without giving them a name
#without a name, you have to use it the same line you are defining it

# def add(x,y):
#     return x + y

add = lambda x, y: x + y

print(add(5,7))
print((lambda x,y: x + y)(20, 13)) #not common

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
# doubled = [double(x) for x in sequence]
# print(doubled)
doubled = list(map(lambda x: x * 2, sequence))#do this to this thing
print(doubled)
