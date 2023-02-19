import pygame
from pygame.locals import *
import sys
import entry.entrys
import block

class school:
    def __init__(self):
        self.list = []
    def upd(self,ob=None,lens=None):
        for i in range(len(self.list)):
            self.list[i].upd(self.list,i)

class windows:
    def __init__(self,w,h,mode=0,color=32):
        self.win=pygame.display.set_mode((w,h),mode,color)
    def play(self):
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
#a = windows(800,600)
#a.play()
