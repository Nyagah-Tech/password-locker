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
    return User.user_auth(username,password)

def display_credentials():
    '''
    this function is responsible for displaying the users credentials
    '''
    return User.cred_display()

def valid_user(firstname,lastname,username,email,password):
    '''
    validates if the user has filled in all the fields required
    '''
    if firstname=="" or lastname=="" or username=="" or email=="" or password=="" :
        return False
    else:
        return True

#credentials

def create_cred_for_existingfile(filename,email,passwords):
    '''
    it will create credentials of an existing account
    '''
    new_cred = Credential(filename,email,passwords)
    return new_cred

def save_creds(Credential):
    '''
    this function saves credentials
    '''
    Credential.save_cred()

def delete_cred(Credential):
    '''
    this function will delete a credential list
    '''
    Credential.del_cred()

def find_cred_byfilename(filename):
    '''
    this function will search for a credential with the given file filename
    '''
    return Credential.cred_exist(filename)

def display_creds():
    '''
    this function wil display all the the saved credentials
    '''
    return 





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

    validAcc = valid_user(firstname,lastname,username,email,password)
    if validAcc:
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

            while True:
                print("use the following shortcodes to navigate through the application")
                print("short_code::: dd -to display all your saved credentials, dc -to delete a credential, fc -find credential by filename, cc -save credentials of an existing account, nc - make credentials for a new account")

                code = input().lower()

                if code == 'cc':
                    print("saving credentials of an existing account or file")
                    print




        else:
            print("invalid username or password")
    else:
        print("please fill all fields required.")
        
        


if __name__ == '__main__':
    main()


    
