init -10 python :
    import os
    import json
    class BD(object):
        def __init__(self,location):
            self.loction=os.path.expanduser(location)
            self.load(self.location)
        def load(self, location):
            if os.path.exists(location):
                self.open_f()
            else:
                self.BD_INIT_MODULE = {}
            return True
        def open_f(self):
            self.BD_INIT_MODULE = json.load(open(self.location,"r"))

        def convert(self):
            try:
                json.dump(self.BD_INIT_MODULE, open(self.location, "w+"))
                return True
            except:
                return False
       #def write(self,key,value):
