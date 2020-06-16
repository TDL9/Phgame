import sys, os
import pygame
from pygame.locals import *

from . import GameObj, utils
from .ResourceManager.GlobalSettings import *
from .ResourceManager.ResourceLoader import *


class Engine():
    _instance_ = None
    def get():
        return Engine._instance_

    def __init__(self, gset):
        if Engine._instance_ != None: return None # Singleton
        Engine._instance_ = self

        # check if some module of pygame is None
        if not pygame.font: print('Warning, fonts disabled')
        if not pygame.mixer: print('Warning, sound disabled')
        # init pygaem
        pygame.init()

        self.settings = gset

        # init windows
        wn = gset.windows_var
        windows_setting = 0
        if gset.resizable: windows_setting |= pygame.RESIZABLE
        self.__dict__[wn] = pygame.display.set_mode(gset.windows_size, flags = windows_setting)

        pygame.display.set_caption(gset.windows_name)


        # set frame timer
        self.clock = pygame.time.Clock()

        # load asset
        asset_d = {}
        for name in gset.resource:
            resource_type = gset.resource[name][0]
            resource_value = tuple(gset.resource[name][1:])
            resource_value = os.path.join(*resource_value)
            if resource_type == "image":
                item = load_image(resource_value)
            if resource_type == "sound":
                item = load_sound(resource_value)
            asset_d[name] = item
        self.asset = Resources(asset_d)

        # root obj, used to distribute events to game objects
        self.root_obj = GameObj.GameObj(add_to_root=False)
        self.root_obj.rect = Rect((0, 0), self.__dict__[self.settings.windows_var].get_size())

    
    def frame_begin(self):
        if pygame.event.get(pygame.QUIT):
            sys.exit()
        self.raw_events_list = pygame.event.get()
        
        self.root_obj.raw_events = dict.fromkeys(self.root_obj.raw_events, utils.nothing)
        for event in self.raw_events_list:
            if event.type in self.root_obj.raw_events:
                self.root_obj.raw_events[event.type] += [event,]
            else:
                self.root_obj.raw_events[event.type] = [event,]
        
        if self.root_obj.raw_events[pygame.VIDEORESIZE]:
            SCREEN_SIZE = self.root_obj.raw_events[pygame.VIDEORESIZE][0].size
            self.__dict__[self.settings.windows_var] = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
            self.root_obj.rect = Rect((0, 0), self.__dict__[self.settings.windows_var].get_size())

        self.hl_events_list = [] # high-level list
        self.root_obj._process()
        

    def frame_draw(self):
        pass


    def frame_end(self):
        self.clock.tick(self.settings.frame_rate)
        pygame.display.flip()
    
GameObj.Engine = Engine