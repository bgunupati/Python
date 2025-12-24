
friends = ["Alice", "Bob", "Charlie"]


def add_friend():
    friend_name = input("Enter the name of the friend to add: ")
    f = friends + [friend_name]  # This creates a new local 'friends' list
    print("Updated friends list:", f,friends)

add_friend()