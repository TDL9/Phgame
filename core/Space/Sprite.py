from .. import GameObj

class Sprite(GameObj.GameObj):
    '''
    Sprite has a pos, image to draw, anchor point
    note that sprite don't draw directly to screen, but to camera
    '''
    def __init__(self, event_types = []):
        GameObj.GameObj.__init__(self, event_types)
        self.pos = [0, 0]
        self.anchor = [0, 0]
        self.image = None
    
