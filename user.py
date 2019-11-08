class User:
    '''
    used to generate instances of the new users
    '''
    user_list = []
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
        User.user_list.append(self) 

    @classmethod
    def user_exist(cls,username,password):
        '''
        checks if an account exist using the username provided by the user
        Args:
            username:this is the username given by the user trying to login in
            return:
                boolean:returns true or false depending on the findings.
        '''
        for user in cls.user_list:
            if user.username  == username and user.password == password:
                return True

        return False

   

