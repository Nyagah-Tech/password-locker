class User:
    '''
    used to generate instances of the new users
    '''
    users_list = []
    def __init__(self,firstname,lastname,username,age,password,):
        '''
        gives a blue print of how the users will be generated
        '''

        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        
        self.age = age
        self.password = password

    def saveUser(self):
        '''
        this method is that saves the users to the users_list
        '''
        User.users_list.append(self) 

