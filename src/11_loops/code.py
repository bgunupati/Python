friends = ["Bharath", "Pavan", "Bhaskar", "Chakri", "Naresh", "Pradeep"]

for friend in friends:
    print(f"{friend} is my friend.")

for friend in range(4): # prints 0,1,2,3
    print(f"{friend} is my friend.")

grades = [85, 90, 78, 92, 88]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

average = total / amount
print("The average grade is:", average)

grades = [85, 90, 78, 92, 88]
total = sum(grades) # Use sum in the place of loop
amount = len(grades)

average = total / amount
print("The average grade is:", average)
