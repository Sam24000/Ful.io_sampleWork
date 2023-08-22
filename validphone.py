import re

def validate_contact_number(contact_number):
    # Regular expression pattern for a valid contact number

    pattern=re.compile("^\+?\d{10}")
    if(pattern.match(contact_number)):
        return True
    pattern=re.compile("^\+?\d.\s?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}?")
    if(pattern.match(contact_number)):
        return True
    pattern=re.compile("\(?\d{3}\)[-.\s]?\d{3}[-.\s]\d{4}?")
    if(pattern.match(contact_number)):
        return True
    pattern=re.compile("^\+?\d{3}[-.\s]?\d{3}[-.\s]\d{4}?")
    if(pattern.match(contact_number)):
        return True
    
# Input contact number from the user
contact_number = input("Enter a 10-digit contact number: ")

if validate_contact_number(contact_number):
    print("Valid contact number")
else:
    print("Invalid contact number")
