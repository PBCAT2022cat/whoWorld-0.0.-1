from entry import *
from random import randint
import block

maps = [{'name':'mont','start':[-1,0,0,1,1,1,2,2,2,3,3,3],'centre':[-3,-3,-3,-2,-2,-2,-1,-1,-1,0,0,1],'startF':[0,1]},
        {'name':'pingOrMont','start':[0,-1,1],'centre':[0,-1,1],'startF':[0,1]},
        {'name':'ping','start':[0,0,0,0,0,0,0,0,0,0,-1,1],'centre':[0,0,0,0,0,0,0,0,0,0,-1,1],'startF':[0,1]}]
land = [{'name':'grass','start':[block.earch.grass],
         'centre':[block.earch.stone,block.earch.diry],'end':[block.earch.stone]},
        {'name':'ice','start':[block.earch.ice,block.earch.snow],
         'centre':[block.earch.ice],'end':[block.earch.stone]}]


def createFill(target,blocks,ob,w,h,pl,bwh=1):
    #lands = land[randint(0,len(land)-1)]
    gets = maps[randint(0,len(maps)-1)]
    #gets = maps[0]
    print(gets['name'])
    getses = gets['start']
    h = h//bwh
    w = w//bwh
    x = 3
    y = h
    yy = 3
    yyy = 0
    lists = []
    for x in range(w):
        #print(x,w/2)
        if x == 1:
            getses = gets['start']
        elif x != 0:
            if x > w/2 and randint(0,1)==0:
                getses = gets['centre']
            elif x > w/3 and randint(0,10)==0:
                getses = gets['centre']
            elif x > w/4 and randint(0,20)==0:
                getses = gets['centre']
        else:
            getses = gets['startF']
        yy = getses[randint(0,len(getses)-1)]
        yyy += yy
        #print(yyy,yy)
        x = x * bwh
        #print(yy,yyy)
        if yyy > 0:
            for i in range(yyy):
                i = blocks(x,0,target,pl)
                lists.append(i)
                for i in lists:
                    i.y += bwh
                i=None
            
            run = True
            while run:
                for xx in lists:
                    xx.y += bwh
                    #xx=None
                    #print(lists[0].y,h*bwh)
                #print(lists[len(lists)-1].y,lists[len(lists)-1].x)
                if lists[0].y >= h*bwh-bwh:
                    #print('s')
                    #run = False
                    break
                #print(run,len(lists))
            #print(lists)
            for i in lists:
                ob.list.append(i)
                i=None
            lists = None
            lists=[]
    return 0

cry = 50
def create(target,ob,w,h,tx,ty,pl,yyy,bwh=1):
    inWhere=0
    lands = land[randint(0,len(land)-1)]
    
    gets = maps[randint(0,len(maps)-1)]
    #gets = maps[0]
    print(gets['name'])
    print(lands['name'])
    getses = gets['start']
    h = h//bwh
    w = w//bwh
    x = 3
    y = h
    yy = 3
    lists = []
    for x in range(w):
        #print(y)
        #print(x,w/2)
        if x == 1:
            getses = gets['start']
        elif x != 0:
            if x > w/2 and randint(0,1)==0:
                getses = gets['centre']
            elif x > w/3 and randint(0,10)==0:
                getses = gets['centre']
            elif x > w/4 and randint(0,20)==0:
                getses = gets['centre']
        else:
            getses = gets['startF']
        yy = getses[randint(0,len(getses)-1)]
        yyy += yy
        #print(yyy,yy)
        x = x * bwh
        #print(yy,yyy)
        if yyy > 0:
            for i in range(yyy):
                blocks = None
                #print(x,y,tx+x,ty+y)
                if i==yyy-1:
                    #print(land[0]['start'])
                    i=lands['start'][randint(0,len(lands['start'])-1)](tx+x,0,target,pl)
                elif inWhere==0:
                    if randint(0,100)<=50:
                        inWhere = 1
                    i=lands['centre'][randint(0,len(lands['centre'])-1)](tx+x,0,target,pl)
                else:
                    i=lands['end'][randint(0,len(lands['end'])-1)](tx+x,0,target,pl)
                lists.append(i)
                for i in lists:
                    i.y += bwh
                i=None
            
            run = True
            while run:
                for xx in lists:
                    xx.y += bwh
                    #xx=None
                    #print(lists[0].y,h*bwh)
                #print(lists[len(lists)-1].y,lists[len(lists)-1].x)
                if lists[0].y >= y*bwh-bwh:
                    print(lists[0].x,lists[0].y)
                    #print('s')
                    #run = False
                    break
                #print(run,len(lists))
            #print(lists)
            for i in lists:
                ob.list.append(i)
                i=None
            lists = None
            lists=[]
    return 0
        
