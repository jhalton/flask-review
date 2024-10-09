print(5 == 5) #exactly equal
print(5 == "5") 
print(10 != 10)

# Comparisons: ==, !=, >, <, >=, <=

friends = ["Joan", "Betty"]
abroad = ["Joan", "Betty"]

print(friends == abroad) # Comparing lists (a cool thing you can do in Python that you can't do in JavaScript)
                         # Checking to see whether these elements HAVE the same thing (TRUE)
print(friends is abroad) # Checking to see whether these elements ARE the same thing (FALSE)

# Recommended to almost never use is, rather == is preferred
