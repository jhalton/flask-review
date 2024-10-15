# friend_ages = {"Wednesday": 12, "Pugsley": 10, "Pubert": 1 }

# friend_ages["Thing"] = 100

# print(friend_ages)

# friends = [
#     {"name": "Victoria", "age": 25},
#     {"name": "Emma", "age": 20},
#     {"name": "Geri", "age": 28},
#     {"name": "Mel B", "age": 25},
#     {"name": "Mel C", "age": 24}
# ]

# print(friends[2]["name"])

coworker_attendance = {"Marcus": 99, "Owen": 60, "Russ": 85}

# for coworker in coworker_attendance:
#     print(f"{coworker}: {coworker_attendance[coworker]}")
for coworker, attendance in coworker_attendance.items():
    print(f"Can you believe {coworker} shows up to {attendance}% of their shifts?")


if "Harmony" in coworker_attendance:
    print(f"Harmony: {coworker_attendance['Harmony']}")
else:
    print(f"Harmony is no longer with us.")


attendance_values = coworker_attendance.values()
print(sum(attendance_values) / len(coworker_attendance)) 
