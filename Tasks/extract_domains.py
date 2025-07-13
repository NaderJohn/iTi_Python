emails = [
    "ali@gmail.com",
    "sara@yahoo.com",
    "mohamed@outlook.com",
    "noha@iteg"
]

def get_domains(email_list=None):  
    if email_list is None:
        email_list = emails
    domains = []
    for email in email_list:
        if '@' in email:
            domains.append(email.split('@')[1])
    return domains


def extract_domains():
    return get_domains()