import unittest # Importing the unittest module
from User import User

class TestUser(unittest.TestCase):
 '''
     Test clas that  defines test cases foe the User class

    '''

    def test_setUp(self):

        '''
        SetUp method to run before test cases

        '''
        self.new_user = User('Jerry','Nabango','Jerry','onyango')

    def test_init(self):

        '''
        Test case to test if the object is initialized properly

        '''

        self.assertEqual(self.new_user.first_name, 'Jerry')

        self.assertEqual(self.new_user.last_name, 'Nabango')

        self.assertEqual(self.new_user.username, 'Jerry')

        self.assertEqual(self.new_user.password, 'onyango')

    def test_save_user(self):

        '''
        Test case to check if the users information can be saved

        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_user_exists(self):
        
        '''
        Test case to check if the users info already exisits

        '''
        self.new_user.save_user()#saving the new User
        self.assertTrue(User.user_exists('Jerry'))

def test_user_exists(self):
        
        '''
        Test case to check if the users info already exisits

        '''
        self.new_user.save_user()
        self.assertTrue(User.user_exists('Jerry'))

if __name__ == '__main__':
    unittest.main()



