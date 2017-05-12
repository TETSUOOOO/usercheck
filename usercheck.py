#! python3

# Thomas Vilela's user creation program - a small program that utilizes a class to keep track of user input/information
# (2) separate header files are imported within the class methods (passwordDetect, phoneAndEmail)
# File creates a json file that stores password, email, and phone number - please do not share any of this information
# THIS IS NOT A SECURE SOURCE FOR STORING PRIVATE INFORMATION - for didactic purposes only
# thomasavilela@gmail.com for any inquiries/comments

import os

class User():
    """Depicts information regarding a user account"""

    def __init__(self, first_name, last_name, alias, email, phone):
        """Initialize the user data"""
        self.first_name = first_name
        self.last_name = last_name
        self.alias = alias
        self.email = ''
        self.phone = 0
        self.log_attempt = 0

    def initialize_password(self, password):
        """Register a password using a regex"""
        from passwordDetect import passwordDetector
        passwordDetector(password)

    def initialize_email(self, email):
        """Enter an acceptable e-mail address with a regex check"""
        from phoneAndEmail import registerEmail
        registerEmail(email)

    def initialize_phone(self, phone):
        """Enter an acceptable phone number with a regex check"""
        from phoneAndEmail import registerPhone
        registerPhone(phone)
        
    def describe_user(self):
        """Print summary of user pertinents"""
        print("User Summary".center(40, "="))
        print("Full name: " + self.first_name.title() + ' ' + self.last_name.title())
        print("Nick: " + self.alias)
        print("Email: " + self.email)
        print("Phone number: " + self.phone)

    def greet_user(self):
        """Print a greeting for the user"""
        print("Welcome, " + self.alias + "!")

    def increment_login_attempts(self):
        """Increments value of attempts by 1"""
        self.log_attempt += 1

    def reset_login_attempts(self):
        """Resets login attempts to 0"""
        self.log_attempt = 0
        print("You need to sign-in or register")
        
userArray = []
print("Please enter your first name, last name, and alias>")
for i in range(3):
    if i == 0:
        print("First name: ", end='')
    elif i == 1:
        print("Last name: ", end='')
    elif i == 2:
        print("Nickname: ", end='')
    userInfo = input()
    userArray += [userInfo]
    
email = input("Enter your e-mail>")
phone = input("Enter your phone number>")
user1 = User(userArray[0], userArray[1], userArray[2], email, phone)

text = input("Enter a password - must be 8 alphanumerics with at least one capital and one lower case letter>")

user1.initialize_password(text)
user1.initialize_email(email)
user1.initialize_phone(phone)
user1.email = email
user1.phone = phone
user1.describe_user()

loginUser = input("Enter your alias>")
if loginUser in userArray:
    user1.increment_login_attempts()
    print("You are already logged in, " + user1.alias + ".")
else:
    user1.reset_login_attempts()
