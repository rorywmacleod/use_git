class Thing:
    '''
    v 1.1 added __str__
    '''
    def __init__(self, value):
        self.__value = value
    @property
    def Value(self):
        return self.__value
    def __str__(self):
        return f'Thing: {self.Value}'
