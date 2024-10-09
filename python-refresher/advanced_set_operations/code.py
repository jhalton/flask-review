#Sets are great for comparing data

friends = {"Don", "Roger", "Joan"}
abroad = {"Don", "Roger"}

local_friends = friends.difference(abroad) #Gives you the elements not in the friends set when compared to abroad
print(local_friends)

art = {"James", "Jeanette", "Russ", "Jon"}
science = {"Jeanette", "James", "Ian", "Marcus"}

both = art.intersection(science) #Intersection gives you the elements that are present in both sets
print(both)
