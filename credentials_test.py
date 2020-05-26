import unittest #Importing the unnittest module
from credentials import Credential #Importing the credentials class
import pyperclip

class TestCredential(unittest.TestCase):

    '''
    Args:
        unittest.TestCase class that helps in creating test cases.

    '''

    def setUp(self):

        '''
        Set up method to run before each test cases

        '''
        self.new_cred = Credential('twitter', 'Jeery', 'onyango')

    def tearDown(self):

        '''
        Method that does clean up after each test has run.

        '''
        Credential.cred_list = []

    def test_init(self):

        '''
         Test case to check if initialization of objects are proper

        '''

        self.assertEqual(self.new_cred.account_name,'Jerry')

        self.assertEqual(self.new_cred.username, 'Nabango')

        self.assertEqual(self.new_cred.password, 'onyango')

    def test_save_cred(self):

        '''
        Test case to check if we can save our credentilas in the empty cred_list.

        '''

        self.new_cred.save_cred()
        self.assertEqual(len(Credential.cred_list),1)

    def test_save_multiple_cred(self):

        '''
        Test case to check if we can save multiple credentials objects to the cred_list

        '''
        self.new_cred.save_cred()

        test_cred = Credential('facebook','Jerry Nabango','crew')

        test_cred.save_cred()
        self.assertEqual(len(Credential.cred_list),2)

    def test_display_cred(self):
        '''
        Test case to test if the credentials can be displayed.

        '''
        self.assertEqual(Credential.display_cred(), Credential.cred_list)

    def test_delete_cred(self):

        '''

        Test case to test if i can remove credentials that i no longer need

        '''
        self.new_cred.save_cred()

        test_cred = Credential('facebook','crew')

        test_cred.save_cred()

        self.new_cred.delete_cred() #Deleteing the credentials objects
        self.assertEqual(len(Credential.cred_list),1)

    def test_copy_cred(self):
        '''
        Test to test if credentials are copied to clipboard.
        '''
        self.new_cred.save_cred()
        Credential.copy_cred('Jerry')
        self.assertEqual(pyperclip.paste(), self.new_cred.username)
