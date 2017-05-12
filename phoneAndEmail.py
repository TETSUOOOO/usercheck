#! python3
# phoneAndEmail.py - Registers syntactical phone numbers and e-mails for registrants

import json, re

filename = 'passwords.json'

def registerPhone(number):
    phoneRegEx = re.compile(r'''(
    (\d{3}|\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

    phoneObject = phoneRegex.search(email)
    try:
        phoneObject.group()
    except AttributeError:
        print('Your phone number is invalid.')
        number = input('Please re-enter phone number>')
        registerPhone(number)
    else:
        print('Phone number accepted!')
        with open(filename, 'a') as num_obj:
            json.dump(number, num_obj)
        print('Phone number saved in database!')

def registerEmail(email):
    emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

    emailObject = emailRegex.search(email)
    try:
        emailObject.group()
    except AttributeError:
        print('Your e-mail is invalid.')
        email = input('Please re-enter e-mail>')
        registerEmail(email)
    else:
        print('Thank you! A confirmation e-mail will be sent to activate your account!')
        with open(filename, 'a') as email_obj:
            json.dump(email, email_obj)
        print('E-mail saved in database!')
