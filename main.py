# ------------------------ init ----------------------------------

import sys, os, json
import pygame
from pygame.locals import *

from core import Engine, GameObj
from core.Space import Sprite, Widget
from core import utils as t

game_setting = {
    "windows_size" : [960, 540],
    "windows_name" : "game",
    "windows_var" : "screen",
    "frame_rate" : 60,
    "resizable" : True,
    "resource" : {
        "ball" : ["image", "pic", "intro_ball.gif"]
    }
}
game_setting = Engine.GlobalSettings(game_setting) # turn string to GS instance
engine = Engine.Engine(game_setting) # init the game


screen = engine.screen
ball, ballrect = engine.asset.ball

# ------------------------ game loop ----------------------------------

white = t.rgb(0xFFFFFF)
black = t.rgb(0x000000)
red = t.rgb(0xFF0000)
blue = t.rgb(0x0000FF)

pan = [[] for i in range(5)]
class qp(Widget.Widget):
    def __init__(self, pos):
        lt =(pos[0]*50,pos[1]*50)
        size = [50, 50]
        super().__init__( Rect(lt, size) )
        self.pos = pos
        self.raw_events = {MOUSEBUTTONDOWN: None, MOUSEBUTTONUP: None}
        
        self.state = 0
    
    def process(self):
        mpos = pygame.mouse.get_pos()
        # print(mpos, self.rect)
        if self.rect.collidepoint(mpos):
            self.surface.fill(white)

            if self.raw_events[MOUSEBUTTONUP]:
                for x in self.raw_events[MOUSEBUTTONUP]:
                    if x.button == BUTTON_LEFT:
                        self.send(["clickboard", self.pos])
        else:
            self.surface.fill(black)
        
    def render(self):
        s = self.surface
        rc = s.get_rect()
        pygame.draw.rect(s, black, rc)
        rc.inflate_ip(-5,-5)
        pygame.draw.rect(s, white, rc)

        r = int(rc.width // 2.5)
        if self.state == 1:
            pygame.draw.circle(s, red, rc.center, r)
        elif self.state == 2:
            pygame.draw.circle(s, blue, rc.center, r)


for p in t.product(range(5), repeat=2):
    pan[p[0]].append((0 ,qp(p)))
qps = list(t.filter(lambda x: type(x) != int ,t.flatten(pan)))

turn = 1

while True:
    engine.frame_begin()
    screen = engine.screen


    screen.fill((0, 0, 0))
    fps = engine.clock.get_fps()
    
    fnt = pygame.font.Font(pygame.font.match_font("arial"), 16)
    fpsinfo = fnt.render("%.2f fps"%fps, True, white)
    
    for he in engine.hl_events_list:
        if he[0] == "clickboard":
            (pan[he[1][0]][he[1][1]][1].state) = ((pan[he[1][0]][he[1][1]][1].state) + 1) % 3

    for x in qps:
        x.render()
        screen.blit(x.surface, x.rect)
    screen.blit(fpsinfo, (screen.get_size()[0]-100,screen.get_size()[1]-100))

    
    engine.frame_end()
