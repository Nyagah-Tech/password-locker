import unittest
from user import User
from credential import Credential

class passwordTest(unittest.TestCase):
    '''
    this class defines the test cases  for the user class behaviour.
    args:
    unittest.TestCase:TESTCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        should run before each test case
        '''
        self.new_user = User("Daniel","nyagah","dannyagah","age","password")
        self.new_cred = Credential("instagram","da@gmail.com","12345") 
    def tearDown(self):
        '''
        it clears or clean up after every case
        '''
        User.user_list = []
        Credential.creds_list = []

    def user_init(self):
        self.assertEqual(self.new_user.firstname,"Daniel")
        self.assertEqual(self.new_user.lastname,"nyagah")
        self.assertEqual(self.new_user.username,"dannyagah")
        self.assertEqual(self.new_user.age,"age")
        self.assertEqual(self.new_user.password,"password")


    def testsave_user(self):
        '''
        testsave meselfthod saves the new user to the user list
        '''
        self.new_user.saveUser()
        self.assertEqual(len(User.user_list),1)

    def testuser_exist_byusername(self):
        '''
        to check the existence of a user through the password inputted
        '''
        self.new_user.saveUser()
        userExist = User.user_exist("dannyagah","password")
        self.assertTrue(userExist)

#creating credentials
    def cred_init(self):
        '''
        is a test case that tests if an object initialized properly
        '''

        self.assertEqual(self.new_cred.filename,"instagram")
        self.assertEqual(self.new_cred.email,"da@gmail.com")
        self.assertEqual(self.new_cred.password,"12345")

    

if __name__ == '__main__':
    unittest.main()