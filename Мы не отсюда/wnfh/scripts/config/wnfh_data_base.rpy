init -10 python :
    import os
    import json
    class BD(object):
        def __init__(self,location):
            self.loction=os.path.expanduser(location)
            self.load(self.location)
        def load(self, location):
            if os.path.exists(location):
                self.load()
            else:
                self.BD_INIT_MODULE = {}
            return True
        def BD_INIT_MODULE(self):
            self.BD_INIT_MODULE = json.load(open(self.location,"r"))
        