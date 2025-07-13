#Nader John 
emails = [
    "ali@gmail.com",
    "sara@yahoo.com",
    "mohamed@outlook.com",
    "noha@iteg"
]

domain=map(lambda x:x.split('@'),emails)
y=list(domain)
for i in y:
    print(i[1])
    
    