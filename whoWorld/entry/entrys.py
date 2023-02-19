import pygame
from pygame.locals import *

class Entry:
    def __init__(self,x,y,image,target):
        self.target=target
        self.image=pygame.image.load(image)
        self.rect=pygame.rect.Rect(x,y,*self.image.get_size())
        self.mask=pygame.mask.from_surface(self.image)
        self.x=x
        self.y=y
    def upd(self,ob,lens):
        self.rect.topleft=self.x,self.y
        self.target.blit(self.image,self.rect)
        
        
