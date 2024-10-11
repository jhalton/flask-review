# numbers = [1, 3, 5]
# doubled = [num * 2 for num in numbers]
# print(doubled) # prints [2, 6, 10]


friends = ["Scooby", "Shaggy", "Velma", "Fred", "Daphne"]
starts_s = [friend for friend in friends if friend.startswith("S")] 
#start with the thing you want to add, iterate, and your condition

print(starts_s) #prints ["Scooby", "Shaggy"]
