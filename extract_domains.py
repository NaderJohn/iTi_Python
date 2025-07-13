emails = [
    "ali@gmail.com",
    "sara@yahoo.com",
    "mohamed@outlook.com",
    "noha@iteg"
]

def extract_domains():
    domain = map(lambda x: x.split('@'), emails)
    y = list(domain)
    return [i[1] for i in y]