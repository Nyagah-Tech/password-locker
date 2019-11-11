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
    return Credential.cred_display()

def existing_cred(del_filename):
    '''
    will look of a credential account if it exist and return a boolean
    '''
    return Credential.find_credential_byName(del_filename)





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
        print('-'*70)

        print("log in below with your username and password")
        print('/n')

        print("enter your username")
        loguser = input()
        print('/n')

        print("enter your password")
        logPass = input()

        if authenticate_user(loguser,logPass):
            print(f"{loguser} welcome to your account")
            print("-"*70)

            while True:
                print("use the following shortcodes to navigate through the application")
                print("short_code::: dd -to display all your saved credentials, dc -to delete a credential, fc -find credential by filename, cc -save credentials of an existing account, nc - make credentials for a new account")

                code = input().lower()

                if code == 'cc':
                    print("saving credentials of an existing account or file")
                    print("please fill the required fields below")
                    print("enter the filename or account name...")
                    filename = input().lower()

                    print("enter your email address...")
                    c_email=input()

                    print("enter your password")
                    c_password = input()

                    save_creds(create_cred_for_existingfile(filename,c_email,c_password))
                    print(f"you have successfully saved your {filename} credentials.")

            
                elif code == 'dc':
                    print("enter the file name or account name of the credentials you want to delete")
                    del_filename = input().lower()
                    if existing_cred(del_filename):
                        del_Acc = find_cred_byfilename(del_filename)
                        delete_cred(del_Acc)
                        print(f"you have successfully deleted the {del_Acc.filename} account credentials")

                    else:
                        print("the above file name oesnot xist in your credential list")
                
                elif code == 'fc':
                    print("enter the file name or account name of the credemtial account you searching for")
                    searchName = input().lower()
                    if existing_cred(searchName):
                        searchAcc = find_cred_byfilename(searchName)
                        print(f"your account is :::")
                        print("-"*20)

                        print(f"account name ..... {searchAcc.filename} ")
                        print(f"account passsword ..{searchAcc.password}")
                        print(f"email address ......{searchAcc.email}")


                    else:
                        print("the above account doesn't exist")
                
                elif code == 'dd':
                    if display_creds() != '':
                        for cred in display_creds():
                            print(f"accountname::: {cred.filename}  password::: {cred.password} email::: {cred.email}")

                    else:
                        print("you have no saved credentials")

                elif code == 'nc':
                    print("make credentials of a none exising account")
                    print("enter the filename or the account name of your new account..")
                    fname = input().lower()
                    print("enter email address")
                    n_email = input()
                    print("Do you want the application to generate a password for you?    enter YES: if you want the application to generate you a password.. NO: if you want to enter your own password ")
                    shortcode = input().lower()

                    if shortcode == 'yes':
                        passcode = n_email[:4] + "234"
                        print(f"your password is {passcode} ")
                        
                    else:
                        print("enter your password")
                        passcode = input()
                    save_creds(create_cred_for_existingfile(fname,n_email,passcode))
                    print(f"you have succesfully created your new credentials for {fname} account")

                    

        else:
            print("invalid username or password")
    else:
        print("please fill all fields required.")
        
        


if __name__ == '__main__':
    main()


    
