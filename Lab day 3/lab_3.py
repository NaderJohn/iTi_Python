emails = [
    "ali@gmail.com",
    "sara@yahoo.com",
    "mohamed@outlook.com",
    "noha@iteg"
]

# def email_validaion(email):
#     if '@' in email and '.' in email:     
#         username , domain = email.split('@')
#         if username and domain :
#             z,y = domain.split('.')
#             if z and y:
#                 return True
#     else:
#         return False
    

# results = filter(email_validaion,emails)

# x = list(results)

# print(x)


# email = input("enter ur email: ")

# if(email_validaion(email)):
#     print('welcome')
# else:
#     print("try again")

domains = map(lambda x: x.split("@"),emails)

x = list(domains)
for i in x:
    print(i[1])


list = [{"name":"omar","pass":"123"},{"name":"ali","pass":"444"}]

name = input("enter ur name : ")

for i in list:
    if name == i["name"]:
        pas = input('enter ur pass: ')
        if pas == i["pass"]:
            print("welcome")
            break
    else:
        continue
else:
    print("not valid")
    exit()

