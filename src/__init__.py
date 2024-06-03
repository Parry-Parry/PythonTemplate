__version__ = "0.0.1"

class functionRegister(object):
    def __init__(self):
        self.functions = {}
    
    def register(self, func : callable, name : str = None):
        if name is None:
            name = func.__name__
        self.functions[name] = func
    
    def __get__(self, name : str):
        return self.functions[name]
        