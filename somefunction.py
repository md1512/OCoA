import math

##Contain some simply function 
##
##-getalpha return the radiant from 2 point 
##-prefpos
##


def getalpha(x1,y1,x2,y2):
    dis=math.sqrt(math.pow((y2-y1),2)+math.pow((x2-x1),2))
    alpha=math.acos((x2-x1)/dis)
    return alpha

def prefpos(speed,p,mp):
    np=[0,0]    
    np[0]=mp[0]-p*speed[0]
    np[1]=mp[1]-p*speed[1]
    return np
    
    
