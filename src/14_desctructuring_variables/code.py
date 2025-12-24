t = (5, 11)
x, y = t
print(x, y)

studnet_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
 
print(list(studnet_attendance.items()))

for t in studnet_attendance.items():
    print(t)    

for student, attendance in studnet_attendance.items():
    print(f"{student}: {attendance}%")


people = [
    ("Alice", 30, "New York"),
    ("Bob", 25, "Los Angeles"),
    ("Charlie", 35, "Chicago")]

for name, age, city in people:
    print(f"{name} is {age} years old and lives in {city}.")


person = {"Alice", 30,"New York"}

name,_,city = person
print(name, city)

*head, tail = [1,2,3,4,5]
print(head)
print(tail)