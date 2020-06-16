import json

class GlobalSettings():
    '''
    Global Settings for game engine, pass [dict / json string] to init
    '''
    def __init__(self, info = ""):
        self.windows_size = [100, 100]
        self.windows_name = "game"
        self.windows_var = "screen"
        if type(info) == dict:
            self.__dict__.update(info)
        elif type(info) == str and len(info):
            self.__dict__.update(json.loads(info))

class Resources(GlobalSettings): pass