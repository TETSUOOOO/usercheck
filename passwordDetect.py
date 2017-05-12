#! python3
# passwordDetect.py - Ensures that password is 8 characters in length, at least one lowercase and one uppercase letter,
# and at least one digit
# saves accepted passwords into a json file

import json, re

filename = 'passwords.json'

def passwordDetector(text):
    """Uses a regex to parse the user input containing the password"""
    passRegEx = re.compile(r'[a-z{1,6}A-Z{1,6}0-9+]{8}')
    passObject = passRegEx.search(text)
    try:
        passObject.group()
    except AttributeError:
        print('Your password is not secure!')
        text = input('Please re-enter password>')
        passwordDetector(text)
    else:
        print('Your password is secure! Please confirm password>')
        confirmed = input()
        if confirmed == text:
            with open(filename, 'a') as pass_obj:
                json.dump(text, pass_obj)
            print('Password is saved!')
        else:
            print('Does not match! Please try again.')
            text = input('Please re-enter password>')
            passwordDetector(text)
