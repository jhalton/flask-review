# name = input("Enter your name: ")
# print(name)

size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8
print(f"Your {square_feet} square foot house is {square_metres: .2f} in square meters")
