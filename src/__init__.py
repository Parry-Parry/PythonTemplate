__version__ = "0.0.1"

class objectRegister(object):
    def __init__(self):
        self.objects = {}
    
    def register(self, obj, name : str = None):
        if name is None:
            name = obj.__name__
        self.objects[name] = obj
    
    def __get__(self, name : str):
        return self.objects[name]

        