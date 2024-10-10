# number = 7

# while True:
#     user_input = input("Would you like to play? (Y/n) ")

#     if user_input == "n":
#         break

#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guessed correctly!")
#         break
#     elif abs(number - user_number) == 1:
#         print("Off by one, my guy.")
#     else:
#         print("Wrongo!")



# friends = ["Morticia", "Debbie", "Wednesday", "Gomez"]

# for friend in friends:
#     print(f"{friend} is my friend.")


grades = [35, 67, 98, 100, 100]
# total = 0
total = sum(grades)
amount = len(grades)

# for grade in grades:
#     total += grade 

print(total / amount)
