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

    def del_cred(self):
        '''
        this deletes a credential"
        '''
        Credential.creds_list.remove(self)
    @classmethod
    def cred_exist(cls,filename):
        '''
        this method will check if a particular filename exists
        Args:
            filename:this is the file name that will be searched
        return:
                it will return the credential file with the secific filename
        '''
        for cred in cls.creds_list:
            if cred.filename == filename:
                return cred

    @classmethod
    def cred_display(cls):
        '''
        returns the contact list
        '''
        return cls.creds_list
