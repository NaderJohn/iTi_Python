def email_validation(email):
    try:
        username, domain = email.split('@')
        z, y = domain.split('.')
        if z and y:
            return True
    except ValueError:
        print('Invalid email format ')
    return False


for i in range(2):
    email = input("Enter your email: ")
    if email_validation(email):
        print("Welcome!")
        break
else:
    
    raise ValueError("Email validation failed after 2 tries.")
