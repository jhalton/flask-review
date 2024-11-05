class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #print out a string of the object's information
    # def __str__(self):
    #     return f"Person {self.name}, {self.age} years old."
    
    #print out an unambiguous method of the object so you could recreate that object
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

jude = Person("Jude", 35)
print(jude)
