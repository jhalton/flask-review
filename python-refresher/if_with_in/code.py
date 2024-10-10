# movies_watched = {"Hocus Pocus", "Addams Family Values", "It"}
# user_movie = input("Enter something you've watched recently: ")

# if user_movie in movies_watched:
#     print(f"I've watched {user_movie} too")
# else:
#     print(f"I haven't watched that yet")


number = 7
user_input = input("Enter 'y' if you would like to play: ")

if user_input in ("y", "Y"): #But using .lower() on the user_input is a better approach
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("Off by one, my guy.")
    else:
        print("Wrongo!")
