import unittest
from user_credentials import User, Credential

class TestUser(unittest.TestCase):
    '''
    Test class defining test cases for the users class behavior

    '''

    def setUp(self):
        '''
        method that runs before each Test
        '''
        self.new_user = User("Michael","Mbogo","Michaelmm17") #create users

    def test_init(self):
        '''
        Test case to check proper initialization
        '''

        self.assertEqual(self.new_user.first_name,"Michael")
        self.assertEqual(self.new_user.last_name,"Mbogo")
        self.assertEqual(self.new_user.password,"Michaelmm17")

    def test_save_user(self):
        '''
        tests if the user is saved in the user list
        '''

        self.new_user.save_user() #saves new users
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        cleans up after each TestCase is made
        '''
        User.user_list = []

    def test_save_multiple_user(self):
        '''
        check to see if multiple users can be saved
        '''

        self.new_user.save_user()
        test_user = User("Ann","Bridgit","brig13")

        test_user.save_user()
        self.assertEqual(len(User.user_list),2)


    def test_delete_user(self):
        '''
        Deletes the user from the user_list
        '''

        self.new_user.save_user()
        test_user = User("Ann","Bridgit","brig13")

        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_display_user(self):
        '''
        displays all user
        '''

        self.assertEqual(User.display_user(), User.user_list)



#Credential class
class TestCredential(unittest.TestCase):
    '''
    Test case defining cases for credentials class behavior
    '''

    def setUp(self):
        '''
        function to create an account before each test
        '''
        self.new_credential = Credential('Mikey','Michael-mbogo','Facebook','Michaelmm17')

    def test__init__(self):
        '''
        Method testing proper initialization
        '''

        self.assertEqual(self.new_credential.user_name,"Mikey")
        self.assertEqual(self.new_credential.account_name,"Michael-mbogo")
        self.assertEqual(self.new_credential.site,"Facebook")
        self.assertEqual(self.new_credential.site_password,"Michaelmm17")

    def test_save_credential(self):
        '''
        saves credentials
        '''

        self.new_credential.save_credential()
        google = Credential('AnnB','Annbrig','twitter','Michaelmm17')
        google.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def tearDown(self):
        '''
        Clears the list after each test
        '''

        Credential.credential_list = []
        User.user_list = []

    def test_save_multiple_credentials(self):
        '''
        Test to check whether multiple functions can be saved
        '''

        self.new_credential.save_credential()
        test_credential = Credential('Kevin','Kevin Mwan','Facebook','Kevkev')
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def test_display_credentials(self):
        '''
        Displays the credentials
        '''
        self.assertEqual(Credential.display_credentials(), Credential.credential_list)


    def test_find_by_site(self):
        '''
        Function that helps search for a credential by user name
        '''
        self.new_credential.save_credential()
        test_credential = Credential('Kevin','Kevin Mwan','Facebook','Kevkev')
        test_credential.save_credential()
        found_credential = Credential.find_by_site('Facebook')
        self.assertEqual(found_credential.site, test_credential.account_name)













    # def test_check_user(self):
    #     '''
    #     Funcion testing login Functionuser
    #     '''
    #     self.new_user = User("Mike","Mbogo","Mikemm17")
    #     self.new_user.save_user()
    #     user2 = User('Kevin','Mbogo','Mikemm17')
    #     user2.save_user()
    #
    #     for user in User.user_list:
    #         if user.first_name == user2.first_name and user.password == user2.password:
    #             current_user = user.first_name
    #     return current_user
    #     self.assertEqual(current_user, credential.check_user(user2.password, user2.first_name))
    #
    #










if __name__ == '__main__':
    unittest.main()
