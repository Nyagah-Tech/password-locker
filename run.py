#!/usr/bin/env python3.6
from user import User
from credential import Credential

def create_userAccount(fname,lname,username,email,password):
    '''
    this is a funtion to create a new user account
    '''
    new_user = User(fname,lname,username,email,password)
    return new_user

def save_user(User):
    '''
    this is function that saves the new user account generated
    '''
    User.saveUser()

def authenticate_user(username,password):
    '''
    this function authenticates users on login using their username and password
    '''
    return User.user_exist(username,password)

def display_credentials():
    '''
    this function is responsible for displaying the users credentials
    '''
    return User.cred_display()



def main():
    print("Hello and Welcome to the password locker apllication that helps you save and keep your passwords safe. First you need to create your own account by filling the below required fields")
    
    print("your first name?")
    firstname = input()

    print("your lastname?")
    lastname = input()

    print("enter your username of choice...")
    username = input()

    print("enter you email address...")
    email = input()

    print("enter your password of choice")
    password = input()

    if firstname=="" or lastname=="" or username=="" or email=="" or password=="" :
        print("please fill all the information required")
    else:
        save_user(create_userAccount(firstname,lastname,username,email,password))
        print(f"{username} you have succesfully created a password locker account..")
        print('/n')

    print("log in below with your username and password")
    print('/n')

    print("enter your username")
    loguser = input()
    print('/n')

    print("enter your password")
    logPass = input()

    if authenticate_user(loguser,logPass):
        print(f"{loguser} welcome to your account")
    else:
        print("invalid username or password")


if __name__ == '__main__':
    main()


    
