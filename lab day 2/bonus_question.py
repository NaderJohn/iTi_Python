# Nader John 

while True:
    name = input("Enter your name: ")
    if name.isalpha():
        break
    else:
        print("Please enter only your name without numbers")

while True:
    email = input("Please enter your email: ")
    if "@" in email and "." in email:
        break
    else:
        print("Invalid email")

print("Your name is", name)
print("Your email is", email)