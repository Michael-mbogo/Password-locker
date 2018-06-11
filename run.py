#!/usr/bin/env python3.6
from user_credentials import User

#creating a user
def create_user(fname,lname,password):
    '''
    Function to create a new user
    '''

    new_user = User(fname,lname,password)
    return new_user

def save_user(user):
    '''
    Function to save a user
    '''
    user.save_user()

def delete_user(user):
    '''
    Function to delete user
    '''
    user.delete_user()

def display_user():
    return User.display_user()

def verify_user(first_name, password):
    '''
    Function that verifys the existance of a user
    '''
    check_user = Credential.check_user(first_name, password)
    return check_user

def create_credential(user_name,account_name,site,site_password):
    '''
    Fn to create a new credential
    '''
    new_credential = Credential(user_name,account_name,site,site_password)
    return new_credential



def main():
    print("Jambo, Welcome to password locker. Are you a member?")
    print('\n')

    while True:
        print("Use these shortcodes : su- create a new account, li- log in, du- display user, del - delete user, ex- exit password locker ")

        short_code = input().lower()

        if short_code == 'ex':
            print("We will miss you, come back again.")

            break

        elif short_code == "su":
            print("Sign up")
            print('-' * 30)
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            password = input('Enter password: ')
            save_user(create_user(first_name,last_name,password))

            print(f"Thank you {first_name} {last_name} for joining us. Your passoword is {password}")

        elif short_code == "li":
            print()
main()
