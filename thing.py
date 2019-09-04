class Thing:
    '''
    v 1.0 
    '''
    def __init__(self, value):
        self.__value = value
    @property
    def Value(self):
        return self.__value
