def email_validation_with_retry():
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
            return {"status": "success", "email": email}
    return {"status": "failed", "attempts": 2}