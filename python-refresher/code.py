#Defining variables, no declarative word
x = 15 
price = 9.99

discount = 0.2

result = price * (1 - discount)

print(result)


name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)

print(with_name)

longer_phrase = "Hello, {}. Today is {}"
formatted = longer_phrase.format("Morticia", "Wednesday")
print(formatted)
