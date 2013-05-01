
class Hole(object):
    base = 0
    length = 0

    def __init__(self, base, length):
        self.base = base
        self.length = length

    def __del__(self):
        pass
        
