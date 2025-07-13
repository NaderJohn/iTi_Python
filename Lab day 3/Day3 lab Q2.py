#Nader John 

emails = [
    "ali@gmail.com",
    "sara@yahoo.com",
    "mohamed@outlook.com",
    "noha@iteg"
]

def validaion(email):
    if '@' in email and '.' in email:     
        username , domain = email.split('@')
        if username and domain :
            z,y = domain.split('.')
            if z and y:
                return True
    else:
        return False
    

results = filter(validaion,emails)

print(list(results))