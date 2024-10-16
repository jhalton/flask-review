users = [
    (0, "Jude", "ilovewillem"),
    (1, "Willem", "acting123"),
    (2, "Malcom", "franklloydwright"),
    (3, "JB", "artsyfartsy")
]

username_mapping = {user[1]: user for user in users} #for user @ idx 1, get all the user info for each user in users

print(username_mapping)
print(username_mapping["Jude"])
