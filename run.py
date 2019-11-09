#!/usr/bin/env python3.6
from user import User
from credential import credential

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