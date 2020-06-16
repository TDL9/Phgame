

class Magical_Call():
    magic = ["rot"]

    def _rot(self):
        print("rot")
        return self

    def __init__(self):
        pass
    def __getattr__(self, name):
        if name in self.magic:
            return self.__getattribute__('_'+name)()
        else:
            raise AttributeError("Magical_Call has no attribute or magic function named : %s"%name)
class MCS():
    pass

mc = Magical_Call()
mc.rot.rot
# mc.fuxk
mc._rot()
# mc.gg()

a=MCS()
a.a