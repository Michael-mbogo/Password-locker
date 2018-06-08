class User:
    '''
    Class that generates new instance of users.
    '''

    user_list = []

    def save_user(self):
        '''
        This method saves users in the user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        The method removes a saved user
        '''

        User.user_list.remove(self)

    def __init__(self,first_name,last_name,password):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
