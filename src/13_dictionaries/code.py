friends_ages = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35
}
friends_ages["David"] = 28
print(friends_ages)
print(friends_ages["Alice"])


friends =[
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

print(friends[1]["name"])


studnet_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
for student in studnet_attendance:
    print(f"{student}: {studnet_attendance[student]}%") 

for student, attendance in studnet_attendance.items():
    print(f"{student}: {attendance}%")

