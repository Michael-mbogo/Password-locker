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
    contact.save_user()

def delete_user(user):
    '''
    Function to delete user
    '''
    contact.delete_user()

def main():
    print("Jambo, Welcome to password locker. Are you a member?")

main()
