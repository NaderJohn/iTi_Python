import os
import csv
from email_validation_with_retry import email_validation_with_retry
import extract_domains

def validate_email_list():
    file_name = "E-mails.csv"
    file_path = os.path.join(os.getcwd(), file_name)
    emails = []

    if os.path.exists(file_path):
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                if row:
                    emails.append(row[-1])

        
        def is_valid(email):
            try:
                username, domain = email.split('@')
                z, y = domain.split('.')
                return bool(z and y)
            except ValueError:
                return False

        valid_emails = list(filter(is_valid, emails))
        extract_domains.get_domains(emails)
        return valid_emails
    else:
        print("File not found.")
        return []