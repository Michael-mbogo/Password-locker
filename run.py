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

def login_user(user_name,site_password):
    """
    function that checks whether a user exist and then login the user in.
    """
    check_user_exist = Credentials.check_user_exist(user_name,site_password)
    return check_user_exist

def create_credential(user_name,account_name,site,site_password):
    '''
    Fn to create a new credential
    '''
    new_credential = Credential(user_name,account_name,site,site_password)
    return new_credential

def save_credential(credential):
    '''
    Fn that save a created credential
    '''
    Credential.save_credential(credential)

def display_credentials(user_name,site):
    '''
    Fn that lets us display a list of credentials
    '''
    Credential.display_credentials(user_name,site)

def find_credential(user_name):
    '''
    Fn that lets us serach and find the credential
    '''
    return Credential.found_credential(user_name)






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
            print(' ')
            print('Enter user name and password to log in')
            user_name = input('Username: ')
            site_password = input('Password: ')
            sign_in = login_user(user_name, site_password)
                if sign_in == True:
                print(f'Nice to have you back {user_name}.)



main()
