class Credential :
    '''
    the credential class is used to generate crentials for a user to store
    '''
    creds_list = []
    def __init__(self,filename,email,password):
        '''
        blueprint on how the credentials will be made
        '''
        self.filename = filename
        self.email = email
        self.password = password

    def save_cred(self):
        '''
        this method saves credentials into our cred list
        '''

        Credential.creds_list.append(self)

    @classmethod
    def cred_display(cls):
        '''
        returns the contact list
        '''
        return cls.creds_list
