# x = 5, 11 #this is a tuple, and the parentheses are only necessary to tell Python that you want to group these as a tuple in another context

# a,b = 5,11

# people = [("Malcom", 54, "Architect"), ("Jude", 51, "Lawyer"), ("Willem", 53, "Actor"), ("JB", 53, "Artist")]

# for name, age, profession in people:
#     print(f"Name: {name}, Age: {age}, Profession: {profession}")

person = ("Jude", 53, "Lawyer")
name, __, profession = person
