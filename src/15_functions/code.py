def hello():
    print("Hello !")

hello()

def user_age_in_seconds():
    user_age = int(input("Enter your age in years: "))
    age_in_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is approximately: {age_in_seconds} seconds")

user_age_in_seconds()
