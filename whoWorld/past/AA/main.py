from entry import *
import player as pl
from threading import Thread

player = pl.see(16*25//2,16*25//2,16*25,16*25)
oneGroup = 25
updGroup = 1

def CreativeTh():
    global cthing
    while True:
        cthing

class whoWorld(windows):
    def __init__(self,w,h,mode=0,color=32):
        super(whoWorld,self).__init__(w,h,mode,color)
    def play(self):
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        self.win.fill(0,0,0)
        test.upd()
        pygame.display.update()
class Group(school):
    def __init__(self,x,y,oneGr,updGr,lens):
        self.og=oneGr
        self.ug=updGr

        self.lens=lens
        self.x=x
        self.y=y
        super(Group,self).__init__()
class groupUpd(school):
    def __init__(self,x,y,oneGr,updGr):
        self.og=oneGr
        self.ug=updGr
        
        self.rx,self.lx=x,x
        self.ry,self.ly=y,y
        super(groupUpd,self).__init__()
    def upd(self,ob=None,lens=None):
        
        for i in range(len(self.list)):
            self.list[i].upd(self.list,i)


Main = whoWorld(16*25,16*25)

gameRun = True
cthing = school()
crOpt = []#0:x,2:y,3:do?
things = groupUpd(0,0,oneGroup,updGroup)
#block.createMap.create(Main.win,block.earch.grass,obj,16*25,16*25,16)
things.list.append(Group(0,0,oneGroup,updGroup,1))
block.createMap.create(Main.win,things.list[0],16*25,16*25,0,0,player,0,16)

CRTHS = Thread(target=CreativeTh)
CRTHS.start()

pygame.init()
font=pygame.font.SysFont(None,50)
pygame.key.set_repeat(1)
tkick = pygame.time.Clock()
if __name__ == "__main__":
    a = []
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                gameRun=False
                pygame.quit()

                #wait thread close
                CRTHS.join()

                sys.exit()
            if i.type == pygame.KEYDOWN:
                if i.key==pygame.K_UP:
                    player.y -= 1
                    #print('s')
                if i.key==pygame.K_DOWN:
                    player.y += 1
                
        #print(pygame.mouse.get_pos())
        Main.win.fill((135,206,235))
        Main.win.blit(font.render(str(player.x)+','+str(player.y),
                                True,(255,255,255)),
                    (0,0))
        player.upd()
        things.upd()
        pygame.display.update()
        tkick.tick(30)
