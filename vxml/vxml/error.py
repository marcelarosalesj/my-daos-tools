''' This module contains the error class that represents Valgrind leaks. '''

class VXMLError:
    '''
    A class to represent Valgrind XML errors
    '''
    def __init__(self, kind):
        '''
        Constructs an error object
        '''
        self.kind = kind

    def __str__(self):
        '''
        Informal string representation of the object
        '''
        return self.kind

    def get_kind(self):
        '''
        Returns the kind of the error
        '''
        return self.kind

    def set_kind(self, kind):
        '''
        Set error kind
        '''
        self.kind = kind
