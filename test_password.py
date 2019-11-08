import unittest
from user import User

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
        self.new_user = User("Daniel","nyagah","dannyagah","age","password",) 
    def tearDown(self):
        '''
        it clears or clean up after every case
        '''
        User.users_list = []

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
        self.assertEqual(len(User.users_list),1)


if __name__ == '__main__':
    unittest.main()