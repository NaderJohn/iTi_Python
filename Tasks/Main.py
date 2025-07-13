from validate_name_email import validate_name_email
from email_checker import validate_email_list  
from extract_domains import extract_domains
from email_validation_with_retry import email_validation_with_retry
from login_system import login_system
from mario_pyramid import mario_pyramid
from count_vowels import count_vowels
from find_letter_i import find_letter_i
from multiplication_table import multiplication_table

def main():
    print("\nMenu Options:")
    print("1. Name and Email")
    print("2. Check Email List (from CSV)")  
    print("3. Show Email Domains")
    print("4. Validate Email")
    print("5. Login")
    print("6. Mario Pyramid")
    print("7. Count Vowels")
    print("8. Find 'i' Positions")
    print("9. Multiplication Table")
    
    choice = input("\nChoose 1-9: ")
    
    if choice == "1":
        print("\n[Name and Email Validation]")
        result = validate_name_email()
        print("\nResult:")
        print("Name:", result["name"])
        print("Email:", result["email"])
    
    elif choice == "2":
        print("\n[Email List Validation from CSV]")
        valid_emails = validate_email_list() 
        print("\nResult:")
        if valid_emails:
            print("Valid emails found:")
            for email in valid_emails:
                print(email)
        else:
            print("No valid emails found or file missing")
    
    elif choice == "3":
        print("\n[Email Domains Extraction]")
        domains = extract_domains()
        print("\nResult:")
        for domain in domains:
            print(domain)
    
    elif choice == "4":
        print("\n[Email Validation with Retry]")
        result = email_validation_with_retry()
        print("\nResult:")
        if result["status"] == "success":
            print("Valid email:", result["email"])
        else:
            print("Failed after 2 attempts")
    
    elif choice == "5":
        print("\n[Login System]")
        result = login_system()
        print("\nResult:")
        if result["status"] == "success":
            print("Welcome", result["user"])
        else:
            print("Login failed")
    
    elif choice == "6":
        print("\n[Mario Pyramid]")
        pyramid = mario_pyramid()
        print("\nResult:")
        print(pyramid)
    
    elif choice == "7":
        print("\n[Vowel Counter]")
        result = count_vowels()
        print("\nResult:")
        print("Text:", result["text"])
        print("Vowels count:", result["vowel_count"])
    
    elif choice == "8":
        print("\n[Find Letter 'i']")
        result = find_letter_i()
        print("\nResult:")
        print("Text:", result["text"])
        print("'i' positions:", result["positions"])
    
    elif choice == "9":
        print("\n[Multiplication Table]")
        result = multiplication_table()
        print("\nResult:")
        for line in result:
            print(line)
    
    else:
        print("Invalid choice. Please run the program again and choose 1-9")

    print("\nProgram completed. Goodbye")

if __name__ == "__main__":
    main()