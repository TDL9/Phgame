import pygame
from pygame.locals import *

from . import utils


class GameObj():

    def __init__(self, event_types = [], engine = None, add_to_root = True):
        self.raw_events = {}
        for et in event_types:
            self.raw_events[et] = None

        self.childs_obj = []
        if not engine:
            engine = Engine.get()
        self.engine = engine
        if engine and add_to_root:
            engine.root_obj.childs_obj.append(self)
    
    def add_child(self, chd):
        self.childs_obj.append(chd)
    
    def process(self):
        pass

    def _process(self):
        
        self.process()
        # passing raw events to child object, and call process recursively
        for chd in self.childs_obj:
            chd.raw_events = dict.fromkeys(chd.raw_events, utils.nothing)
            for event in chd.raw_events:
                if event in self.raw_events:
                    chd.raw_events[event] = self.raw_events[event]
            
            chd._process()
    
    def send(self, item):
        self.engine.hl_events_list.append(item)