class see:
    def __init__(self,x,y,w,h):
        self.urx=x-w//2
        self.ury=y-h//2
        #print(x,y,w,h,self.urx,self.ury)
        #print()
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    def upd(self,ob=None,lens=None):
        self.urx=self.x-self.w//2
        self.ury=self.y-self.h//2
