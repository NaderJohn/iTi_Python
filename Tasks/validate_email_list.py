emails = [
    "ali@gmail.com",
    "sara@yahoo.com",
    "mohamed@outlook.com",
    "noha@iteg"
]

def validate_email_list():
    def validation(email):
        if '@' in email and '.' in email:     
            username, domain = email.split('@')
            if username and domain:
                z,y = domain.split('.')
                if z and y:
                    return True
        return False
    
    return list(filter(validation, emails))