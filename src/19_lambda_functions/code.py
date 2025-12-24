def add(x, y):
    return x + y
print(add(2, 3))

add = lambda x, y: x + y
print(add(2, 3))

(lambda x, y: x + y)(2,3)

sequence = [1, 2, 3, 4, 5]

doubled = [x * 2 for x in sequence]
print(doubled)

def double(x):
    return x * 2

sequence = [1, 2, 3, 4, 5]
doubled = [double(x) for x in sequence]
print(doubled)


sequence = [1, 2, 3, 4, 5]
doubled = map(double, sequence)
print(doubled)  # This will print a map object
print(list(doubled))  # Convert map object to list to see the values

doubled = [(lambda x:x * 2)(x) for x in sequence]
print(doubled)

doubled = map((lambda x:x * 2), sequence)
print(list(doubled))    
