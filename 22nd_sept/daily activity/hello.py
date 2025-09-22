print("Hello World")
def greet(User):
    return f"Hello {User}"
name = input("What is your name? ")
message = greet(name)
print(message)