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
