def add(x,y):
    print(x + y)
    return x + y


# add(5, 8)
# res = add(5, 8)
# print(res)


def divide(dividend, divisor):
    if divisor != 0:
        return dividend/divisor
    else:
        return "You can't divide by 0 you dumb-dumb"
    

res = divide(15, 3)
print(res)
