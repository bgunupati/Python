numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
doubled = [x * 2 for x in numbers]
print(doubled)

friends = ["Bharath", "Pavan", "Bhaskar", "Chakri", "Naresh", "Pradeep","Balaji"]
starts_s = [friend for friend in friends if friend.startswith("B")]
print(starts_s)

friends = ["Bharath", "Bhaskar", "Balaji"]
starts_b =[friend for friend in friends if friend.startswith("B")]

print(friends)
print(starts_b)
print(friends is starts_b)