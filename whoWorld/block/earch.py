import entry

class grass(entry.entrys.Entry):
    def __init__(self,x,y,target,pl,other=None):
        self.pl=pl
        if other:
            #print(other)
            super(grass,self).__init__(x,y,other,target)
        else:
            super(grass,self).__init__(x,y,".\\block\\image\\grass.png",target)
    def upd(self,ob=None,lens=0):
        #print(self.pl.urx,self.rect.x,self.pl.ury,self.rect.y)
        self.rect.topleft=self.x,self.y
        self.target.blit(self.image,(self.rect.x-self.pl.urx,
                                     self.rect.y-self.pl.ury))
        #print(12)
class diry(grass):
    def __init__(self,x,y,target,pl):
        super(diry,self).__init__(x,y,target,pl,".\\block\\image\\diry.png")
class stone(grass):
    def __init__(self,x,y,target,pl):
        super(stone,self).__init__(x,y,target,pl,".\\block\\image\\stone.png")
class snow(grass):
    def __init__(self,x,y,target,pl):
        super(snow,self).__init__(x,y,target,pl,".\\block\\image\\snow.png")
class ice(grass):
    def __init__(self,x,y,target,pl):
        super(ice,self).__init__(x,y,target,pl,".\\block\\image\\ice.png")


blockList = []
blockList=[grass,stone]
